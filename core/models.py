from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Employee(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
