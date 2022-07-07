import datetime
from decimal import *

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.utils.translation import gettext_lazy as _
from management.utils import unique_slug_generator
from django_countries.fields import CountryField
from management.models import Department


# Create your models here.
class CustomerUser(AbstractUser):
    class Category(models.IntegerChoices):
        Applicant_or_Job_Applicant = 1
        Coda_Staff_Member = 2
        Client_OR_Customer_or_Student = 3

    # added this column here
    class SubCategory(models.IntegerChoices):
        No_selection = 0
        Job_Support = 1
        Student = 2
        Full_time = 3
        Contractual = 4
        Agent = 5
        Other = 6

    class Score(models.IntegerChoices):
        Male = 1
        Female = 2

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=100)
    gender = models.IntegerField(choices=Score.choices, blank=True, null=True)
    phone = models.CharField(default="90001", max_length=100)
    address = models.CharField(blank=True, null=True, max_length=100)
    city = models.CharField(blank=True, null=True, max_length=100)
    state = models.CharField(blank=True, null=True, max_length=100)
    country = CountryField(blank=True, null=True)
    category = models.IntegerField(choices=Category.choices, default=999)
    # added this column here
    sub_category = models.IntegerField(
        choices=SubCategory.choices, blank=True, null=True
    )
    # category=models.IntegerField(choices=Category.choices,blank=True,null=False)
    # applicant=models.BooleanField('Is Job Applicant', default=True)
    # Changes Made to Model-3/29/2022
    is_admin = models.BooleanField("Is admin", default=False)
    is_employee = models.BooleanField("Is employee", default=False)
    is_client = models.BooleanField("Is Client", default=False)
    is_applicant = models.BooleanField("Is applicant", default=False)
    resume_file = models.FileField(upload_to="resumes/doc/", blank=True, null=True)

    # is_active = models.BooleanField('Is applicant', default=True)
    class Meta:
        ordering = ["-date_joined"]

# =========================CREDENTIALS TABLE======================================
class CredentialCategory(models.Model):
    department = models.ForeignKey(Department,on_delete=models.RESTRICT,default="Other")
    # created_by= models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        verbose_name=_('Category Name'),
        help_text=_('Required'),
        max_length=255, 
        unique=True,
    )
    slug = models.SlugField(verbose_name=_('category safe URL'), max_length=255, unique=True)
    description = models.TextField(max_length=1000, default=None)
    entry_date = models.DateTimeField(_('entered on'),auto_now_add=True, editable=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('management:credentialcategorylist', args=[self.slug])
    class Meta:
        verbose_name=_('Category')
        verbose_name_plural=_('Categories')

    def __str__(self):
        return f"{self.category} Categories"

class Credential(models.Model):
    category = models.ManyToManyField(CredentialCategory, blank=True,related_name='credentialcategory')
    added_by= models.ForeignKey(CustomerUser, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_('credential Name'),
        help_text=_('Required'),
        max_length=255, 
    )
    slug = models.SlugField(verbose_name=_('credential safe URL'), max_length=255, unique=True)
    description = models.TextField(max_length=1000, default=None)
    link_name=models.CharField(max_length=255, default='General')
    link=models.CharField(max_length=100,blank=True, null=True)
    password=models.CharField(max_length=255,blank=True, null=True, default='No Password Needed')
    entry_date = models.DateTimeField(_('entered on'),auto_now_add=True, editable=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "credentials"

    def get_absolute_url(self):
        return reverse("management:credential")

    def __str__(self):
        return self.name

# ========================================SLUGS GENERATOR====================================================
def credentialcategory_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(credentialcategory_pre_save_receiver, sender=CredentialCategory)

# ========================================TIME TRACKER====================================================
# Time Tracking Model
class Tracker(models.Model):
    class Duration(models.IntegerChoices):
        One_Hour = 1
        Two_Hours = 2
        Three_Hours = 3
        Four_Hours = 4
        Five_Hours = 5
        Eight_Hours = 8
        Ten_Hours = 10

    # class AssignedTime(models.IntegerChoices):
    # Plan_A =30
    # Plan_B =120
    # Other = 999

    # Job Category.
    Job_Support = "Job_Support"
    Interview = "Interview"
    Training = "Training"
    Mentorship = "Mentorship"
    Other = "Other"
    # Task/Activities
    Reporting = "reporting"
    Database = "database"
    Business_Analysis = "Business Analysis"
    ETL = "Data Cleaning"
    Other = "Any Other"

    CAT_CHOICES = [
        (Job_Support, "Job_Support"),
        (Interview, "Interview"),
        (Training, "Training"),
        (Mentorship, "Mentorship"),
        (Other, "Other"),
    ]
    TASK_CHOICES = [
        (Reporting, "reporting"),
        (Database, "database"),
        (Business_Analysis, "Business Analysis"),
        (ETL, "Data Cleaning"),
        (Other, "Other"),
    ]
    category = models.CharField(
        max_length=25,
        choices=CAT_CHOICES,
    )
    task = models.CharField(
        max_length=25,
        choices=TASK_CHOICES,
    )
    plan = models.CharField(
        verbose_name=_("group"), help_text=_("Required"), max_length=255, default="B"
    )
    employee = models.CharField(
        verbose_name=_("Employee Name"),
        help_text=_("Required"),
        max_length=255,
        default="CODA",
    )
    author = models.ForeignKey(
        "accounts.CustomerUser",
        verbose_name=_("Client Name"),
        on_delete=models.CASCADE,
        related_name="author",
        limit_choices_to={"is_client": True, "is_active": True},
    )
    # clientname = models.ForeignKey('accounts.CustomerUser', on_delete=models.CASCADE, related_name="clientname",limit_choices_to={'is_client': True})
    login_date = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    duration = models.IntegerField(choices=Duration.choices, default=2)
    time = models.PositiveIntegerField(
        # max_digits=3,
        help_text=_("Maximum 200"),
        error_messages={
            "name": {" max_length": ("The maximum hours must be between 0 and 199")}
        },
        default=120,
    )

    class Meta:
        ordering = ["login_date"]

    def get_absolute_url(self):
        return reverse("usertime", args=[self.username])

    @property
    def end(self):
        # date_time = datetime.datetime.now() + datetime.timedelta(hours=2)
        date_time = self.login_date + datetime.timedelta(hours=0)
        endtime = date_time.strftime("%H:%M")
        return endtime

    @property
    def total_payment(self):
        total = self.duration.objects.aggregate(TOTAL=Sum("duration"))["TOTAL"]
        return total

    """ 
    @property
    def amt_per_plan(self):
        if self.plan=='A':
            return 30
        elif self.plan=='B':
            return 120
        else:
            return 9999
    """
