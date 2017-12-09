from tinydb import TinyDB, Query

db = TinyDB('mp7data.json')

def passData(id, name, preferences, time):
    namepreftime = [name, preferences, time]
    db.insert({id:namepreftime})

def returnData(id):
    ID = Query()
    return db.search(ID.type == id)
