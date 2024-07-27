from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.urls import reverse
from datetime import datetime ,timezone

# Create your models here.
####################ValidationError##############
def check_date_time(value):
    now = datetime.now(timezone.utc)
    if value <= now:
        raise ValidationError (_('ضروري التاريخ يكون اكبر من الوقت الحالي'))

#################### choices ####################
class Status(models.IntegerChoices):
    PENDING = 1 ,_('قيد الانشاء')
    ACTIVE = 2 ,_('تم الانشاء')
    DEACTIVATE = 3 ,_('تم التوقيف')

class TypeAdvertising(models.IntegerChoices):
    main  = 1 , _('الرئيسي')
    sub = 2 , _('الفرعي')


#################### Models #####################
class Country(models.Model):
    name_ar = models.CharField(_("اسم البلاد بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم البلاد بالانجلزي"), max_length=50,blank=True , null=True)
    status = models.IntegerField(_("الحالة"),choices=Status.choices ,default=2)
    create_at = models.DateTimeField(_("تاريخ الانشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)

    class Meta:
        verbose_name = _("البلاد")
        verbose_name_plural = _("البلدان")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})


class Provinec(models.Model):
    name_ar = models.CharField(_("اسم الماحفظة بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم المحافظة بالانجلزي"), max_length=50,blank=True , null=True)
    country = models.ForeignKey(Country, verbose_name=_("البلاد"), on_delete=models.CASCADE)
    status = models.IntegerField(_("الحالة"),choices=Status.choices ,default=2)
    create_at = models.DateTimeField(_("تاريخ الانشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("المحافظة")
        verbose_name_plural = _("المحافظات")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Provinec_detail", kwargs={"pk": self.pk})


class Directorate(models.Model):
    name_ar = models.CharField(_("اسم المديرية بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم المديرية بالانجلزي"), max_length=50,blank=True , null=True)
    provinec = models.ForeignKey(Provinec, verbose_name=_("المحافظة"), on_delete=models.CASCADE)
    status = models.IntegerField(_("الحالة"),choices=Status.choices ,default=2)
    create_at = models.DateTimeField(_("تاريخ الانشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True) 
    class Meta:
        verbose_name = _("المديرية")
        verbose_name_plural = _("المدريات")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Tropical_detail", kwargs={"pk": self.pk})

class AreWe(models.Model):
    goal_ar = models.TextField(_("الهدف بالعربي"))
    goal_en = models.TextField(_("الهدف بالانجلزي"),blank=True , null=True)
    image_goal = models.ImageField(_("صورة الهدف"), upload_to="images/arewe")
    message_ar = models.TextField(_("الرسالة بالعربي"))
    message_en = models.TextField(_("الرسالة بالانجلزي"),blank=True, null=True)
    image_message = models.ImageField(_("صورة الرسالة"), upload_to="images/arewe")
    idea_ar = models.TextField(_("الفكرة بالعربي"))
    idea_en = models.TextField(_("الفكرة بالانجلزي"),blank=True,null=True)
    image_idea = models.ImageField(_("صورة الفكرة"), upload_to="images/arewe")
    vision_ar = models.TextField(_("الرؤية بالعربي"))
    vision_en = models.TextField(_("الرؤية بالانجلزي"),blank=True,null=True)
    image_vision = models.ImageField(_("صورة الرؤية"), upload_to="images/arewe")
    status = models.IntegerField(_("الحالة"),choices=Status.choices ,default=2)
    create_at = models.DateTimeField(_("تاريخ الانشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("من نحن")
        verbose_name_plural = _("من نحن")

    def __str__(self):
        return self.goal_ar

    def get_absolute_url(self):
        return reverse("AreWe_detail", kwargs={"pk": self.pk})


class Advertising(models.Model):

    name_ar = models.CharField(_("اسم المعلان بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم المعلان بالانجلزي"), max_length=50,blank=True , null=True)
    end_time = models.DateTimeField(_("نهائية العرض"),validators=[check_date_time])
    image = models.ImageField(_("صورة الاعلان"), upload_to="images/advertising")
    type_advertising = models.IntegerField(_("نوع الاعلان"),choices=TypeAdvertising.choices , default=1 )
    urls_ar = models.URLField(_("الرابط الذي يكون داخل الصورة بالغة العربية"), max_length=200 ,blank=True , null=True)
    urls_en = models.URLField(_("الرابط الذي داخل الصورة بالغة الانجلزية"), max_length=200 ,blank=True , null=True)
    status = models.IntegerField(_("الحالة"),choices=Status.choices ,default=2)
    create_at = models.DateTimeField(_("تاريخ الانشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("الاعلان")
        verbose_name_plural = _("الاعلانات")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Advertising_detail", kwargs={"pk": self.pk})

