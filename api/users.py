import json
import hashlib
import time
import api.sessions as sessions
import os




def authenticateUser(mongoCli, username,password):
    users = mongoCli["users"]["users"]
    
    user = users.find_one({"username": username})
    if user != None:
        if user["password"] == hashlib.sha256(password.encode()).hexdigest():
            return {"status": "ok", "message":"OK","user": user}
        else:
            return {"status": "error", "message":"IC"}
    else:
        return {"status": "error", "message":"NE"}


def getUser(mongoCli, username):
    users = mongoCli["users"]["users"]
    
    user = users.find_one({"username": username})
    
    if user != None:
        return {"status": "ok", "message": "OK", "user": user}
    else:
        return {"status": "error", "message": "NE"}

def validateLogin(mongoCli, username, sessionkey):
    session = sessions.Session(mongoCli,sessionkey, username)
    newsession = hashlib.sha224(os.urandom(1024)).hexdigest()
    if session.inDB:
        if session.session == sessionkey:
            session.session = newsession
            session.updateDB()
            return {"status": "ok", "message": "OK", "key": newsession}
        else:
            session.removeFromDB()
            return {"status":"error","message":"IC"}
    else:
        return {"status": "error", "message":"NE"}