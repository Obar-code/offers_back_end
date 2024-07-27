from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from places.models import Status
# Create your models here.

class Department(models.Model):

    name_ar = models.CharField(_("اسم القسم بالعربي"), max_length=50)
    name_en = models.CharField(_("اسم القسم بالانجلزي"), max_length=50)
    status = models.IntegerField(_("حالة القسم"), choices=Status.choices ,default=2)
    image = models.ImageField(_("الصورة"), upload_to='images/department')
    create_at = models.DateTimeField(_("تاريخ الانشاء"),auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التعديل"), auto_now=True)

    class Meta:
        verbose_name = _("قسم")
        verbose_name_plural = _("الاقسام")

    def __str__(self):
        return self.name_ar

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})



