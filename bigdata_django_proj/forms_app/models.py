from django.db import models
import datetime
from django.urls import reverse

class Meta1P(models.Model):
    marca = models.CharField(max_length=256)
    cod_departamento = models.PositiveIntegerField()
    cod_subdepartamento = models.IntegerField()
    cod_segmento = models.PositiveIntegerField()
    cod_marca_propria = models.IntegerField()

    #Shoptime
    alcance_tv_shop = models.CharField(max_length=1, null=True, blank=True)

    cod_dispositivo_origem = models.PositiveIntegerField()
    cod_unidade_negocio = models.PositiveIntegerField()
    dia = models.DateField()
    valor_calculado = models.DecimalField(decimal_places=2, max_digits=30)

    #Shoptime
    valor_calc_alcance_shop = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    percentual_margem_orcada = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"""{self.dia} - {self.marca} - {round(self.valor_calculado, 2)} - {self.percentual_margem_orcada}%"""

    def get_absolute_url(self):
        return reverse("forms_app:1p_list")

class  Meta3P(models.Model):
    marca = models.CharField(max_length=256)
    cod_departamento = models.PositiveIntegerField()
    departamento = models.CharField(max_length=256)
    cod_subdepartamento = models.IntegerField()
    ponto_venda = models.CharField(max_length=256, null=True, blank=True)

    #Shoptime
    alcance_tv_shop = models.CharField(max_length=1, null=True, blank=True)

    data = models.DateField()
    valor_calculado = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    #Shoptime
    valor_calc_alcance_shop = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    data_update = models.DateField(null=True, blank=True)
    val_calc_mesmas_lojas = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    #Shoptime
    val_calc_alcance_mesmas_lojas_shop = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    val_calc_novas_lojas = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    #Shoptime
    val_calc_alcance_novas_lojas_shop = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)

    def __str__(self):
        return f"""{self.data} - {self.marca}%"""

    def get_absolute_url(self):
        return reverse("forms_app:3p_list")

