from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1)
        self.writeBoolean(True) #Room or Gameroom?
        self.writeVInt(1)
        
        self.writeLong(0, 1) #hlid

        self.writeVInt(1557129593) #1594036200
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeDataReference(15, 7) #карта 3 туза
        self.writeBoolean(False)

        self.writeVInt(1) #Players
        self.writeBoolean(True) #эт когда король комната
        self.writeLong(player.ID[0], player.ID[1]) #hlid
        self.writeDataReference(16, 0)
        self.writeDataReference(29, 0)
        self.writeVInt(0) #трофеи
        self.writeVInt(0) #трофеи для ранга
        self.writeVInt(0) #мощь
        self.writeVInt(3) #state TODO: Player State
        self.writeBoolean(False) #Ready?
        self.writeVInt(0) #блу ор ред
        self.writeVInt(0) #0
        self.writeVInt(2) #2
        self.writeVInt(0) #?
        self.writeVInt(0) #?
        self.writeString(player.Name)
        self.writeVInt(0)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(0)

        self.writeDataReference(23, 76)
        self.writeDataReference(23, 255)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeInt(0)      



    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion