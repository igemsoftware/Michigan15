from protocat_app.models import *
from django.test import TestCase
from django.test import Client
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserAuthenticationForm, ProtocolUploadForm
from webtest import TestApp
from datetime import datetime

class UserRegistrationTest(TestCase):
    """
    Checks that input is return correctly from database
    """
    def test_input_signup(self):
        username = "johnd"
        email = "123@gmail.com"
        first = "John"
        last = "Doe"
        password = "123"
        new_user = UserRegistration(email=email, user_name=username, first_name=first, last_name=last, password=password)
        self.assertEqual(new_user.details(), "johnd, 123@gmail.com")

class UserAuthenticationTest(TestCase):
    """
    Checks that input is return correctly from database
    """
    def test_input_login(self):
        username = "johnd"
        password = "123"
        new_login = UserAuthentication(user_name=username, password=password)
        self.assertEqual(new_login.details(), "johnd, 123")

class ProtocolMethodTests(TestCase):
    """
    Checks that input is return correctly from database
    """
    def test_input_uploadb(self):
        author = "John Doe"
        title = "Photosynthesis of Plants"
        description = "This is how a plant eats"
        protocol = Protocol(author=author, title=title, description=description)
        self.assertEqual(protocol.details(), "John Doe, Photosynthesis of Plants, This is how a plant eats")

class NotLoggedInTests(TestCase):
    def test_not_logged_in(self):
        c = Client()
        ''' creating a user'''
        user = User.objects.create_user(username="johnd", password="123")
        user.save()
        ''' creating a protocol'''
        protocol = Protocol.objects.create(author="johnd", id=1)
        protocol.save()
        """
        Someone not logged should be able to access
        these pages
        """
        response = c.get('/protocol_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_authentication/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_registration/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/rating_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/date_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/author_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/title_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/modified_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/about/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/feedback/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/protocol_display/1/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_profile/johnd/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/search/?search=something')
        self.assertEqual(response.status_code, 200)
        """
        Someone not logged in should NOT be able to access these pages
        """
        response = c.get('/user_home/')
        self.assertEqual(response.status_code, 404)
        response = c.get('/protocol_upload/')
        self.assertEqual(response.status_code, 302)
        response = c.get('/user_home/')
        self.assertEqual(response.status_code, 404)
        response = c.get('/delete_protocol/1/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/pre_edit/1/')
        self.assertEqual(response.status_code, 200)

class LoggedInTests(TestCase):
    def test_logged_in(self):
        c = Client()
        ''' creating a user'''
        user = User.objects.create_user(username="johnd", password="123")
        user.save()

        user2 = User.objects.create_user(username="janed", password="123")
        user2.save()
        c.login(username='johnd', password="123")
        ''' creating a protocol'''

        protocol = Protocol.objects.create(author="johnd", id=1)
        protocol.save()

        protocol2 = Protocol(author="janed", id="2")
        protocol2.save()

        response = c.get('/protocol_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_authentication/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_registration/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/rating_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/date_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/author_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/title_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/modified_list/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/about/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/feedback/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/protocol_display/1/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_profile/johnd/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/search/?search=something')
        self.assertEqual(response.status_code, 200)
        response = c.get('/user_home/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/protocol_upload/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/delete_protocol/1/')
        self.assertEqual(response.status_code, 302)

class Forms(TestCase):
    def test_signup(self):
        form = UserRegistrationForm({
            'user_name' : "name",
            'first_name' : "John",
            'last_name' : "Doe",
            'email' : "johnd@gmail.com",
            'password' : "123"
        })
        self.assertTrue(form.is_valid())
        response = self.client.post('/user_registration/', {
            'user_name' : "name",
            'first_name' : "John",
            'last_name' : "Doe",
            'email' : "johnd@gmail.com",
            'password' : "123"
        })
        self.assertTrue(response.status_code, 302)

        user = User.objects.create_user(username="johnd", password="123")
        user.save()

        response = self.client.post('/user_registration/', {
            'user_name' : "johnd",
            'first_name' : "John",
            'last_name' : "Doe",
            'email' : "johnd@gmail.com",
            'password' : "123"
        })
        self.assertTrue(response.status_code, 200)

    def test_login(self):
        c = Client()
        response = self.client.post('/user_authentication/', {
            'user_name' : "johnd",
            'password' : "123"
        })
        self.assertEqual(response.status_code, 200)

        user = User.objects.create_user(username="johnd", password="123")
        user.save()

        form = UserAuthenticationForm({
            'user_name' : "johnd",
            'password' : "123"
        })
        self.assertTrue(form.is_valid())
        response = self.client.post('/user_authentication/', {
            'user_name' : "johnd",
            'password' : "123"
        })
        self.assertEqual(response.status_code, 302)
        c.login(username="johnd", password="123")



    def test_upload(self):
        form = ProtocolUploadForm({
            'title': "Protocol",
            'description': "This is a protocol",
            'protocol_type': "BC",
            'reagents': "Chemicals",
            'protocol_steps': "Do stuff"
        })
        self.assertTrue(form.is_valid())
        form.save()
        response = self.client.post('/protocol_upload/', {
            'title': "Protocol",
            'description': "This is a protocol",
            'protocol_type': "BC",
            'reagents': "Chemicals",
            'protocol_steps': "Do stuff"
        })
        self.assertEqual(response.status_code, 302)

    def test_edit(self):
        c = Client()
        user = User.objects.create_user(username="johnd", password="123")
        user.save()
        c.login(username="johnd", password='123')
        protocol = Protocol.objects.create(author="johnd", id=1, title='title', reagents='reagents',
                                        date_of_upload=datetime.now(), date_modified=datetime.now(),
                                        description='description', protocol_type='BC', rating=0.00,
                                        num_ratings=0, user_rated='ds', protocol_steps="stuff")
        protocol.save()

        response = self.client.post('/pre_edit/1/', {
            'title': "Protocol",
            'description': "This is a protocol",
            'protocol_type': "BC",
            'reagents': "Chemicals",
            'protocol_steps': "Do stuff"
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/edit_protocol/1/', {
            'title': "Protocol",
            'description': "This is a protocol",
            'protocol_type': "BC",
            'reagents': "Chemicals",
            'protocol_steps': "Do stuff"
        })
        self.assertEqual(response.status_code, 200)












