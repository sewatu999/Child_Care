from django.apps import apps as django_apps
from django.apps import AppConfig
from django.apps import AccountsConfig


class ChildCareConfig(AppConfig):
    name = 'child_care'
   

class AccountsConfig(AccountsConfig):
    name = 'accounts',
    verbose_name = 'Accounts' 
