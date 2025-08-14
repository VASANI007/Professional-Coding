from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    code_file = models.FileField(upload_to='code_files/')
    output_video = models.FileField(upload_to='videos/', blank=True, null=True)
    output_image = models.ImageField(upload_to='images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class cars(models.Model):
    vehicle_image = models.ImageField(upload_to='Cars/', null=True, blank=True)
    v_name = models.TextField()

    Seats = [
        ("0", "4"),
        ("1", "5"),
        ("2", "7")
    ]
    seats = models.CharField(max_length=10, choices=Seats, default="1")  # Default to "5 seats"

    V_Type = [
        ("SUVs", "SUVs"),
        ("Sedans", "Sedans"),
        ("Crossovers", "Crossovers"),
        ("Coupes", "Coupes"),
        ("Hatchbacks", "Hatchbacks"),
    ]
    vehicle_type = models.CharField(max_length=50, choices=V_Type, default="1")  # Default to "Sedans"
    stock_no = models.TextField(unique=True)
    doors = models.IntegerField()
    year = models.IntegerField()
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    VIN = models.TextField(unique=True)
    price = models.FloatField(default=0.0)
    description = models.TextField(null=True)
    make = models.CharField(max_length=50, null=True)

    V_status = [
        ("0", "Unavailable"),
        ("1", "Available")
    ]
    status = models.CharField(max_length=10, choices=V_status, default="1")  # Default to "Available"

    def __str__(self):
        return self.v_name
    
    def vehicle_pic(self):
        return mark_safe(f'<img src="{self.vehicle_image.url}" width="100">')

class contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True)
    msg=models.TextField(null=True)
    
class category(models.Model):
    cat_name = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.cat_name

class ourgallery(models.Model):
    c_name = models.CharField(max_length=255,null=False)
    c_img = models.ImageField(upload_to='gallery/', null=True, blank=True)
    c_id = models.ForeignKey(category, on_delete=models.CASCADE)
    c_fullcode = models.TextField()
    c_createddate = models.DateField(auto_now_add=True)
    c_type = models.CharField(max_length=255,null=False)
    c_required = models.TextField()
    c_des = models.TextField()
    
    def __str__(self):
        return self.c_name
    
    def c_pic(self):
        if self.c_img and hasattr(self.c_img, 'url'):
            return mark_safe(f'<img src="{self.c_img.url}" width="100">')
        return mark_safe('<img src="/static/media/not.gif" width="100">')