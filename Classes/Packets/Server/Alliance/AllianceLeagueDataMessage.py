from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler



class AllianceLeagueDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        
    def encode(self, fields, player):
        self.writeByte(31)

        self.writeVInt(False) #State
        self.writeVInt(1)
        self.writeVInt(0) #Timer
        self.writeVInt(4) #Unk
        self.writeVInt(3) #Event Days' Maps

        self.writeVInt(1) #NumMap
        self.writeVInt(4) #Unk
        self.writeDataReference(15, 7) #Map
        self.writeVInt(0) #Unk

        self.writeVInt(2) #NumMap
        self.writeVInt(4) #Unk
        self.writeDataReference(15, 7) #Map
        self.writeVInt(0) #Unk

        self.writeVInt(3) #NumMap
        self.writeVInt(4) #unk
        self.writeDataReference(15, 7) #Map
        self.writeVInt(0) #unk

        self.writeBoolean(True) #League Boolean

        self.writeVLong(0, 1) # LeagueID
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVLong(0, 1) #Club?
        self.writeVInt(1) # Day number
        self.writeVInt(player.Trophies) #Trophies
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0) # Season score
        self.writeVInt(1) # Season leaderboard place
        self.writeVInt(0)

        self.writeBoolean(True)

        self.writeVLong(0, 1)
        self.writeVInt(0)
        self.writeVInt(4) #Max Golden Tickets
        self.writeVInt(0) # Used normal tickets
        self.writeVInt(0) # Max golden tickets
        self.writeVInt(0) # Used golden tickets

        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(999999)
        self.writeVInt(4)
        self.writeVInt(3)

        self.writeVInt(1)
        self.writeVInt(4)
        self.writeDataReference(15, 7)
        self.writeVInt(0)

        self.writeVInt(2)
        self.writeVInt(4)
        self.writeDataReference(15, 25)
        self.writeVInt(0)

        self.writeVInt(3)
        self.writeVInt(4)
        self.writeDataReference(15, 5)
        self.writeVInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22161

    def getMessageVersion(self):
        return self.messageVersion