from django.http import request
from django.conf import  settings


class Ses(object):
    ses_all = None

    def __init__(self,request):
        self.session = request.session.get(settings.SESSION_ID)
        print ("ses--re-----",self.session)

        if not self.session:
            self.session = {}
        print ("Tundeses-------",self.session)


    def add_author(self,name):
        self.session[name] = (self.session.get(name) or 0) + 1
        print ("ses-------",self.session)

        ses_all  = self.session
        self.save()

    def reduce_author(self,name):
        if self.session.get(name):

            self.session[name] = (self.session.get(name)  - 1)
        else:
            raise Exception("Not availalbe")
        ses_all  = self.session
        self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        #	remove	cart	from	session
        del self.session[settings.SESSION_ID]
        self.save()



