from django.contrib import admin
from .models import Upload,VendorData

class UploadAdmin(admin.ModelAdmin):
    list_display = ('id','uploaded_file','uploaded_date')

class VendordataAdmin(admin.ModelAdmin):
    list_display = ('id','sub_id','first_name','last_name','status')

admin.site.site_header = "Subscription Fulfillment Upload"
admin.site.register(Upload, UploadAdmin)
admin.site.register(VendorData, VendordataAdmin)
