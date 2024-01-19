from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11)
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message = models.TextField()
    client_filter_operator_code = models.CharField(max_length=3)
    client_filter_tag = models.CharField(max_length=50)
