from django.core.validators import RegexValidator
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.core.validators import MaxValueValidator, MinValueValidator
from phone_field import PhoneField


import re


def validate_mobile_number(phone):
    pattern = r'^\+?91?[6789]\d{9}$'
    return re.match(pattern, phone)


# Create your models here.


# class Contact(models.Model):
#     name = models.CharField(max_length=50)
#     phone_regex = RegexValidator(
#         regex=r'^[789]\d{9}$',
#         message="Phone number must be in the format: '9999999999'."
#     )

#     phone = models.CharField(
#         validators=[phone_regex], max_length=10, unique=True)


class Student(models.Model):
    # Personal info
    student_image = models.ImageField(upload_to="pictures")
    qr_code = models.ImageField(upload_to='qr_code', blank=True)
    name = models.CharField(max_length=20)
    personal_email = models.EmailField()
    phone = models.CharField(
        max_length=13, validators=[validate_mobile_number])

    # phone = models.IntegerField()
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    current_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)

    # acadmeics info
    college_name = models.CharField(max_length=100)
    enrollment_year = models.IntegerField()
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, default="")
    roll_no = models.IntegerField()
    college_email = models.EmailField()
    # current_cgpa = models.DecimalField()
    current_cgpa = models.CharField(max_length=5
    )
    backlog = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        qr_name = "127.0.0.1:8000/student/"+str(self.roll_no)
        qrcode_img = qrcode.make(qr_name)
        canvas = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        file_name = f'qr_code-{self.roll_no}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
