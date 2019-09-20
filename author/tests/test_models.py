from django.test import TestCase
from author.models import  Author
from django.test.client import  Client
from author import urls,views
from django.urls import path


class AuthorTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     kwargs = {'fname':'olatunde','lname':'ajadi'}
    #     Author.objects.create(**kwargs)

    def setUp(self):
        self.c = Client()
        kwargs = {'fname': 'olatunde', 'lname': 'ajadi'}
        Author.objects.create(**kwargs)


    def test_author_str(self):
        author = Author.objects.get(id=1)
        self.assertEquals(str(author),'olatunde,ajadi')

    def test_fname_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('fname').verbose_name
        self.assertEquals(field_label,'fname')

    def test_get_url(self):
        author = Author.objects.get(id=1)
        url = author.get_absolute_url()
        print ("-----",url)
        self.assertEquals(url,'/a/1')

    def test_url_response(self):
        response = self.c.get('/a/1')
        print (response.__dict__)
        self.assertEquals(response.status_code,200)



