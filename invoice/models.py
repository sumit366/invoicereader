from django.db import models


class Invoice(models.Model):
    class Meta:
        db_table = 'invoice'

    product = models.CharField(max_length=200, default=None)
    customer_type = models.CharField(max_length=500, default=None)
    date = models.DateField(auto_now=True)
    actual = models.FloatField()
    expected = models.FloatField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    region = models.CharField(max_length=100)
