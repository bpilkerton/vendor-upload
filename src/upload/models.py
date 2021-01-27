from django.db import models
from django.utils import dateparse
import csv

class Upload(models.Model):
    uploaded_file = models.FileField(upload_to ='vendor_uploads/')
    uploaded_date = models.DateTimeField('Date Uploaded', auto_now=True)
    #add an uploaded_user field

    #Override the save method
    def save(self, *args, **kwargs):
        super(Upload, self).save(*args, **kwargs)

        #File should be scrutinized further before reading
        with open(self.uploaded_file.path, 'r', newline = '') as file:
            columns = ['sub_id','first_name','last_name', \
                       'street','state','zip','status', \
                       'product_id','product_name','product_amount','tx_date']
            reader = csv.DictReader(file, fieldnames=columns, delimiter='\t')
            for row in reader:
                #Convert Zulu In to ISO-8601, this is naive and needs work
                zulu = row['tx_date']
                row['tx_date'] = dateparse.parse_datetime(zulu)
                row = VendorData.objects.create_row(row)

class RowManager(models.Manager):
    def create_row(self, row):
        r = self.create(**row)
        return r

#Normalize input model to User, Product, Transaction
class VendorData(models.Model):
    sub_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True)
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=100, null=True)
    product_amount = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tx_date = models.DateField(null=True,auto_now=False)
    objects = RowManager()

