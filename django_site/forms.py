from django import forms
from .metas_app.models import Meta1P

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
            'valor_calculado': 'Valor Calculado',
            'valor_calc_alcance_shop': 'Valor Calculado Alcance Shoptime',
            'percentual_margem_orcada': 'Percentual da Margem Orçada'
        }