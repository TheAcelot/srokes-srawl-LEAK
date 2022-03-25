from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class AvatarNameCheckRequestMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeString(fields["Name"])
        self.writeBoolean(fields["NameSetByUser"])

    def decode(self):
        fields = {}
        fields["Name"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        print(playerData)
        playerData["Name"] = fields["Name"]
        db_instance.updatePlayerData(playerData, calling_instance)
        Messaging.sendMessage(20300, fields, calling_instance.player)

    def getMessageType(self):
        return 14600

    def getMessageVersion(self):
        return self.messageVersion