from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from edc_constants.choices import YES_NO
from edc_reportable import MILLIMOLES_PER_LITER
from edc_reportable.choices import REPORTABLE


class CholModelMixin(models.Model):
    # chol
    chol_value = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        verbose_name="chol",
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    chol_units = models.CharField(
        verbose_name="units",
        max_length=15,
        choices=((MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),),
        null=True,
        blank=True,
    )

    chol_abnormal = models.CharField(
        verbose_name="abnormal", choices=YES_NO, max_length=25, null=True, blank=True
    )

    chol_reportable = models.CharField(
        verbose_name="reportable",
        choices=REPORTABLE,
        max_length=25,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True