from django.test import TestCase
from author.models import  Author
from django.urls import reverse
from django.test.client import  Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class AuthorTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     kwargs = {'fname':'olatunde','lname':'ajadi'}
    #     Author.objects.create(**kwargs)

    def setUp(self):
        self.c = APIClient()
        kwargs = {'fname': 'olatunde', 'lname': 'ajadi'}
        Author.objects.create(**kwargs)
        self.user = User(username='olatunde')
        self.user.set_password("dannynoc")
        self.user.first_name = 'olatunde'
        self.user.last_name = 'ajadi'
        self.user.save()


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
        response = self.c.post('/a/1')
        self.assertEquals(response.status_code,200)

    def test_user(self):
        me = User.objects.get(id=1)
        # print (str(me.query))
        self.assertEquals(me.username,'olatunde')

    #     Get token
    def test_user_request(self):
        response = self.c.login(username='olatunde',password='dannynoc')
        print ("dict--------",response)
        self.assertTrue(response,"Cant login ,failed ")
    def test_token(self):
        token,_ = Token.objects.get_or_create(user_id=1)
        print ("TOken -----",token)
        usertoken = self.c.post(reverse('author:login_view'),data={'username':'olatunde','password':'dannynoc'})
        # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.assertEquals(token.key,usertoken.content)

    def test_login_view(self):
        response = self.c.post('/a/login',data={'username':'olatunde','password':'dannynoc'})
        print ("login-view------",response.content)
        self.assertEquals(response.status_code,240)


    def test_auth_user(self):
        user = authenticate(username='olatunde',password='dannynoc')
        self.assertFalse(None,user)





