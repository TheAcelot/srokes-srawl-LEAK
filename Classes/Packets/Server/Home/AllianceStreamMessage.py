from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class AllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)
        self.writeVInt(1)
        self.writeVInt(2) #Event
        self.writeVInt(0)
        self.writeVInt(playerData["TickMessage"]) #NumEvent
        self.writeVInt(player.ID[0])
        self.writeVInt(player.ID[1])
        self.writeString(player.Name)
        self.writeVInt(2) #Role
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeString(playerData["ClubMessage"])
        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24311

    def getMessageVersion(self):
        return self.messageVersion