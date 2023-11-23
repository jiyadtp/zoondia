from django.db import models

# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=100, null=True, db_index=True)
    lastname = models.CharField(max_length=100, null=True, db_index=True)
    email = models.CharField(max_length=100, null=True,db_index=True)
    password = models.CharField(max_length=100, null=True, db_index=True)


class UrlDetails(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="user_url_id",null=True)
    url = models.CharField(max_length=150, null=True)
    visited_count = models.CharField(max_length=10, null=True)
    qr_value = models.TextField(null=True)
