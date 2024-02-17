# AlbionMaster

AlbionMaster is a sophisticated API designed for orchestrating multi-boxing strategies in Albion Online. The primary objective is to streamline gameplay by enabling concurrent execution of tasks, such as performing multiple Heart Transport Missions simultaneously and efficiently clearing dungeons.

## Purpose

This project aims to enhance the gaming experience by seamlessly managing multiple Albion Online accounts. The key functionalities include:

- Coordinating the movements and actions of a master player across multiple accounts.
- Optimizing dungeon clearing processes through synchronized actions.

## Strategy

The strategic approach involves implementing two distinct components: the "Master" service and the "Slave" service. The "Master" service is responsible for providing real-time updates on the main player's position, health, and potential threats, allowing the "Slave" service to respond intelligently.

### Implementation Plan:

1. **API Development:**
    - Utilize FastAPI to construct a robust API that efficiently retrieves crucial data from the main player.
    - Implement endpoints for retrieving real-time information, focusing on key parameters like position and attacker entities.

2. **Bot Development:**
    - Craft a sophisticated bot capable of emulating the actions of the main player.
    - Ensure seamless synchronization between the "Master" and "Slave" services for optimal multi-boxing performance.

## TODO:

- **Build API:**
    - [x] Implement endpoint for retrieving the player's current position.
    - [ ] Implement endpoint for tracking attacker entities.

Stay tuned for updates as we continue to refine and enhance AlbionMaster for a seamless multi-boxing experience in Albion Online.
