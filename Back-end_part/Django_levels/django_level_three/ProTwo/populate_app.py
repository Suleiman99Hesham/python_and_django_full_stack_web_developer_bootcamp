import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from sec_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    
    for entry in range(N):
        full_name=fakegen.name().split()
        f_name = full_name[0]
        l_name = full_name[1]
        email = fakegen.email()
        user = User.objects.get_or_create(fisrt_name = f_name, last_name = l_name, email = email)

if __name__ == "__main__":
    print('Populating Script....')
    populate(20)
    print('Populating Complete!')