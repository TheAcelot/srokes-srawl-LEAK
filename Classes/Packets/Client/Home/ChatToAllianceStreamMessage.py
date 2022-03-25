from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class ChatToAllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Message"] = self.readString()
        print(fields["Message"])
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        if fields["Message"] == "/фон зима":
            playerData["ThemeID"] = 36
            playerData["ClubMessage"] = "Фон обновлен на: Зима"
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
        elif fields["Message"] == "/фон любовь":
            playerData["ThemeID"] = 37
            playerData["ClubMessage"] = "Фон обновлен на: Любовь"
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
        elif fields["Message"] == "/фон тигр":
            playerData["ThemeID"] = 38
            playerData["ClubMessage"] = "Фон обновлен на: Тигр"
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
        elif fields["Message"] == "/обнулить":
            for i in range(54):
                playerData["OwnedBrawlers"][f"{i}"]["Trophies"] = 0
                playerData["OwnedBrawlers"][f"{i}"]["HighestTrophies"] = 0
            playerData["OwnedBrawlers"][f"54"]["Trophies"] = 0
            playerData["OwnedBrawlers"][f"54"]["HighestTrophies"] = 0
            playerData["Trophies"] = 0
            playerData["ClubMessage"] = "Все персонажи обнулены!"
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
        elif fields["Message"] == "/помощь":
            playerData["ClubMessage"] = "Команды, доступные для тебя:\n/фон зима - зимний фон\n/фон тигр - тигриный фон\n/фон любовь - розовый фон на 14 февраля\n/обнулить - обнулить трофеи на аккаунте\n/помощь - отобразить текущее сообщение."
        else:
            playerData["ClubMessage"] = fields["Message"]
        playerData["TickMessage"] = playerData["TickMessage"] + 1
        print(playerData["TickMessage"])
        db_instance.updatePlayerData(playerData, calling_instance)
        Messaging.sendMessage(24311, fields, calling_instance.player)

    def getMessageType(self):
        return 14315

    def getMessageVersion(self):
        return self.messageVersion