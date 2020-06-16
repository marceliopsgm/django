from django.shortcuts import render, redirect

# Using class based views
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from forms_app import models
from django.urls import reverse_lazy

from django.core.files.storage import FileSystemStorage
import pandas as pd

# class IndexView(TemplateView):
#     template_name = 'index.html'

def home(request):
    return render(request, 'home.html')

################################################################
###### Authentication
################################################################
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         print('if')
#     else:
#         form = UserCreationForm()
#         print('else')
#     return render(request, 'registration/signup.html', {'form': form})

################################################################
###### 1P
################################################################

class Meta1PListView(ListView):
    context_object_name = 'ctx_meta1p'
    model = models.Meta1P
    # template_name = 'forms_app/meta1p_list.html'

class Meta1PDetailView(DetailView):
    context_object_name = 'ctx_meta1p_detail'
    models = models.Meta1P
    template_name = 'forms_app/meta1p_detail.html'

    def get_queryset(self):
      return models.Meta1P.objects.order_by('id')

class Meta1PCreateView(CreateView):
    fields = ('marca', 'cod_departamento', 'cod_subdepartamento', 'cod_segmento', 'cod_marca_propria',
              'alcance_tv_shop', 'cod_dispositivo_origem', 'cod_unidade_negocio', 'dia',
               'valor_calculado', 'valor_calc_alcance_shop', 'percentual_margem_orcada')
    model = models.Meta1P
    # template_name = 'forms_app/meta1p_create.html'


class Meta1PUpdateView(UpdateView):
    fields = ('marca', 'cod_departamento', 'cod_subdepartamento', 'cod_segmento', 'cod_marca_propria',
              'alcance_tv_shop', 'cod_dispositivo_origem', 'cod_unidade_negocio', 'dia',
               'valor_calculado', 'valor_calc_alcance_shop', 'percentual_margem_orcada')
    model = models.Meta1P

class Meta1PDeleteView(DeleteView):
    model = models.Meta1P
    success_url = reverse_lazy("forms_app:list")

def meta1pUpload(request):
    context = {}
    if request.method == 'POST':

        uploaded_file = request.FILES['1p_csv_file']
        fs = FileSystemStorage()

        # Check the name and the size of the file
        is_csv_valid = uploaded_file.name.endswith('.csv')
        is_size_valid = uploaded_file.size > 0

        if is_csv_valid and is_size_valid:
            # Save and load file to/from django
            tmp_save_file = fs.save(uploaded_file.name, uploaded_file)
            tmp_load_file = fs.open(tmp_save_file, mode='rb')

            # Convert the file into Pandas Dataframe
            df = pd.read_csv(tmp_load_file)

            # Check if the header is valid
            lst_expected = ['marca', 'cod_departamento', 'cod_subdepartamento', 'cod_segmento', 'cod_marca_propria',
                            'alcance_tv_shop', 'cod_dispositivo_origem', 'cod_unidade_negocio', 'dia',
                            'valor_calculado', 'valor_calc_alcance_shop', 'percentual_margem_orcada']

            lst_header = []
            for i in df.columns:
                lst_header.append(i.lower())

            if lst_expected == lst_header:
                print('\n--------------\n Arquivo lido\n--------------\n{}\n'.format(df.iloc[0:10]))
                print(df.dtypes)

                ##############################################################################
                # Check if the mandatory fields are filled
                ##############################################################################
                lst_filled_valid = []

                if df.isnull().marca.any():
                    lst_filled_valid.append('marca')

                if df.isnull().cod_departamento.any():
                    lst_filled_valid.append('cod_departamento')

                if df.isnull().cod_subdepartamento.any():
                    lst_filled_valid.append('cod_subdepartamento')

                if df.isnull().cod_segmento.any():
                    lst_filled_valid.append('cod_segmento')

                if df.isnull().cod_marca_propria.any():
                    lst_filled_valid.append('cod_marca_propria')

                if df.isnull().cod_dispositivo_origem.any():
                    lst_filled_valid.append('cod_dispositivo_origem')

                if df.isnull().cod_unidade_negocio.any():
                    lst_filled_valid.append('cod_unidade_negocio')

                if df.isnull().dia.any():
                    lst_filled_valid.append('dia')

                if df.isnull().valor_calculado.any():
                    lst_filled_valid.append('valor_calculado')

                if df.isnull().percentual_margem_orcada.any():
                    lst_filled_valid.append('percentual_margem_orcada')

                ##############################################################################
                # Check if the field type is valid
                ##############################################################################
                lst_type_valid = []
                if 'int64' == df.cod_departamento.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_departamento')

                if 'int64' == df.cod_subdepartamento.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_subdepartamento')

                if 'int64' == df.cod_segmento.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_segmento')

                if 'int64' == df.cod_marca_propria.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_marca_propria')

                if 'int64' == df.cod_dispositivo_origem.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_dispositivo_origem')

                if 'int64' == df.cod_unidade_negocio.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_unidade_negocio')

                if 'int64' == df.valor_calc_alcance_shop.dtype or 'float64' == df.valor_calc_alcance_shop.dtype:
                    pass
                else:
                    lst_type_valid.append('valor_calc_alcance_shop')

                if 'int64' == df.valor_calculado.dtype or 'float64' == df.valor_calculado.dtype:
                    pass
                else:
                    lst_type_valid.append('valor_calculado')

                if 'float64' == df.percentual_margem_orcada.dtype:
                     pass
                else:
                     lst_type_valid.append('percentual_margem_orcada')

                ##############################################################################

                ##############
                # Main
                ##############
                if len(lst_filled_valid) == 0:
                    if len(lst_type_valid) == 0:
                        context['status'] = 'Arquivo carregado com sucesso: {}'.format(fs.url(uploaded_file.name).replace('/media/',''))
                        # context['arquivo'] = format(df.iloc[0:10])
                    else:
                        context['status'] = 'Campos com formatos diferentes: {}'.format(lst_type_valid)
                        context['mensagem'] = 'Favor corrigir e tentar novamente.'
                else:
                    context['status'] = 'Os campos a seguir são obrigatórios: {}'.format(lst_filled_valid)
                    context['mensagem'] = 'Favor preencher e tentar novamente.'


        else:
            context['status'] = 'Arquivo inválido!'
            context['mensagem'] = 'Favor submeter um arquivo no formato CSV.'

    return render(request, 'forms_app/meta1p_upload.html', context)

################################################################
###### 3P
################################################################

def meta3pUpload(request):
    context = {}
    if request.method == 'POST':

        uploaded_file = request.FILES['3p_csv_file']
        fs = FileSystemStorage()

        # Check the name and the size of the file
        is_csv_valid = uploaded_file.name.endswith('.csv')
        is_size_valid = uploaded_file.size > 0

        if is_csv_valid and is_size_valid:
            # Save and load file to/from django
            tmp_save_file = fs.save(uploaded_file.name, uploaded_file)
            tmp_load_file = fs.open(tmp_save_file, mode='rb')

            # Convert the file into Pandas Dataframe
            df = pd.read_csv(tmp_load_file)

            # Check if the header is valid
            lst_expected = ['marca', 'cod_departamento', 'departamento', 'cod_subdepartamento', 'ponto_venda',
                            'alcance_tv_shop','data','valor_calculado','valor_calc_alcance_shop','data_update',
                            'val_calc_mesmas_lojas','val_calc_alcance_mesmas_lojas_shop','val_calc_novas_lojas',
                            'val_calc_alcance_novas_lojas_shop']

            lst_header = []
            for i in df.columns:
                lst_header.append(i.lower())

            if lst_expected == lst_header:
                print('\n--------------\n Arquivo lido\n--------------\n{}\n'.format(df.iloc[0:10]))
                print(df.dtypes)

                ##############################################################################
                # Check if the mandatory fields are filled
                ##############################################################################
                lst_filled_valid = []

                if df.isnull().marca.any():
                    lst_filled_valid.append('marca')

                if df.isnull().cod_departamento.any():
                    lst_filled_valid.append('cod_departamento')

                if df.isnull().departamento.any():
                    lst_filled_valid.append('departamento')

                if df.isnull().cod_subdepartamento.any():
                    lst_filled_valid.append('cod_subdepartamento')

                if df.isnull().data.any():
                    lst_filled_valid.append('data')

                # ##############################################################################
                # # Check if the field type is valid
                # ##############################################################################
                lst_type_valid = []
                if 'int64' == df.cod_departamento.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_departamento')

                if 'int64' == df.cod_subdepartamento.dtype:
                    pass
                else:
                    lst_type_valid.append('cod_subdepartamento')

                if 'int64' == df.alcance_tv_shop.dtype or 'float64' == df.alcance_tv_shop.dtype:
                    pass
                else:
                    lst_type_valid.append('alcance_tv_shop')

                if 'int64' == df.valor_calculado.dtype or 'float64' == df.valor_calculado.dtype:
                    pass
                else:
                    lst_type_valid.append('valor_calculado')

                if 'int64' == df.valor_calc_alcance_shop.dtype or 'float64' == df.valor_calc_alcance_shop.dtype:
                    pass
                else:
                    lst_type_valid.append('valor_calc_alcance_shop')

                if 'int64' == df.val_calc_mesmas_lojas.dtype or 'float64' == df.val_calc_mesmas_lojas.dtype:
                    pass
                else:
                    lst_type_valid.append('val_calc_mesmas_lojas')

                if 'int64' == df.val_calc_alcance_mesmas_lojas_shop.dtype or 'float64' == df.val_calc_alcance_mesmas_lojas_shop.dtype:
                    pass
                else:
                    lst_type_valid.append('val_calc_alcance_mesmas_lojas_shop')

                if 'int64' == df.val_calc_novas_lojas.dtype or 'float64' == df.val_calc_novas_lojas.dtype:
                    pass
                else:
                    lst_type_valid.append('val_calc_novas_lojas')

                if 'int64' == df.val_calc_alcance_novas_lojas_shop.dtype or 'float64' == df.val_calc_alcance_novas_lojas_shop.dtype:
                    pass
                else:
                    lst_type_valid.append('val_calc_alcance_novas_lojas_shop')


                # ##############################################################################

                ##############
                # Main
                ##############
                if len(lst_filled_valid) == 0:
                    if len(lst_type_valid) == 0:
                        context['status'] = 'Arquivo carregado com sucesso: {}'.format(fs.url(uploaded_file.name).replace('/media/',''))
                        # context['arquivo'] = format(df.iloc[0:10])
                    else:
                        context['status'] = 'Campos com formatos diferentes: {}'.format(lst_type_valid)
                        context['mensagem'] = 'Favor corrigir e tentar novamente.'
                else:
                    context['status'] = 'Os campos a seguir são obrigatórios: {}'.format(lst_filled_valid)
                    context['mensagem'] = 'Favor preencher e tentar novamente.'


        else:
            context['status'] = 'Arquivo inválido!'
            context['mensagem'] = 'Favor submeter um arquivo no formato CSV.'

    return render(request, 'forms_app/meta3p_upload.html', context)


class Meta3PListView(ListView):
    context_object_name = 'ctx_meta3p'
    model = models.Meta3P
    # template_name = 'forms_app/meta1p_list.html'

class Meta3PDetailView(DetailView):
    context_object_name = 'ctx_meta3p_detail'
    models = models.Meta3P
    template_name = 'forms_app/meta3p_detail.html'

    def get_queryset(self):
      return models.Meta3P.objects.order_by('id')

class Meta3PCreateView(CreateView):
    fields = ('marca', 'cod_departamento', 'departamento', 'cod_subdepartamento',
             'ponto_venda', 'alcance_tv_shop', 'data', 'valor_calculado',
             'valor_calc_alcance_shop', 'data_update', 'val_calc_mesmas_lojas',
             'val_calc_alcance_mesmas_lojas_shop', 'val_calc_novas_lojas',
             'val_calc_alcance_novas_lojas_shop')
    model = models.Meta3P

class Meta3PUpdateView(UpdateView):
    fields = ('marca', 'cod_departamento', 'departamento', 'cod_subdepartamento',
             'ponto_venda', 'alcance_tv_shop', 'data', 'valor_calculado',
             'valor_calc_alcance_shop', 'data_update', 'val_calc_mesmas_lojas',
             'val_calc_alcance_mesmas_lojas_shop', 'val_calc_novas_lojas',
             'val_calc_alcance_novas_lojas_shop')
    model = models.Meta3P

class Meta3PDeleteView(DeleteView):
    model = models.Meta3P
    success_url = reverse_lazy("forms_app:list")