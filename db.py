import json

class MyDb:

    def insert(self,name,email,password):
        with open("users.json","r") as rf:
            database=json.load(rf)

            if email in database:
                return 0
            else:
                database[email]=[name,password]

        with open("users.json","w") as wf:
            json.dump(database,wf,indent=4)
            return 1
            
    def search(self,email,password):
        with open("users.json","r") as rf:
            database=json.load(rf)
            if email in database:
                if database[email][1]==password:
                    return 1
                else:
                    return 0
            else:
                return 0
