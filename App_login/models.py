from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
        "Enter a valid international mobile phone number starting with +(country code)"))


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    Name = models.CharField(max_length=50, blank=False, null=True)
    class_id = models.CharField(max_length=30, blank=False, null=True)
    batch = models.CharField(max_length=30, blank=False, null=True)
    Department = models.CharField(max_length=30, blank=False, null=True)
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True,
                                    null=True)
    Section = models.CharField(max_length=30, blank=False, null=True)
    Date_of_Birth = models.DateField(verbose_name=_("Date of birth"), blank=True, null=True)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    Name = models.CharField(max_length=50, blank=False, null=True)
    teacher_id = models.CharField(max_length=30, blank=False, null=True)
    Designation = models.CharField(max_length=50, blank=False, null=True)
    Department = models.CharField(max_length=30, blank=False, null=True)
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True,
                                    null=True)
    Qualification = models.CharField(max_length=30, blank=False, null=True)
    Facebook = models.CharField(max_length=30, blank=False, null=True)
    WhatsApp = models.CharField(max_length=30, blank=False, null=True)
