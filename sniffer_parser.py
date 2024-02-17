from threading import Thread
import subprocess
import json
import traceback
import os
import platform
from getpass import getpass
from queue import Queue, Empty

from albion_classes.Player import Player
from packets.OperationCodes import OperationCodes


def parse_code(line: str):
    f_find = line.find('][') + 2
    s_find = line.find(']', f_find, f_find + 5)
    return int(line[f_find:s_find])


def parse_map(line, map_index) -> dict:
    try:
        result = json.loads(line[map_index:])
    except json.decoder.JSONDecodeError:
        print("Error parseMap:")
        print(line)
        return {}

    return result


def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        try:
            queue.put(line.decode('utf-8'))
        except UnicodeDecodeError:
            print("Error de Decodificacion:")
            print(line)
    out.close()


class AlbionPacketSniffer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.daemon = False

        self.external_sniffer = None
        self.sniffer = None
        self.queue = Queue()
        self.open_sniffer()

        # Character Info
        self.player = Player()

        # Running flag
        self.reading = False

    def open_sniffer(self):
        if os.name == 'nt' or platform.system() == 'Windows':
            comand = [r'./AOSnifferNET/AOSnifferNET.exe']
            try:
                self.external_sniffer = subprocess.Popen(comand,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE,
                                                         creationflags=subprocess.CREATE_NO_WINDOW
                                                         )
            except:
                print(traceback.format_exc())
        elif os.name == 'posix' or platform.system() == 'Linux':
            password = getpass("Please enter your user password: ")
            comand = r"sudo -S mono ./AOSnifferNET/AOSnifferNET.exe".split()
            try:
                self.external_sniffer = subprocess.Popen(comand,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE,
                                                         stdin=subprocess.PIPE
                                                         )
            except:
                print(traceback.format_exc())

            password += "\n"
            self.external_sniffer.stdin.write(password.encode())
            self.external_sniffer.stdin.flush()

        self.sniffer = Thread(target=enqueue_output, args=(self.external_sniffer.stdout, self.queue))
        self.sniffer.daemon = False
        self.sniffer.start()

    def reopen_sniffer(self):
        print("Reabriendo sniffer")
        self.destroy()
        self.sniffer = None
        self.open_sniffer()

    def run(self):
        self.reading = True
        while self.reading:
            '''Packet reading'''
            line = ""
            try:
                line = self.queue.get(timeout=30)  # q.get_nowait()  # or q.get(timeout=.1)
            except Empty:
                if self.reading and self.external_sniffer.poll is not None:
                    self.reopen_sniffer()
                continue

            map_index = line.find('{')
            if map_index != -1:
                indice_fin = line.find("]")
                packet_type = line[3:indice_fin]
                # Login Packets
                if packet_type.find('L') != -1:
                    pass
                # Special Packets
                elif packet_type.find('En') != -1:
                    pass

                # Events
                elif packet_type.find('Ev') != -1:
                    pass
                # Operations Requests
                elif packet_type.find('Req') != -1:
                    op_code = parse_code(line)

                    if op_code == OperationCodes.Move.value:
                        map_data = parse_map(line, map_index)

                        self.parse_player_loc(map_data)
                        self.player.speed = map_data['speed']
                        self.player.angle = map_data['angle']
                # Operations Response
                elif packet_type.find('Res') != -1:
                    op_code = parse_code(line)

                    if op_code == OperationCodes.Join.value:
                        map_data = parse_map(line, map_index)
                        self.parse_player_loc(map_data)
                        # cluster id
                        cluster_id = str(map_data['cluster'])
                        remain = 4 - len(cluster_id)
                        cluster_id = '0' * remain + cluster_id
                        self.player.init(
                            map_data['characterId'],
                            map_data['markId'],
                            map_data['characterName'],
                            cluster_id,
                            map_data['pos'],
                            map_data['currentHealth'],
                            map_data['maxHealth'],
                            map_data['currentEnergy'],
                            map_data['maxEnergy'],
                            map_data['faction']
                        )
                        self.player.angle = map_data['angle']

    def stop(self):
        self.reading = False
        print("Sniffer Terminated.")

    def destroy(self):
        self.external_sniffer.terminate()
        self.external_sniffer.wait()
        print("Sniffer Destroyed.")

    def parse_player_loc(self, map_data):
        try:
            pos = map_data['pos']
        except KeyError:
            pos = map_data['0']
        except:
            print(f'Error parseando loc de jugador: {map_data}')
            pos = 0, 0

        self.player.set_pos(pos)

        try:
            target = map_data['target']
            self.player.target_pos = target
        except KeyError:
            pass
