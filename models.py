from google.appengine.ext import ndb

class Account(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.IntegerProperty()
    
