from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler
import random as r
from Classes.Packets.Client.Home.AskForAllianceDataMessage import AskForAllianceDataMessage


class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):

        self.writeBoolean(True) #Show Online Players
        db = DatabaseHandler()
        entry = db.load_all()
        another = len(db.getAll(0))
        allSockets = ClientsManager.GetAll()

        self.writeLong(0, 1) #hlid
        self.writeString("<c3200ff>V<c6500ff>o<c9800ff>k<ccb00ff>e<cff00ff>s<cff00cc>B<cff0099>r<cff0066>a<cff0033>w<cff0001>l</c>") #name
        self.writeDataReference(8, 18) #badge
        self.writeVInt(3) # Type
        self.writeVInt(another)  # Total Members
        self.writeVInt(player.Trophies)  # Total Trophies
        self.writeVInt(0)  # Trophies Required
        self.writeDataReference(0)
        self.writeString("RU")  # Region
        self.writeVInt(0)
        self.writeBoolean(False)  # Family Friendly
        self.writeVInt(0)

        self.writeString("tg: @vokesbrawl\ndiscord: https://discord.gg/XhV3n8WkzN") # Description

        self.writeVInt(len(entry)) # Members Count
        for data in entry:
            self.writeLong(data["ID"][0], data["ID"][1])
            if data["ID"][1] == 46879790:
                self.writeVInt(2) # Role
            else:
                self.writeVInt(4)
            self.writeVInt(data["Trophies"]) # Trophies
            if data["ID"][1] in allSockets:
                self.writeVInt(2) # Player State TODO: Members state
            else:
                self.writeVInt(0)
            self.writeVInt(6974) # State Timer

            # whatIsThat = 5
            self.writeVInt(1)
            self.writeVInt(1) # idk
            self.writeVInt(19) # Power League Rank
            self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            self.writeString(data["Name"]) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000 + data["Thumbnail"]) # Player Thumbnail
            self.writeVInt(43000000 + data["Namecolor"]) # Player Name Color
            self.writeVInt(46000001) # Color Gradients

            self.writeVInt(-1)
            self.writeBoolean(False)

            self.writeVInt(0) # Club Leauge?
        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        print("hi")

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion