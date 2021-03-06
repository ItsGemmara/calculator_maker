# Generated by Django 4.0.4 on 2022-05-29 11:25

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorMaker', '0002_remove_calculator_formula_calculator_formula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='formula',
            field=models.TextField(unique=True, verbose_name='Formula'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='name',
            field=models.CharField(max_length=500, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='variables',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('a', 'a'), ('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'), ('f', 'f'), ('g', 'g'), ('h', 'h'), ('i', 'i'), ('j', 'j'), ('k', 'k'), ('l', 'l'), ('m', 'm'), ('n', 'n'), ('o', 'o'), ('p', 'p'), ('q', 'q'), ('r', 'r'), ('s', 's'), ('t', 't'), ('u', 'u'), ('v', 'v'), ('w', 'w'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Variables',
        ),
    ]
