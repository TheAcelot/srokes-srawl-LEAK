from Classes.Packets.PiranhaMessage import PiranhaMessage


class AvatarNameCheckResponseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(0)
        self.writeInt(0)
        self.writeString(player.Name)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20300

    def getMessageVersion(self):
        return self.messageVersion