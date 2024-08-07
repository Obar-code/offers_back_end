from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import gettext as _
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from places.models import Directorate ,Status
from department.models import Department

# Create your models here.
################# choices ###############
class TypeAccount(models.IntegerChoices):
    customer = 1 , _('عميل')
    website = 2 , _('موقع للكتروني')
    market = 3, _('محل تجاري')

class Account(AbstractUser):
    type_account = models.IntegerField(_("نوع المستخدام"),choices=TypeAccount.choices, default=1)
    phone_number = PhoneNumberField(_("رقم الهاتف"),unique=True)
    email = models.EmailField(_("البريد الالكتروني"), max_length=254 ,unique=True)
    image = models.ImageField(_("صورة الملف الشخصي"), upload_to='images/accounts',blank= True , null=True)
   ##directorate = models.ForeignKey(Directorate, verbose_name=_("المدينة"), on_delete=models.CASCADE ,blank= True , null=True)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    def get_absolute_url(self):
        return reverse("Account_detail", kwargs={"pk": self.pk})


class Website(models.Model):
    image_ar = models.ImageField(_("صورة الموقع بالعربي"), upload_to='images/webite')
    image_en = models.ImageField(_("صورة الموقع بالانجليزي"), upload_to='images/webite',blank=True)
    name_ar = models.CharField(_("اسم الموقع الاكترني بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم الموقع الاكتروني بالانجلزي"), max_length=50 , blank=True)
    about_the_site_ar = models.TextField(_("نبذة عن الموقع الاكتروني بالعربي"))
    about_the_site_en = models.TextField(_("نبذة عن الموقع الاكتروني بالانجلزي"),blank=True)
    account = models.ForeignKey(Account, verbose_name=_("المستخدام المنشاء"), on_delete=models.CASCADE)
    departments = models.ManyToManyField(Department, verbose_name=_("مجلات الموقع الاكتروني"))
    email = models.EmailField(_("البريد الاكتروني"), max_length=254)
    link = models.URLField(_("رابط الموقع"), max_length=200)
    status = models.IntegerField(_("حالة الموقع"), choices=Status.choices ,default=2)
    #directorate = models.ForeignKey(Directorate, verbose_name=_("المدينة"), on_delete=models.CASCADE)
    facebook = models.URLField(_("رابط الفيسبوك"), max_length=200,blank=True)
    the_x = models.URLField(_("منصة اكس"), max_length=200,blank=True)
    instagram = models.URLField(_("انستقرام"), max_length=200,blank=True)
    tiktok = models.URLField(_("منصة تكتك"), max_length=200,blank=True)
    whatsapp = models.URLField(_("واتساب"), max_length=200,blank=True)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("الموقع الالكتروني ")
        verbose_name_plural = _("المواقع الالكتروني")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Website_detail", kwargs={"pk": self.pk})

class Market(models.Model):
    image_ar = models.ImageField(_("الصورة الموقع بالعربي"), upload_to='images/webite')
    image_en = models.ImageField(_("صورة الموقع بالانجلزي"), upload_to='images/webite' , blank=True)
    name_ar = models.CharField(_("اسم المحل التجاري بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم المحل التجاري بالانجزي"), max_length=50 ,blank=True)
    about_the_market_ar = models.TextField(_("نبذة عن المحل التجاري بالعربي"))
    about_the_market_en = models.TextField(_("نبذة المحل التجاري بالانجلزي"),blank=True)
    account = models.ForeignKey(Account, verbose_name=_("المستخدام المنشاء"), on_delete=models.CASCADE)
    departments = models.ManyToManyField(Department, verbose_name=_("مجلات المحل التجاري"))
    email = models.EmailField(_("البريد الاكتروني"), max_length=254,blank=True)
    link = models.URLField(_("رابط الموقع"), max_length=200,blank=True)
    status = models.IntegerField(_("حالة المحل التجاري"), choices=Status.choices ,default=2)
   # directorate = models.ForeignKey(Directorate, verbose_name=_("المدينة"), on_delete=models.CASCADE)
    facebook = models.URLField(_("رابط الفيسبوك"), max_length=200,blank=True)
    the_x = models.URLField(_("منصة اكس"), max_length=200,blank=True)
    instagram = models.URLField(_("انستقرام"), max_length=200,blank=True)
    tiktok = models.URLField(_("منصة تكتك"), max_length=200,blank=True)
    whatsapp = models.URLField(_("واتساب"), max_length=200,blank=True)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("محل تجاري")
        verbose_name_plural = _("محلات تجاريه")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Market_detail", kwargs={"pk": self.pk})

class GlobalWebsite(models.Model):

    name_ar = models.CharField(_("اسم الموقع بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم الموقع بالانجلزي"), max_length=50)
    status = models.IntegerField(_("حالة المحل التجاري"), choices=Status.choices ,default=2)
    link = models.URLField(_("رابط الموقع"), max_length=200)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("الموقع العالمي")
        verbose_name_plural = _("المواقع العالمية")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("GlobalW_detail", kwargs={"pk": self.pk})

