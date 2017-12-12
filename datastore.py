import pickledb

db = pickledb.load('realmp7data.db', False)

# def passData(name, preferences, time, id):
#     namepreftime = [name, preferences, time]
#     db.set(id,namepreftime)


# def returnData(id):
#     return db.get(id)

def getUsers():
    try:
        return db.lgetall("users")
    except KeyError as e:
        db.lcreate("users")
        db.dump()
        return []

def addUser(id, topics):
    db.ladd("users",id)
    db.dcreate(id)
    db.dadd(id,("id",id))
    db.dadd(id,("topics",topics))
    db.dump()

def setTime(id, time):
    db.dadd(id, ("time", time))
    db.dump()

def getUsersByTime(time):
    users = getUsers()
    outputUsers = []
    for user in users:
        userData = returnData(user)
        if userData["time"] == time :
            outputUsers.append(userData)
    return outputUsers
