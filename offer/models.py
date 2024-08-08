from django.db import models
from django.utils.translation import gettext as _ 
from accounts.models import Website , Market , GlobalWebsite
from department.models import Department
from django.urls import reverse
from places.models import Status
from django.utils import timezone

# Create your models here.

class CurrencyType(models.Model):

    name_ar = models.CharField(_("اسم العملة بالعربي "), max_length=50)
    name_en = models.CharField(_("اسم العملة بالانجلزي"), max_length=50 ,blank=True , null=True)
    cut_ar = models.CharField(_("اختصار العملة بالعربي"), max_length=50)
    status = models.ImageField(_("حالة العرض"),choices=Status.choices ,default=2)
    cut_en = models.CharField(_("اختصار العملة بالانجلزي"), max_length=50 ,blank=True , null=True)
    icon = models.ImageField(_("رمز العملة"), upload_to='image/currency',)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),default=timezone.now)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), null=True, blank=True)
    class Meta:
        verbose_name = _("نوع العملة")
        verbose_name_plural = _("أنواع العملة")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("currency type_detail", kwargs={"pk": self.pk})


class Offer(models.Model):

    website = models.ForeignKey(Website, verbose_name=_("الموقع الالكتوني"), on_delete=models.CASCADE , blank=True , null=True)
    market = models.ForeignKey(Market, verbose_name=_("المحل التجاري"), on_delete=models.CASCADE ,blank=True , null=True)
    department = models.ForeignKey(Department, verbose_name=_("القسم"), on_delete=models.CASCADE)
    image_ar = models.ImageField(_("الصورة صورة غلاف العرض بالعربي"), upload_to="images/offer")
    image_en = models.ImageField(_("الصورة غلاف العرض بالانجلزي"), upload_to="image/offer", blank=True , null=True)
    name_ar = models.CharField(_("اسم العرض بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم العرض بالانجلزي"), max_length=50 , blank=True , null=True)
    description_ar = models.TextField(_("الوصف بالعربي"))
    description_en = models.TextField(_("الوصف بالانجلزي"), blank=True , null=True)
    status = models.ImageField(_("حالة العرض"),choices=Status.choices ,default=2)
    duration = models.DateTimeField(_("تاريخ انتهاء العرض"), auto_now=False, auto_now_add=False)
    price_before = models.DecimalField(_("السعر قبل"), max_digits=10, decimal_places=2)
    price_after = models.DecimalField(_("السعر قبل"), max_digits=10, decimal_places=2)
    currency_type = models.ForeignKey(CurrencyType, verbose_name=_("نوع العملة"), on_delete=models.CASCADE)
    distinct = models.BooleanField(_("هل العرض مميز") , default=False)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),default=timezone.now)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), null=True, blank=True)

    class Meta:
        verbose_name = _("العرض والخصومات")
        verbose_name_plural = _("العروض والخصومات")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Offer_detail", kwargs={"pk": self.pk})


class Coupon(models.Model):
    website = models.ForeignKey(Website, verbose_name=_("الموقع الالكتوني"), on_delete=models.CASCADE , blank=True , null=True)
    market = models.ForeignKey(Market, verbose_name=_("المحل التجاري"), on_delete=models.CASCADE ,blank=True , null=True)
    name_ar = models.CharField(_("الاسم بالعربي"), max_length=50)
    name_en = models.CharField(_("الاسم بالانجلزي"), max_length=50)
    image_ar = models.ImageField(_("الصورة بالعربي"), upload_to="images/coupon",)
    image_en = models.ImageField(_("الصورة بالانجلزي"), upload_to="images/coupon", blank=True , null=True)
    status = models.ImageField(_("حالة القسيمة"),choices=Status.choices ,default=2)
    coupon_value = models.DecimalField(_("قيمة القسية"), max_digits=10, decimal_places=2)
    currency_type = models.ForeignKey(CurrencyType, verbose_name=_("نوع العملة"), on_delete=models.CASCADE)
    description_ar = models.TextField(_("نبذة عن القسيمة بالعربي"))
    description_en = models.TextField(_("نبذة عن القسية بالانجلزي"), blank=True , null=True)
    terms_of_use_ar = models.TextField(_("شروط الاستخدام في بالعربي"))
    terms_of_use_en = models.TextField(_("شروط الاستخدام بالانجلزي"), blank=True , null=True)
    duration = models.DateTimeField(_("تاريخ انتهاء القسيمة"), auto_now=False, auto_now_add=False)
    use = models.IntegerField(_("عدد الاستخدام "))
    create_at = models.DateTimeField(_("تاريخ الانشاء"),default=timezone.now)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("القسيمة")
        verbose_name_plural = _("القسائم")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Coupon_detail", kwargs={"pk": self.pk})


class LocalCoupon(models.Model):
    website = models.ForeignKey(Website, verbose_name=_("الموقع الالكتوني"), on_delete=models.CASCADE , blank=True , null=True)
    market = models.ForeignKey(Market, verbose_name=_("المحل التجاري"), on_delete=models.CASCADE ,blank=True , null=True)
    image_ar = models.ImageField(_("الصورة بالعربي"), upload_to="images/coupon",)
    image_en = models.ImageField(_("الصورة بالانجلزي"), upload_to="images/coupon", blank=True , null=True)
    coupon_value = models.DecimalField(_("قيمة الكوبون"), max_digits=10, decimal_places=2)
    currency_type = models.ForeignKey(CurrencyType, verbose_name=_("نوع العملة"), on_delete=models.CASCADE)
    status = models.ImageField(_("حالة الكوبون"),choices=Status.choices ,default=2)
    description_ar = models.TextField(_("نبذة عن الكوبو ن بالعربي"))
    description_en = models.TextField(_("نبذة عن الكوبون بالانجلزي"), blank=True , null=True)
    terms_of_use_ar = models.TextField(_("شروط الاستخدام في بالعربي"))
    terms_of_use_en = models.TextField(_("شروط الاستخدام بالانجلزي"), blank=True , null=True)
    use = models.IntegerField(_("عدد الاستخدام "))
    duration = models.DateTimeField(_("تاريخ انتهاء القسيمة"), auto_now=False, auto_now_add=False)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),default=timezone.now)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("القسائم المحلية")
        verbose_name_plural = _("القسائم المحلية")

    def __str__(self):
        return self.description_ar

    def get_absolute_url(self):
        return reverse("LocalCoupon_detail", kwargs={"pk": self.pk})


class GlobalCoupon(models.Model):
    
    global_website = models.ForeignKey(GlobalWebsite, verbose_name=_("الموقع الالكتروني"), on_delete=models.CASCADE)
    image_ar = models.ImageField(_("الصورة بالعربي"), upload_to="images/coupon",)
    image_en = models.ImageField(_("الصورة بالانجلزي"), upload_to="images/coupon", blank=True , null=True)
    coupon_value = models.DecimalField(_("قيمة الكوبون"), max_digits=10, decimal_places=2)
    currency_type = models.ForeignKey(CurrencyType, verbose_name=_("نوع العملة"), on_delete=models.CASCADE)
    status = models.ImageField(_("حالة الكوبون"),choices=Status.choices ,default=2)
    description_ar = models.TextField(_("نبذة عن الكوبو ن بالعربي"))
    description_en = models.TextField(_("نبذة عن الكوبون بالانجلزي"), blank=True , null=True)
    terms_of_use_ar = models.TextField(_("شروط الاستخدام في بالعربي"))
    terms_of_use_en = models.TextField(_("شروط الاستخدام بالانجلزي"), blank=True , null=True)
    use = models.IntegerField(_("عدد الاستخدام "))
    duration = models.DateTimeField(_("تاريخ انتهاء القسيمة"), auto_now=False, auto_now_add=False)
    create_at = models.DateTimeField(_("تاريخ الانشاء"),default=timezone.now)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)
    class Meta:
        verbose_name = _("الكوبون العالمي")
        verbose_name_plural = _("الكوبون العالمي")

    def __str__(self):
        return self.description_ar

    def get_absolute_url(self):
        return reverse("GlodeCopens_detail", kwargs={"pk": self.pk})





