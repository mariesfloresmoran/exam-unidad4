# Generated by Django 4.1.4 on 2022-12-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.URLField()),
                ('titulo_proyecto', models.CharField(max_length=200)),
                ('descripcion_proyecto', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'proyectos',
                'ordering': ['titulo_proyecto'],
            },
        ),
    ]
