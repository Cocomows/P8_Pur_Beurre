# Generated by Django 2.1 on 2018-09-20 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pur_beurre', '0007_auto_20180920_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='saved_by',
        ),
        migrations.AlterField(
            model_name='save',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date sauvegarde'),
        ),
    ]
