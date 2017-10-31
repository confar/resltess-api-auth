# posts/api.py
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm

from restless.dj import DjangoResource
from restless import exceptions

from .models import ApiUser


class ApiUserForm(ModelForm):
    class Meta(object):
        model = ApiUser
        fields = ['email', 'password', 'type']


class ApiUserLoginResource(DjangoResource):

    #POST/account/login/
    def create_detail(self, *args, **kwargs):
        try:
            user = authenticate(self.request, email=self.data.get('email'), password=self.data.get('password'))
            if user:
                login(self.request, user)
                print("User is logged in")
            else:
                raise exceptions.Unauthorized(msg='wrong password or username')
        except exceptions.NotFound:
            return None


    def is_authenticated(self):
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True
        # Alternatively, if the user is logged into the site...
        # return self.request.user.is_authenticated()

        #POST/account/logout/
class ApiUserLogoutResource(DjangoResource):

    def create_detail(self, *args, **kwargs):
        logout(self.request)
        print("User has logged out")

    def is_authenticated(self):
        if self.request.user.is_authenticated():
            return True
        else:
            raise exceptions.Unauthorized(msg='User is not Authorised')

        #POST/account/register/
class ApiUserRegisterResource(DjangoResource):

    def create_detail(self, *args, **kwargs):
        form = ApiUserForm(self.data)

        if not form.is_valid():
            raise exceptions.BadRequest('Something is wrong.')

        user = ApiUser.objects.create_user(
        email=form.cleaned_data['email'],
        password=form.cleaned_data['password'],
        type=form.cleaned_data['type'],
        )
        print("User has registered")




    def is_authenticated(self):
        return True
