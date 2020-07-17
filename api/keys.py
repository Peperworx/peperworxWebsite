import json
import hashlib
import time
import os

def validateKey(mongoCLI, key, secret):
    keyDB = mongoCLI["keys"]["keys"]
    pKey = keyDB.find_one({"key": key})
    if pKey != None:
        pKey["_id"] = str(pKey["_id"])
        if pKey["secret"] == secret:
            pKey["secret"] == "censored"
            return {"status":"ok","message":"OK","key":pKey}
        else:
            return {"status":"error","message":"IC"}
    else:
        return {"status":"error","message":"NE"}
    

