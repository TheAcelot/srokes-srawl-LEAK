import json
from subprocess import call

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

class LogicSelectSkinCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        fields["SelectedSkin"] = calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        fields["SelectedBrawler"] = calling_instance.readVInt()
        print("Selected Brawler: {}".format(fields["SelectedBrawler"]))
        print("Selected Skin: {}".format(fields["SelectedSkin"]))
        #LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[4])
        print(calling_instance.player.ID)
        player_data["SelectedBrawler"] = fields["SelectedBrawler"]
        player_data["SelectedSkin"] = fields["SelectedSkin"]
        db_instance.updatePlayerData(player_data, calling_instance)
        print("Updated!")
        #Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})

    def getCommandType(self):
        return 506