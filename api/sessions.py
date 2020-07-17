import pymongo
import json
import time
import hashlib
import base64
import json
import lz4.frame
import time
import calendar
import datetime

class Session:
    def __init__(self, mongoCli):
        self.dictionary = {}
        self.sessionDB = mongoCli["sessions"]["sessions"]
        self.initialized = False
        
        
    def create(self, identifier, expiration = calendar.timegm((datetime.datetime.utcnow() + datetime.timedelta(days=1)).timetuple())):
        
        self.identifier = hashlib.sha512(str(identifier).encode()).hexdigest()
        self.sessionDB.delete_many({"identifier": self.identifier})
        self.sessionDB.insert_one({"identifier":self.identifier,"content":base64.b64encode(lz4.frame.compress(json.dumps(self.dictionary).encode())),"expiration":expiration})
        self.initialized = True
    def load(self, identifier, expiration = calendar.timegm((datetime.datetime.utcnow() + datetime.timedelta(days=1)).timetuple())):
        self.identifier = hashlib.sha512(str(identifier).encode()).hexdigest()
        found = self.sessionDB.find({"identifier": self.identifier}).count() == 1
        if found:
            self.initialized = True
            self.pull()
        else:
            self.create(identifier,calendar.timegm((datetime.datetime.utcnow() + datetime.timedelta(days=1)).timetuple()))
    def pull(self):
        if not self.initialized:
            return None
        dct = self.sessionDB.find_one({"identifier": self.identifier})
        dictionary = json.loads(lz4.frame.decompress(base64.b64decode(dct["content"])))
        self.dictionary = dictionary
    def push(self):
        if not self.initialized:
            return None
        query = {"identifier": self.identifier}
        newData = {"identifier":self.identifier,"content":base64.b64encode(lz4.frame.compress(json.dumps(self.dictionary).encode()))}
        self.sessionDB.update(query, newData)
    def __getitem__(self, index):
        if not self.initialized:
            return None
        if index not in self.dictionary.keys():
            return self.__missing__(index)
        self.pull()
        return self.dictionary[index]
    def __setitem__(self, index, value):
        if not self.initialized:
            return None
        
        self.pull()
        self.dictionary[index] = value
        self.push()
    def __missing__(self, index):
        return None
    def __delitem__(self, index):
        if not self.initialized:
            return None
        self.pull()
        del self.dictionary[index]
        self.push()
    def get(self, *args):
        return self.dictionary.get(args)
    def __contains__(self, index):
        self.pull()
        return index in self.dictionary

    def keys(self):
        if not self.initialized:
            return None
        self.pull()
        return self.dictionary.keys()
    
    def items(self):
        if not self.initialized:
            return None
        self.pull()
        return self.dictionary.items()
    
    def pop(self, *args):
        self.pull()
        poped = self.dictionary.pop(args)
        self.push()
        return poped
    
    def popitem(self):
        self.pull()
        poped = self.dictionary.popitem()
        self.push()
        return poped
    def values(self):
        self.pull()
        return self.dictionary.values()
    def setdefault(self, *args):
        self.pull()
        seted = self.dictionary.setdefault(args)
        self.push()
        return seted
    def update(self, *args):
        self.pull()
        self.dictionary.update(args)
        self.push()
        return None
    def copy(self, *args):
        self.pull()
        return self.dictionary.copy(args)
    def asdict(self):
        self.pull()
        return self.dictionary.copy()
    def clear(self, *args):
        self.pull()
        cleared = self.dictionary.clear(*args)
        self.push()
        return cleared