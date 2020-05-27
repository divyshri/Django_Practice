import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def populate(N=5):
    for entry in range(N):
        #Create Fake databases
        fake_first_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
    print("Populating Scripts")
    populate(50)
    print("Populating Complete")
