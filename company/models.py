from django.db import models
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


STATUS = (("call denied","call denied"),
           ("interested","interested"),
           ("not interested","not interested"),
           ("wrong number","wrong number"),
           ("follow up","follow up"),
           ("dead","dead")
           )
Company = (("company","company"),
            ("end customer","end customer")
            )

class company_details(models.Model):
    Company_Name  = models.CharField(max_length=100)
    Contact_person_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Contact_1 = models.CharField(max_length=100)
    Contact_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.Company_Name

class contact(models.Model):
    company_type = models.CharField(max_length=20,choices=Company,default='company')
    company_ID = models.ForeignKey(company_details, on_delete=models.CASCADE)
    status = models.CharField(
        max_length = 50,
        choices =STATUS,
        default = 'call denied')
    next_follow_up_date = models.DateField()
    remark = models.CharField(max_length=1000)
    last_call_date = models.DateField()

    def __str__(self):
        return self.company_type


