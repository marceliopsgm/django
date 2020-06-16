# Generated by Django 3.0.3 on 2020-06-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta3P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=256)),
                ('cod_departamento', models.PositiveIntegerField()),
                ('departamento', models.CharField(max_length=256)),
                ('cod_subdepartamento', models.IntegerField()),
                ('ponto_venda', models.CharField(blank=True, max_length=256, null=True)),
                ('alcance_tv_shop', models.CharField(blank=True, max_length=1, null=True)),
                ('data', models.DateField()),
                ('valor_calculado', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('valor_calc_alcance_shop', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('data_update', models.DateField(blank=True, null=True)),
                ('val_calc_mesmas_lojas', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('val_calc_alcance_mesmas_lojas_shop', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('val_calc_novas_lojas', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('val_calc_alcance_novas_lojas_shop', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
    ]