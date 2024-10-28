# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Alt text](<Screenshot 2024-10-24 185923-2.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)
```


## OUTPUT

![Alt text](<Screenshot (3).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
