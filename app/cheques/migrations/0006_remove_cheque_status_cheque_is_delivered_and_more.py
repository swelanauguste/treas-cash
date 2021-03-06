# Generated by Django 4.0.2 on 2022-02-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheques', '0005_alter_cheque_amount_alter_cheque_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheque',
            name='status',
        ),
        migrations.AddField(
            model_name='cheque',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cheque',
            name='is_printed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ChequeStatus',
        ),
    ]
