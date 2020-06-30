from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Using class based views
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models
from django.urls import reverse_lazy

from django.core.files.storage import FileSystemStorage
import pandas as pd

def home(request):
    return render(request, 'home.html')

################################################################
# Authentication
################################################################

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


################################################################
# 1P
################################################################

# CRUD

from django_site.forms import Meta1pForm
from .models import Meta1P

def meta1pList(request):
    context = {'ctx_meta1p_list': Meta1P.objects.all()}
    return render(request, 'metas_app/meta1p_list.html', context)

def meta1pForm(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Meta1pForm()
        else:
            meta1p = Meta1P.objects.get(pk=id)
            form = Meta1pForm(instance=meta1p)
        return render(request, 'metas_app/meta1p_form.html', {'form_1p':form})
    else:
        if id == 0:
            form = Meta1pForm(request.POST)
        else:
            meta1p = Meta1P.objects.get(pk=id)
            form = Meta1pForm(request.POST, instance=meta1p)

        if form.is_valid():
            form.save()
        return redirect('1p_list')

def meta1pDelete(request, id):
    meta1p = Meta1P.objects.get(pk=id)
    meta1p.delete()
    return redirect('1p_list')

# Upload CSV
def meta1pUpload(request):
    try:
        context = {}
        if request.method == 'POST':

            uploaded_file = request.FILES['1p_csv_file']
            fs = FileSystemStorage()

            # Check the name and the size of the file
            is_csv_valid = uploaded_file.name.endswith('.csv')
            is_size_valid = uploaded_file.size > 0

            lst_expected = ['marca', 'cod_departamento', 'cod_subdepartamento', 'cod_segmento', 'cod_marca_propria',
                            'alcance_tv_shop', 'cod_dispositivo_origem', 'cod_unidade_negocio', 'dia',
                            'valor_calculado', 'valor_calc_alcance_shop', 'percentual_margem_orcada']

            # Read file and validate the header
            is_header_valid = False
            if is_size_valid:
                df_tmp = pd.read_csv(uploaded_file)
                lst_header = df_tmp.columns.tolist()
                del df_tmp

                is_header_valid = (lst_header == lst_expected)

            if is_csv_valid and is_size_valid and is_header_valid:
                # Save and load file to/from django
                tmp_save_file = fs.save(uploaded_file.name, uploaded_file)
                tmp_load_file = fs.open(tmp_save_file, mode='rb')

                # Convert the file into Pandas Dataframe
                df = pd.read_csv(tmp_load_file)

                lst_header = []
                for i in df.columns:
                    lst_header.append(i.lower())

                if lst_expected == lst_header:
                    # print('\n--------------\n Arquivo lido\n--------------\n{}\n'.format(df.iloc[0:10]))
                    # print(df.dtypes)

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
                            context['status'] = 'Arquivo atualizado com sucesso: {}'.format(fs.url(uploaded_file.name).replace('/media/',''))
                            # context['arquivo'] = format(df.iloc[0:10])
                        else:
                            fs.delete(tmp_save_file)
                            context['status'] = 'Campos com formatos diferentes: {}'.format(lst_type_valid)
                            context['message'] = 'Por favor, corrija e tente novamente'
                    else:
                        fs.delete(tmp_save_file)
                        context['status'] = 'Os campos a seguir são obrigatórios: {}'.format(lst_filled_valid)
                        context['message'] = 'Por favor, corrija e tente novamente'

            else:
                context['status'] = 'Arquivo inválido'
                context['message'] = 'Por favor, submeta um arquivo .csv válido'
                context['expected'] = 'Layout esperado: {}'.format(lst_expected)

        return render(request, 'metas_app/meta1p_upload.html', context)

    except:
        context['status'] = 'Erro tentando ler o arquivo'
        context['message'] = 'Por favor, verifique o formato e o layout do arquivo (cabeçalho e dados)'

        return render(request, 'metas_app/meta1p_upload.html', context)


################################################################
# 3P
################################################################

# CRUD

from django_site.forms import Meta3pForm
from .models import Meta3P

def meta3pList(request):
    context = {'ctx_meta3p_list': Meta3P.objects.all()}
    return render(request, 'metas_app/meta3p_list.html', context)

def meta3pForm(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Meta3pForm()
        else:
            meta3p = Meta3P.objects.get(pk=id)
            form = Meta3pForm(instance=meta3p)
        return render(request, 'metas_app/meta3p_form.html', {'form_3p':form})
    else:
        if id == 0:
            form = Meta3pForm(request.POST)
        else:
            meta3p = Meta3P.objects.get(pk=id)
            form = Meta3pForm(request.POST, instance=meta3p)

        if form.is_valid():
            form.save()
        return redirect('3p_list')

def meta3pDelete(request, id):
    meta3p = Meta3P.objects.get(pk=id)
    meta3p.delete()
    return redirect('3p_list')

# Upload CSV
def meta3pUpload(request):
    try:
        context = {}
        if request.method == 'POST':

            uploaded_file = request.FILES['3p_csv_file']
            fs = FileSystemStorage()

            # Check the name and the size of the file
            is_csv_valid = uploaded_file.name.endswith('.csv')
            is_size_valid = uploaded_file.size > 0

            lst_expected = ['marca', 'cod_departamento', 'departamento', 'cod_subdepartamento', 'ponto_venda',
                                'alcance_tv_shop','data','valor_calculado','valor_calc_alcance_shop','data_update',
                                'val_calc_mesmas_lojas','val_calc_alcance_mesmas_lojas_shop','val_calc_novas_lojas',
                                'val_calc_alcance_novas_lojas_shop']

            # Read file and validate the header
            is_header_valid = False
            if is_size_valid:
                df_tmp = pd.read_csv(uploaded_file)
                lst_header = df_tmp.columns.tolist()
                del df_tmp

                is_header_valid = (lst_header == lst_expected)

            if is_csv_valid and is_size_valid and is_header_valid:
                # Save and load file to/from django
                tmp_save_file = fs.save(uploaded_file.name, uploaded_file)
                tmp_load_file = fs.open(tmp_save_file, mode='rb')

                # Convert the file into Pandas Dataframe
                df = pd.read_csv(tmp_load_file)

                lst_header = []
                for i in df.columns:
                    lst_header.append(i.lower())

                if lst_expected == lst_header:
                    # print('\n--------------\n Arquivo lido\n--------------\n{}\n'.format(df.iloc[0:10]))
                    # print(df.dtypes)

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
                            context['status'] = 'Arquivo atualizado com sucesso: {}'.format(fs.url(uploaded_file.name).replace('/media/',''))
                            # context['arquivo'] = format(df.iloc[0:10])
                        else:
                            fs.delete(tmp_save_file)
                            context['status'] = 'Campos com formatos diferentes: {}'.format(lst_type_valid)
                            context['message'] = 'Por favor, corrija e tente novamente'
                    else:
                        fs.delete(tmp_save_file)
                        context['status'] = 'Os campos a seguir são obrigatórios: {}'.format(lst_filled_valid)
                        context['message'] = 'Por favor, corrija e tente novamente'

            else:
                context['status'] = 'Arquivo inválido'
                context['message'] = 'Por favor, submeta um arquivo .csv válido'
                context['expected'] = 'Layout esperado: {}'.format(lst_expected)

        return render(request, 'metas_app/meta3p_upload.html', context)

    except:
        context['status'] = 'Erro tentando ler o arquivo'
        context['message'] = 'Por favor, verifique o formato e o layout do arquivo (cabeçalho e dados)'

        return render(request, 'metas_app/meta3p_upload.html', context)