# Generated by Django 4.0.4 on 2022-05-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorMaker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculator',
            name='Formula',
        ),
        migrations.AddField(
            model_name='calculator',
            name='formula',
            field=models.TextField(default=1,  verbose_name='Formula'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calculator',
            name='name',
            field=models.CharField(max_length=500,  verbose_name='name'),
        ),
    ]