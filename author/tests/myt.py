import os
import django
from django.conf import settings
from django.db import models
from django import forms
from Authorapi import settings as set

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", set)

settings.configure( DEBUG=True,
                    INSTALLED_APPS=set.INSTALLED_APPS,
                    DATABASES=set.DATABASES)
django.setup()
from author.models import Author

class mymodelform(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
af = Author.objects.get(pk=17)
print ("af----",af.__dict__)
newf = af.__dict__
newf['fname']='danny'
f = mymodelform(newf,instance=af)
a =f.save(commit=False)
a.fname ='adebisi--oll'
a.save()
print ("fields-----",f.fields)
af = Author.objects.get(pk=17)
print ("Dan----",af.__dict__)
print ("form ---",f)
data = {'subject': '','message': 'Hi there', 'sender': 'in the west', 'cc_myself': True}

class CommentForm(forms.Form):
    name = forms.CharField(initial='Class')
    url = forms.URLField()
    comment = forms.CharField()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['url'].initial = "http://yahoo.com"
        self.fields['comment'].initial = "Cool"

data = {'name':'','url':'music.com','comment':'very good'}

f = CommentForm(data)
print ("T  ---",f.errors)
for row in f.fields.keys(): print(row)
