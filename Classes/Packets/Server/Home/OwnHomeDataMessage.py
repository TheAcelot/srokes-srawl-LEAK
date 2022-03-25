import time
import random

from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(player.Trophies) # Trophies
        self.writeVInt(player.HighestTrophies + 50000) # Highest Trophies
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(0)

        self.writeVInt(1) # Selected Skins
        self.writeDataReference(29, player.SelectedSkin)
        print(player.SelectedSkin)

        self.writeVInt(0) # Randomizer Skin Selected

        self.writeVInt(0) # Current Random Skin

        if player.Trophies <= 139:
            
            self.writeVInt(len(ownedSkins))
            
            for skinID in ownedSkins:
                self.writeDataReference(29, skinID)
        else:
            self.writeVInt(len(ownedSkins) + 1)
            
            for skinID in ownedSkins:
                self.writeDataReference(29, skinID)
            self.writeDataReference(29, 437)


        self.writeVInt(0) # Unlocked Skin Purchase Option

        self.writeVInt(0) # New Item State

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(10000)
        self.writeVInt(10000)
        self.writeVInt(10000)

        self.writeVInt(1)
        self.writeVInt(1)

        self.writeVInt(5) #rares

        self.writeVInt(93)
        self.writeVInt(206)
        self.writeVInt(456)
        self.writeVInt(792)
        self.writeVInt(729)

        self.writeBoolean(True) # Offer 1
        self.writeDataReference(2, random.randint(0, 234))
        self.writeInt(0) #Time
        self.writeInt(0) #Readed
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(6974)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change

        self.writeVInt(0) # Offers count

        # self.writeVInt(1)  # RewardCount
        # for i in range(1):
        #    self.writeVInt(6)  # ItemType
        #    self.writeVInt(0)
        #    self.writeDataReference(0)  # CsvID
        #    self.writeVInt(0)

        # self.writeVInt(4)
        # self.writeVInt(150)
        # self.writeVInt(950400)
        # self.writeVInt(2)
        # self.writeVInt(0)
        # self.writeBoolean(False)
        # self.writeVInt(3917)
        # self.writeVInt(0)
        # self.writeBoolean(False)
        # self.writeVInt(49)
        # self.writeInt(0)
        # self.writeString("С ДНЁМ ВЛЮБЛЁННЫХ")
        # self.writeBoolean(False)
        # self.writeString('offer_stv')
        # self.writeVInt(-1)
        # self.writeBoolean(False)
        # self.writeVInt(0)
        # self.writeVInt(0)
        # self.writeString()
        # self.writeBoolean(False)
        # self.writeBoolean(False)

        self.writeVInt(0)

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(1)
        self.writeDataReference(16, player.SelectedBrawler)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVInt(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        if player.Trophies <= 1250:
            self.writeLong(4, player.Trophies)  # TrophiesGained
        else:
            self.writeLong(4, 1250)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        self.writeLong(9, 1)  # ShowStarPoints
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 0)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 0)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 0)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0)

        self.writeVInt(10)  # Brawlpass
        for i in range(10):
            self.writeVInt(i)
            if i != 0:
                self.writeVInt(34500)
            else:
                self.writeVInt(28500)
            self.writeBoolean(True)
            self.writeVInt(0)

            self.writeByte(2)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(512)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(512)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True) #quest entry
        self.writeVInt(1)
        self.writeVInt(0) #UNK
        self.writeVInt(0) #UNK
        self.writeVInt(3) #Mission Type
        self.writeVInt(player.Trophies) #Completed Points
        self.writeVInt(player.Trophies + 100000) #Mission Int \ Max Points
        self.writeVInt(player.Trophies) #Tokens
        self.writeVInt(0) #UNK
        self.writeVInt(0) #UNK
        self.writeVInt(0) #Mission Level (0/5)
        self.writeVInt(9999) #Timer
        self.writeBoolean(False) #Only with BP
        self.writeBoolean(False) #New State
        self.writeDataReference(0) #Brawler
        self.writeVInt(3) #GameMode (0 - GemGrab, 3 - Bounty)
        self.writeVInt(0) #UNK
        self.writeVInt(0) #UNK
        self.writeVInt(0) #UNK  


        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(25) # Count

        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        self.writeVInt(10) # Events
        index = 1

        for i in [112, 8, 9, 5, 22, 54]:
            self.writeVInt(-1)
            self.writeVInt(index)  # EventType
            self.writeVInt(0)  # EventsBeginCountdown
            self.writeVInt(51208)  # Timer
            self.writeVInt(0)  # tokens reward for new event
            self.writeDataReference(15, i)  # MapID
            self.writeVInt(-1)  # GameModeVariation
            self.writeVInt(2)  # State
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)  # Modifiers
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # Map Maker Map Structure Array
            self.writeVInt(0)
            self.writeBoolean(False)  # Power League Data Array
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # ChronosTextEntry
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(-1)
            self.writeBoolean(False)
            self.writeBoolean(False)
            index += 1

        self.writeVInt(0)
        self.writeVInt(16)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 7)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # ChronosTextEntry
        self.writeVInt(-64)
        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(17)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 25)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # ChronosTextEntry
        self.writeVInt(-64)
        self.writeBoolean(False)

                # Power League Solo Mode #
        self.writeVInt(0)
        self.writeVInt(14)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 4)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) #zh
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Power League Team Mode #
        self.writeVInt(0)
        self.writeVInt(15)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 4)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(6) # Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0) # Comming Events

        self.writeVInt(10)  # Brawler Upgrade Cost
        self.writeVInt(20)
        self.writeVInt(35)
        self.writeVInt(75)
        self.writeVInt(140)
        self.writeVInt(290)
        self.writeVInt(480)
        self.writeVInt(800)
        self.writeVInt(1250)
        self.writeVInt(1875)
        self.writeVInt(2800)

        self.writeVInt(4)  # Shop Coins Price
        self.writeVInt(20)
        self.writeVInt(50)
        self.writeVInt(140)
        self.writeVInt(280)

        self.writeVInt(4)  # Shop Coins Amount
        self.writeVInt(150)
        self.writeVInt(400)
        self.writeVInt(1200)
        self.writeVInt(2600)

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0)

        self.writeVInt(21)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        from Database.DatabaseHandler import DatabaseHandler
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)
        self.writeLong(1, 41000000 + playerData["ThemeID"]) # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270) # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, 12) # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 0) # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0) # Double Token Event
        self.writeLong(31, 0) # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(10046, 1)

        self.writeVInt(2)  # Timed Int Value Entry

        # Double tokens event
        self.writeVInt(14)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(700000) # Time left

        # Gold rush event
        self.writeVInt(31)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(700000) # Time left

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVInt(1) # NotificationFactory

        self.writeVInt(83) # чо
        self.writeInt(0)
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("SaVok")
        self.writeInt(0)
        self.writeString("Добро пожаловать в Voke's Brawl!")

        self.writeInt(0)
        self.writeString("Поддержи наш проект и зайди в телеграм")

        self.writeInt(0)
        self.writeString("ТЕЛЕГРАМ")

        self.writeString("/b2d704b22b95a4d70f66e89da867a64b")
        self.writeString('3a35620676c1d08d12086257a5ae03eb612452d8')

        self.writeString("brawlstars://extlink?page=https%3A%2F%2Ft.me%2Fvokesbrawl")
        self.writeVInt(3473)
        

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVInt(15)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(99999) # Club coins

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(player.Gems)  # Diamonds
        self.writeVInt(player.Gems)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
