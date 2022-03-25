from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class GetPlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["HighID"] = self.readInt()
        fields["LowID"] = self.readInt()
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24113, fields, calling_instance.player)

    def getMessageType(self):
        return 14113

    def getMessageVersion(self):
        return self.messageVersion