from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class LeaderboardMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("RU")

        self.writeVInt(2)

        for i in ["Жалко, но тут ничего нет", "It's a pity, but there's nothing here"]:

            self.writeVInt(0)
            self.writeVInt(1)

            self.writeVInt(1)
            self.writeVInt(0) #trophies

            self.writeVInt(1)
            self.writeString("t.me/vokesbrawl")

            self.writeString(i)
            self.writeVInt(0)
            self.writeVInt(28000069)
            self.writeVInt(43000005)
            self.writeVInt(46000005)
            self.writeVInt(0) #UNK

        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("RU")

        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24403

    def getMessageVersion(self):
        return self.messageVersion