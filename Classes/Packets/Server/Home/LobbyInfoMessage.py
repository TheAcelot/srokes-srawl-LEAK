from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
import time
import psutil
from Database.DatabaseHandler import DatabaseHandler

class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db = DatabaseHandler()
        accs = len(db.getAll(0))
        self.writeVInt(ClientsManager.GetCount())
        self.writeString(f"SROKES SRAWL LEAK by TheAcelot!")
        self.writeVInt(0)

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion