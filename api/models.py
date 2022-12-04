from django.db import models


# Create your models here.


class UdyamForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobile = models.CharField(max_length=12)
    aadhaar = models.CharField(max_length=15)
    social_category = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    specially_abled = models.CharField(max_length=10)
    have_gstn = models.CharField(max_length=10)
    enterprise_name = models.CharField(max_length=150)
    pan = models.CharField(max_length=12)
    organization_type_id = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=25)
    ifsc_code = models.CharField(max_length=25)
    business_activity = models.CharField(max_length=50)
    business_nature = models.CharField(max_length=80)
    male_employees = models.IntegerField()
    female_employees = models.IntegerField()
    start_date = models.DateField()
    flat_no = models.CharField(max_length=30)
    name_of_building = models.CharField(max_length=150)
    village_town = models.CharField(max_length=50)
    block = models.CharField(max_length=150)
    road_street = models.CharField(max_length=150)
    pincode = models.CharField(max_length=15)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    district = models.CharField(max_length=70)
    status = models.IntegerField(default=0, help_text='0-pending, 1-active, 2-completed')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_created=True,auto_now_add=True)
