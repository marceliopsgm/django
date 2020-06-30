from django import forms
from .metas_app.models import Meta1P, Meta3P


class Meta1pForm(forms.ModelForm):

    class Meta:
        model = Meta1P
        # fields = '__all__'
        fields = ('marca', 'cod_departamento', 'cod_subdepartamento', 'cod_segmento', 'cod_marca_propria',
                  'alcance_tv_shop', 'cod_dispositivo_origem', 'cod_unidade_negocio', 'dia', 'valor_calculado',
                  'valor_calc_alcance_shop', 'percentual_margem_orcada')

        labels = {
            'cod_departamento': 'Código do Departamento',
            'cod_subdepartamento': 'Código do Subdepartamento',
            'cod_segmento': 'Código do Segmento',
            'cod_marca_propria': 'Código da Marca Própria',
            'alcance_tv_shop': 'Alcance TV Shoptime',
            'cod_dispositivo_origem': 'Código do Dispositivo de Origem',
            'cod_unidade_negocio': 'Código da Unidade de Negócio',
            'dia':'Dia (mm/dd/yyyy)',
            'valor_calculado': 'Valor Calculado',
            'valor_calc_alcance_shop': 'Valor Calculado Alcance Shoptime',
            'percentual_margem_orcada': 'Percentual da Margem Orçada'
        }

class Meta3pForm(forms.ModelForm):

    class Meta:
        model = Meta3P
        # fields = '__all__'
        fields = ('marca', 'cod_departamento', 'departamento', 'cod_subdepartamento', 'ponto_venda', 'alcance_tv_shop',
                  'data', 'valor_calculado', 'valor_calc_alcance_shop', 'data_update', 'val_calc_mesmas_lojas',
                  'val_calc_alcance_mesmas_lojas_shop', 'val_calc_novas_lojas', 'val_calc_alcance_novas_lojas_shop')

        labels = {
            'cod_departamento': 'Código do Departamento',
            'cod_subdepartamento': 'Código do Subdepartamento',
            'ponto_venda': 'Ponto de Venda',
            'alcance_tv_shop': 'Alcance TV Shoptime',
            'data': 'Data (mm/dd/yyyy)',
            'valor_calculado': 'Valor Calculado',
            'valor_calc_alcance_shop': 'Valor Calculado Alcance Shoptime',
            'data_update': 'Data de Update (mm/dd/yyyy)',
            'val_calc_mesmas_lojas': 'Valor Calculado Mesmas Lojas',
            'val_calc_alcance_mesmas_lojas_shop': 'Valor Calculado Mesmas Lojas Shoptime',
            'val_calc_novas_lojas': 'Valor Calculado Novas Lojas',
            'val_calc_alcance_novas_lojas_shop': 'Valor Calculado Alcance Novas Lojas Shoptime'
        }