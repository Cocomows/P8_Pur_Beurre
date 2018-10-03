# Generated by Django 2.1 on 2018-09-20 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pur_beurre', '0006_auto_20180920_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='save',
            name='saved_by',
        ),
        migrations.AddField(
            model_name='save',
            name='saved_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sauvegardé par'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='save',
            name='saved_product',
        ),
        migrations.AddField(
            model_name='save',
            name='saved_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pur_beurre.Product', verbose_name='Produit sauvegardé'),
            preserve_default=False,
        ),
    ]
