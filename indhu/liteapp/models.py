from django.db import models
from django.contrib import admin
class BankLoan (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    income=models.IntegerField()
    dob=models.CharField(max_length=8)
    account_num=models.CharField(max_length=11,primary_key=True)


class BankLoanAdmin(admin.ModelAdmin):
   list_display=("name","age","income","dob","account_num")


