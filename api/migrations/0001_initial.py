# Generated by Django 4.0.4 on 2022-05-09 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_calibre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ObjetoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_objeto', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.objetotipo')),
            ],
        ),
        migrations.CreateModel(
            name='Municao',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.objeto')),
                ('marca', models.CharField(max_length=64)),
                ('modelo', models.CharField(max_length=64)),
                ('valor_estimado', models.FloatField()),
                ('calibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.calibre')),
            ],
        ),
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.objeto')),
                ('marca', models.CharField(max_length=64)),
                ('modelo', models.CharField(max_length=64)),
                ('quantidade_de_tiros', models.IntegerField()),
                ('valor_estimado', models.FloatField()),
                ('imagem', models.CharField(max_length=128)),
                ('calibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.calibre')),
            ],
        ),
    ]