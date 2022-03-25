from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer([fields["HighID"], fields["LowID"]])


        self.writeVInt(fields["HighID"])
        self.writeVInt(fields["LowID"])
        self.writeBoolean(False)

        self.writeVInt(55)

        for i in range(54):
            self.writeDataReference(16, i)
            self.writeVInt(0)
            self.writeVInt(playerData["OwnedBrawlers"][f"{i}"]["Trophies"])
            self.writeVInt(playerData["OwnedBrawlers"][f"{i}"]["HighestTrophies"])
            self.writeVInt(11)
        
        self.writeDataReference(16, 54)
        self.writeVInt(0)
        self.writeVInt(playerData["OwnedBrawlers"][f"54"]["Trophies"])
        self.writeVInt(playerData["OwnedBrawlers"][f"54"]["HighestTrophies"])
        self.writeVInt(11)

        self.writeVInt(15)

        self.writeVInt(1)
        self.writeVInt(10000) #3vs3 wins

        self.writeVInt(2)
        self.writeVInt(428000) #XP

        self.writeVInt(3)
        self.writeVInt(playerData["Trophies"]) #HighestTrophies

        self.writeVInt(4)
        self.writeVInt(playerData["Trophies"]) #Trophies

        self.writeVInt(5)
        self.writeVInt(55) #Brawlers list

        self.writeVInt(7)
        self.writeVInt(28000000 + playerData["Thumbnail"]) #ProfileIcon

        self.writeVInt(8)
        self.writeVInt(10000) #SoloWins

        self.writeVInt(9)
        self.writeVInt(15) #Roborumble LVL

        self.writeVInt(11)
        self.writeVInt(10000) #DuoWins

        self.writeVInt(12)
        self.writeVInt(15) #BossFight LVL

        self.writeVInt(15)
        self.writeVInt(12) #Most chalenges wins

        self.writeVInt(16)
        self.writeVInt(15) #CityFight LVL 

        self.writeVInt(17)
        self.writeVInt(19) #Highest Team League

        self.writeVInt(18)
        self.writeVInt(19) #Highest Solo League

        self.writeVInt(19)
        self.writeVInt(19) #Highest Club League


        self.writeString(playerData["Name"])
        self.writeVInt(0)
        self.writeVInt(playerData["Thumbnail"] + 28000000)
        self.writeVInt(43000000 + playerData["Namecolor"])
        self.writeVInt(0)

        self.writeBoolean(True)  # Is in club

        self.writeInt(0)
        self.writeInt(1) #Club ID
        self.writeString("<c3200ff>V<c6500ff>o<c9800ff>k<ccb00ff>e<cff00ff>s<cff00cc>B<cff0099>r<cff0066>a<cff0033>w<cff0001>l</c>")  # club name
        self.writeVInt(8)
        self.writeVInt(18)  # Club badgeID
        self.writeVInt(1)  # club type | 1 = Open, 2 = invite only, 3 = closed
        self.writeVInt(1)  # Current members count
        self.writeVInt(0) #Club Trophies
        self.writeVInt(0)  # Trophy required
        self.writeVInt(0)  # (Unknown)
        self.writeString("RU")  # region
        self.writeVInt(0)  # (Unknown)
        self.writeVInt(0) # (Unknown)
        self.writeVInt(25)
        self.writeVInt(2)
        

        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion