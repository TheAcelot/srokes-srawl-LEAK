import json
import sqlite3
import traceback


class DatabaseHandler():
    def __init__(self):
        self.conn = sqlite3.connect("Database/Files/player.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (ID int, Token text, Nick text, Trophies int, Data json)""")
        except sqlite3.OperationalError:
            pass
        except Exception:
            print(traceback.format_exc())

    def createAccount(self, data):
        try:
            self.cursor.execute("INSERT INTO main (ID, Token, Nick, Trophies, Data) VALUES (?, ?, ?, ?, ?)", (data["ID"][1], data["Token"], data["Name"], data["Trophies"], json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())

    def getAll(self, num):
        self.playersId = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                self.playersId.append(self.db[i][num])
            return self.playersId
        except Exception:
            print(traceback.format_exc())

    def load_all(self):
        self.ids = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in self.db:
                data_db = json.loads(i[4])
                self.ids.append(data_db)
            return self.ids
        except Exception:
            print(traceback.format_exc())

    def getPlayer(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return json.loads(self.cursor.fetchall()[0][4])
        except Exception:
            print(traceback.format_exc())

    def getPlayerName(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return json.loads(self.cursor.fetchall()[0][2])
        except Exception:
            print(traceback.format_exc())

    def getPlayerEntry(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return self.cursor.fetchall()[0]
        except IndexError:
            pass
        except Exception:
            print(traceback.format_exc())

    def loadAccount(self, player, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            playerData = json.loads(self.cursor.fetchall()[0][4])
            player.ID = playerData["ID"]
            player.Name = playerData["Name"]
            player.Registered = playerData["Registered"]
            player.Thumbnail = playerData["Thumbnail"]
            player.Namecolor = playerData["Namecolor"]
            player.Region = playerData["Region"]
            player.ContentCreator = playerData["ContentCreator"]
            player.Coins = playerData["Coins"]
            player.Gems = playerData["Gems"]
            player.StarPoints = playerData["StarPoints"]
            player.Trophies = playerData["Trophies"]
            player.HighestTrophies = playerData["HighestTrophies"]
            player.TrophyRoadTier = playerData["TrophyRoadTier"]
            player.Experience = playerData["Experience"]
            player.Level = playerData["Level"]
            player.Tokens = playerData["Tokens"]
            player.TokensDoubler = playerData["TokensDoubler"]
            player.SelectedBrawler = playerData["SelectedBrawler"]
            player.SelectedSkin = playerData["SelectedSkin"]
            player.OwnedPins = playerData["OwnedPins"]
            player.OwnedThumbnails = playerData["OwnedThumbnails"]
            player.OwnedBrawlers = playerData["OwnedBrawlers"]
        except Exception:
            print(traceback.format_exc())

    def updatePlayerData(self, data, calling_instance):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE ID=?", (json.dumps(data, ensure_ascii=0), calling_instance.player.ID[1]))
            self.conn.commit()
            self.loadAccount(calling_instance.player, calling_instance.player.ID)
        except Exception:
            print(traceback.format_exc())

    def playerExist(self, loginToken, loginID):
        try:
            if loginID[1] in self.getAll(0):
                if loginToken != self.getPlayerEntry(loginID)[1]:
                    return False
                return True
            return False
        except Exception:
            print(traceback.format_exc())
