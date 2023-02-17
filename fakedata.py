import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CrudFbv.settings')
import django
django.setup()
from faker import Faker
from random import *
from MyApp.models import *

fakerobj=Faker()

def populate(n):
    for i in range(n):
        feno=randint(100,150)
        fename=fakerobj.name()
        fesal=randint(25000,45000)
        feaddr=fakerobj.city()
        employee_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
        print(employee_record)
populate(6)