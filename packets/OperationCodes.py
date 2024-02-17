from enum import IntEnum, auto


class OperationCodes(IntEnum):
    Unused = 0
    Ping = auto()
    Join = auto()
    VersionedOperation = auto()
    CreateAccount = auto()
    Login = auto()
    CreateGuestAccount = auto()
    SendCrashLog = auto()
    SendTraceRoute = auto()
    SendVfxStats = auto()
    SendGamePingInfo = auto()
    CreateCharacter = auto()
    DeleteCharacter = auto()
    SelectCharacter = auto()
    AcceptPopups = auto()
    RedeemKeycode = auto()
    GetGameServerByCluster = auto()
    GetShopPurchaseUrl = auto()
    GetReferralSeasonDetails = auto()
    GetReferralLink = auto()
    GetShopTilesForCategory = auto()
    Move = auto()
    AttackStart = auto()
    CastStart = auto()
    CastCancel = auto()
    TerminateToggleSpell = auto()
    ChannelingCancel = auto()
    AttackBuildingStart = auto()
    InventoryDestroyItem = auto()
    InventoryMoveItem = auto()
    InventoryRecoverItem = auto()
    InventoryRecoverAllItems = auto()
    InventorySplitStack = auto()
    InventorySplitStackInto = auto()
    GetClusterData = auto()
    ChangeCluster = auto()
    ConsoleCommand = auto()
    ChatMessage = auto()
    ReportClientError = auto()
    RegisterToObject = auto()
    UnRegisterFromObject = auto()
    CraftBuildingChangeSettings = auto()
    CraftBuildingTakeMoney = auto()
    RepairBuildingChangeSettings = auto()
    RepairBuildingTakeMoney = auto()
    ActionBuildingChangeSettings = auto()
    HarvestStart = auto()
    HarvestCancel = auto()
    TakeSilver = auto()
    ActionOnBuildingStart = auto()
    ActionOnBuildingCancel = auto()
    InstallResourceStart = auto()
    InstallResourceCancel = auto()
    InstallSilver = auto()
    BuildingFillNutrition = auto()
    BuildingChangeRenovationState = auto()
    BuildingBuySkin = auto()
    BuildingClaim = auto()
    BuildingGiveup = auto()
    BuildingNutritionSilverStorageDeposit = auto()
    BuildingNutritionSilverStorageWithdraw = auto()
    BuildingNutritionSilverRewardSet = auto()
    ConstructionSiteCreate = auto()
    PlaceableObjectPlace = auto()
    PlaceableObjectPlaceCancel = auto()
    PlaceableObjectPickup = auto()
    FurnitureObjectUse = auto()
    FarmableHarvest = auto()
    FarmableFinishGrownItem = auto()
    FarmableDestroy = auto()
    FarmableGetProduct = auto()
    FarmableFill = auto()
    TearDownConstructionSite = auto()
    CastleGateUse = auto()
    AuctionCreateOffer = auto()
    AuctionCreateRequest = auto()
    AuctionGetOffers = auto()
    AuctionGetRequests = auto()
    AuctionBuyOffer = auto()
    AuctionAbortAuction = auto()
    AuctionModifyAuction = auto()
    AuctionAbortOffer = auto()
    AuctionAbortRequest = auto()
    AuctionSellRequest = auto()
    AuctionGetFinishedAuctions = auto()
    AuctionGetFinishedAuctionsCount = auto()
    AuctionFetchAuction = auto()
    AuctionGetMyOpenOffers = auto()
    AuctionGetMyOpenRequests = auto()
    AuctionGetMyOpenAuctions = auto()
    AuctionGetItemAverageStats = auto()
    AuctionGetItemAverageValue = auto()
    ContainerOpen = auto()
    ContainerClose = auto()
    ContainerManageSubContainer = auto()
    Respawn = auto()
    Suicide = auto()
    JoinGuild = auto()
    LeaveGuild = auto()
    CreateGuild = auto()
    InviteToGuild = auto()
    DeclineGuildInvitation = auto()
    KickFromGuild = auto()
    InstantJoinGuild = auto()
    DuellingChallengePlayer = auto()
    DuellingAcceptChallenge = auto()
    DuellingDenyChallenge = auto()
    ChangeClusterTax = auto()
    ClaimTerritory = auto()
    GiveUpTerritory = auto()
    ChangeTerritoryAccessRights = auto()
    GetMonolithInfo = auto()
    GetClaimInfo = auto()
    GetAttackInfo = auto()
    GetTerritorySeasonPoints = auto()
    GetAttackSchedule = auto()
    GetMatches = auto()
    GetMatchDetails = auto()
    JoinMatch = auto()
    LeaveMatch = auto()
    ChangeChatSettings = auto()
    LogoutStart = auto()
    LogoutCancel = auto()
    ClaimOrbStart = auto()
    ClaimOrbCancel = auto()
    MatchLootChestOpeningStart = auto()
    MatchLootChestOpeningCancel = auto()
    DepositToGuildAccount = auto()
    WithdrawalFromAccount = auto()
    ChangeGuildPayUpkeepFlag = auto()
    ChangeGuildTax = auto()
    GetMyTerritories = auto()
    MorganaCommand = auto()
    GetServerInfo = auto()
    SubscribeToCluster = auto()
    AnswerMercenaryInvitation = auto()
    GetCharacterEquipment = auto()
    GetCharacterSteamAchievements = auto()
    GetCharacterStats = auto()
    GetKillHistoryDetails = auto()
    LearnMasteryLevel = auto()
    ReSpecAchievement = auto()
    ChangeAvatar = auto()
    GetRankings = auto()
    GetRank = auto()
    GetGvgSeasonRankings = auto()
    GetGvgSeasonRank = auto()
    GetGvgSeasonHistoryRankings = auto()
    GetGvgSeasonGuildMemberHistory = auto()
    KickFromGvGMatch = auto()
    GetCrystalLeagueDailySeasonPoints = auto()
    GetChestLogs = auto()
    GetAccessRightLogs = auto()
    GetGuildAccountLogs = auto()
    GetGuildAccountLogsLargeAmount = auto()
    InviteToPlayerTrade = auto()
    PlayerTradeCancel = auto()
    PlayerTradeInvitationAccept = auto()
    PlayerTradeAddItem = auto()
    PlayerTradeRemoveItem = auto()
    PlayerTradeAcceptTrade = auto()
    PlayerTradeSetSilverOrGold = auto()
    SendMiniMapPing = auto()
    Stuck = auto()
    BuyRealEstate = auto()
    ClaimRealEstate = auto()
    GiveUpRealEstate = auto()
    ChangeRealEstateOutline = auto()
    GetMailInfos = auto()
    GetMailCount = auto()
    ReadMail = auto()
    SendNewMail = auto()
    DeleteMail = auto()
    MarkMailUnread = auto()
    ClaimAttachmentFromMail = auto()
    ApplyToGuild = auto()
    AnswerGuildApplication = auto()
    RequestGuildFinderFilteredList = auto()
    UpdateGuildRecruitmentInfo = auto()
    RequestGuildRecruitmentInfo = auto()
    RequestGuildFinderNameSearch = auto()
    RequestGuildFinderRecommendedList = auto()
    RegisterChatPeer = auto()
    SendChatMessage = auto()
    SendModeratorMessage = auto()
    JoinChatChannel = auto()
    LeaveChatChannel = auto()
    SendWhisperMessage = auto()
    Say = auto()
    PlayEmote = auto()
    StopEmote = auto()
    GetClusterMapInfo = auto()
    AccessRightsChangeSettings = auto()
    Mount = auto()
    MountCancel = auto()
    BuyJourney = auto()
    SetSaleStatusForEstate = auto()
    ResolveGuildOrPlayerName = auto()
    GetRespawnInfos = auto()
    MakeHome = auto()
    LeaveHome = auto()
    ResurrectionReply = auto()
    AllianceCreate = auto()
    AllianceDisband = auto()
    AllianceGetMemberInfos = auto()
    AllianceInvite = auto()
    AllianceAnswerInvitation = auto()
    AllianceCancelInvitation = auto()
    AllianceKickGuild = auto()
    AllianceLeave = auto()
    AllianceChangeGoldPaymentFlag = auto()
    AllianceGetDetailInfo = auto()
    GetIslandInfos = auto()
    AbandonMyIsland = auto()
    BuyMyIsland = auto()
    BuyGuildIsland = auto()
    AbandonGuildIsland = auto()
    UpgradeMyIsland = auto()
    UpgradeGuildIsland = auto()
    MoveMyIsland = auto()
    MoveGuildIsland = auto()
    TerritoryFillNutrition = auto()
    TeleportBack = auto()
    PartyInvitePlayer = auto()
    PartyRequestJoin = auto()
    PartyAnswerInvitation = auto()
    PartyAnswerJoinRequest = auto()
    PartyLeave = auto()
    PartyKickPlayer = auto()
    PartyMakeLeader = auto()
    PartyChangeLootSetting = auto()
    PartyMarkObject = auto()
    PartySetRole = auto()
    SetGuildCodex = auto()
    ExitEnterStart = auto()
    ExitEnterCancel = auto()
    QuestGiverRequest = auto()
    GoldMarketGetBuyOffer = auto()
    GoldMarketGetBuyOfferFromSilver = auto()
    GoldMarketGetSellOffer = auto()
    GoldMarketGetSellOfferFromSilver = auto()
    GoldMarketBuyGold = auto()
    GoldMarketSellGold = auto()
    GoldMarketCreateSellOrder = auto()
    GoldMarketCreateBuyOrder = auto()
    GoldMarketGetInfos = auto()
    GoldMarketCancelOrder = auto()
    GoldMarketGetAverageInfo = auto()
    TreasureChestUsingStart = auto()
    TreasureChestUsingCancel = auto()
    UseLootChest = auto()
    UseShrine = auto()
    UseHellgateShrine = auto()
    LaborerStartJob = auto()
    LaborerTakeJobLoot = auto()
    LaborerDismiss = auto()
    LaborerMove = auto()
    LaborerBuyItem = auto()
    LaborerUpgrade = auto()
    BuyPremium = auto()
    RealEstateGetAuctionData = auto()
    RealEstateBidOnAuction = auto()
    FriendInvite = auto()
    FriendAnswerInvitation = auto()
    FriendCancelnvitation = auto()
    FriendRemove = auto()
    InventoryStack = auto()
    InventorySort = auto()
    InventoryDropAll = auto()
    InventoryAddToStacks = auto()
    EquipmentItemChangeSpell = auto()
    ExpeditionRegister = auto()
    ExpeditionRegisterCancel = auto()
    JoinExpedition = auto()
    DeclineExpeditionInvitation = auto()
    VoteStart = auto()
    VoteDoVote = auto()
    RatingDoRate = auto()
    EnteringExpeditionStart = auto()
    EnteringExpeditionCancel = auto()
    ActivateExpeditionCheckPoint = auto()
    ArenaRegister = auto()
    ArenaAddInvite = auto()
    ArenaRegisterCancel = auto()
    ArenaLeave = auto()
    JoinArenaMatch = auto()
    DeclineArenaInvitation = auto()
    EnteringArenaStart = auto()
    EnteringArenaCancel = auto()
    ArenaCustomMatch = auto()
    UpdateCharacterStatement = auto()
    BoostFarmable = auto()
    GetStrikeHistory = auto()
    UseFunction = auto()
    UsePortalEntrance = auto()
    ResetPortalBinding = auto()
    QueryPortalBinding = auto()
    ClaimPaymentTransaction = auto()
    ChangeUseFlag = auto()
    ClientPerformanceStats = auto()
    ExtendedHardwareStats = auto()
    ClientLowMemoryWarning = auto()
    TerritoryClaimStart = auto()
    TerritoryClaimCancel = auto()
    ClaimPowerCrystalStart = auto()
    ClaimPowerCrystalCancel = auto()
    TerritoryUpgradeWithPowerCrystal = auto()
    RequestAppStoreProducts = auto()
    VerifyProductPurchase = auto()
    QueryGuildPlayerStats = auto()
    QueryAllianceGuildStats = auto()
    TrackAchievements = auto()
    SetAchievementsAutoLearn = auto()
    DepositItemToGuildCurrency = auto()
    WithdrawalItemFromGuildCurrency = auto()
    AuctionSellSpecificItemRequest = auto()
    FishingStart = auto()
    FishingCasting = auto()
    FishingCast = auto()
    FishingCatch = auto()
    FishingPull = auto()
    FishingGiveLine = auto()
    FishingFinish = auto()
    FishingCancel = auto()
    CreateGuildAccessTag = auto()
    DeleteGuildAccessTag = auto()
    RenameGuildAccessTag = auto()
    FlagGuildAccessTagGuildPermission = auto()
    AssignGuildAccessTag = auto()
    RemoveGuildAccessTagFromPlayer = auto()
    ModifyGuildAccessTagEditors = auto()
    RequestPublicAccessTags = auto()
    ChangeAccessTagPublicFlag = auto()
    UpdateGuildAccessTag = auto()
    SteamStartMicrotransaction = auto()
    SteamFinishMicrotransaction = auto()
    SteamIdHasActiveAccount = auto()
    CheckEmailAccountState = auto()
    LinkAccountToSteamId = auto()
    InAppConfirmPaymentGooglePlay = auto()
    InAppConfirmPaymentAppleAppStore = auto()
    InAppPurchaseRequest = auto()
    InAppPurchaseFailed = auto()
    CharacterSubscriptionInfo = auto()
    AccountSubscriptionInfo = auto()
    BuyGvgSeasonBooster = auto()
    ChangeFlaggingPrepare = auto()
    OverCharge = auto()
    OverChargeEnd = auto()
    RequestTrusted = auto()
    ChangeGuildLogo = auto()
    PartyFinderRegisterForUpdates = auto()
    PartyFinderUnregisterForUpdates = auto()
    PartyFinderEnlistNewPartySearch = auto()
    PartyFinderDeletePartySearch = auto()
    PartyFinderChangePartySearch = auto()
    PartyFinderChangeRole = auto()
    PartyFinderApplyForGroup = auto()
    PartyFinderAcceptOrDeclineApplyForGroup = auto()
    PartyFinderGetEquipmentSnapshot = auto()
    PartyFinderRegisterApplicants = auto()
    PartyFinderUnregisterApplicants = auto()
    PartyFinderFulltextSearch = auto()
    PartyFinderRequestEquipmentSnapshot = auto()
    GetPersonalSeasonTrackerData = auto()
    GetPersonalSeasonPastRewardData = auto()
    UseConsumableFromInventory = auto()
    ClaimPersonalSeasonReward = auto()
    EasyAntiCheatMessageToServer = auto()
    XignCodeMessageToServer = auto()
    BattlEyeMessageToServer = auto()
    SetNextTutorialState = auto()
    AddPlayerToMuteList = auto()
    RemovePlayerFromMuteList = auto()
    ProductShopUserEvent = auto()
    GetVanityUnlocks = auto()
    BuyVanityUnlocks = auto()
    GetMountSkins = auto()
    SetMountSkin = auto()
    SetWardrobe = auto()
    ChangeCustomization = auto()
    ChangePlayerIslandData = auto()
    GetGuildChallengePoints = auto()
    SmartQueueJoin = auto()
    SmartQueueLeave = auto()
    SmartQueueSelectSpawnCluster = auto()
    UpgradeHideout = auto()
    InitHideoutAttackStart = auto()
    InitHideoutAttackCancel = auto()
    HideoutFillNutrition = auto()
    HideoutGetInfo = auto()
    HideoutGetOwnerInfo = auto()
    HideoutSetTribute = auto()
    HideoutUpgradeWithPowerCrystal = auto()
    HideoutDeclareHQ = auto()
    HideoutUndeclareHQ = auto()
    HideoutGetHQRequirements = auto()
    HideoutBoost = auto()
    HideoutBoostConstruction = auto()
    OpenWorldAttackScheduleStart = auto()
    OpenWorldAttackScheduleCancel = auto()
    OpenWorldAttackConquerStart = auto()
    OpenWorldAttackConquerCancel = auto()
    GetOpenWorldAttackDetails = auto()
    GetNextOpenWorldAttackScheduleTime = auto()
    RecoverVaultFromHideout = auto()
    GetGuildEnergyDrainInfo = auto()
    ChannelingUpdate = auto()
    UseCorruptedShrine = auto()
    RequestEstimatedMarketValue = auto()
    LogFeedback = auto()
    GetInfamyInfo = auto()
    GetPartySmartClusterQueuePriority = auto()
    SetPartySmartClusterQueuePriority = auto()
    ClientAntiAutoClickerInfo = auto()
    ClientBotPatternDetectionInfo = auto()
    ClientAntiGatherClickerInfo = auto()
    LoadoutCreate = auto()
    LoadoutRead = auto()
    LoadoutReadHeaders = auto()
    LoadoutUpdate = auto()
    LoadoutDelete = auto()
    LoadoutOrderUpdate = auto()
    LoadoutEquip = auto()
    BatchUseItemCancel = auto()
    EnlistFactionWarfare = auto()
    GetFactionWarfareWeeklyReport = auto()
    ClaimFactionWarfareWeeklyReport = auto()
    GetFactionWarfareCampaignData = auto()
    ClaimFactionWarfareItemReward = auto()
    SendMemoryConsumption = auto()
    PickupPowerCrystalStart = auto()
    PickupPowerCrystalCancel = auto()
    SetSavingChestLogsFlag = auto()
    GetSavingChestLogsFlag = auto()
    RegisterGuestAccount = auto()
    ResendGuestAccountVerificationEmail = auto()
    DoSimpleActionStart = auto()
    DoSimpleActionCancel = auto()
    GetGvgSeasonContributionByActivity = auto()
    GetGvgSeasonContributionByCrystalLeague = auto()
    GetGuildMightCategoryContribution = auto()
    GetGuildMightCategoryOverview = auto()
    GetPvpChallengeData = auto()
    ClaimPvpChallengeWeeklyReward = auto()
    GetPersonalMightStats = auto()
    AuctionGetLoadoutOffers = auto()
    AuctionBuyLoadoutOffer = auto()
    AccountDeletionRequest = auto()
    AccountReactivationRequest = auto()
    GetModerationEscalationDefiniton = auto()
    EventBasedPopupAddSeen = auto()
    GetItemKillHistory = auto()
    GetVanityConsumables = auto()
    EquipKillEmote = auto()
    ChangeKillEmotePlayOnKnockdownSetting = auto()
    BuyVanityConsumableCharges = auto()
    ReclaimVanityItem = auto()
    GetArenaRankings = auto()
    GetCrystalLeagueStatistics = auto()
    SendOptionsLog = auto()
    SendControlsOptionsLog = auto()
    MistsUseImmediateReturnExit = auto()
    MistsUseStaticEntrance = auto()
    MistsUseCityRoadsEntrance = auto()
    ChangeNewGuildMemberMail = auto()
    GetNewGuildMemberMail = auto()
    ChangeGuildFactionAllegiance = auto()
    GetGuildFactionAllegiance = auto()
    GuildBannerChange = auto()
    GuildGetOptionalStats = auto()
    GuildSetOptionalStats = auto()
    GetPlayerInfoForStalk = auto()
    PayGoldForCharacterTypeChange = auto()
    QuickSellAuctionQueryAction = auto()
    QuickSellAuctionSellAction = auto()
    FcmTokenToServer = auto()
    ApnsTokenToServer = auto()
    DeathRecap = auto()
    AuctionFetchFinishedAuctions = auto()
    AbortAuctionFetchFinishedAuctions = auto()
    RequestLegendaryEvenHistory = auto()
    PartyAnswerStartHuntRequest = auto()
    HuntAbort = auto()
    UseFindTrackSpellFromItemPrepare = auto()
    InteractWithTrackStart = auto()
    InteractWithTrackCancel = auto()
    TerritoryRaidStart = auto()
    TerritoryRaidCancel = auto()
    TerritoryClaimRaidedRawEnergyCrystalResult = auto()
    GvGSeasonPlayerGuildParticipationDetails = auto()
    DailyMightBonus = auto()
    ClaimDailyMightBonus = auto()