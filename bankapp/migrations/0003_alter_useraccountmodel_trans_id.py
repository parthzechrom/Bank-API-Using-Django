# Generated by Django 4.1 on 2022-08-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_customuser_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountmodel',
            name='trans_id',
            field=models.BigIntegerField(db_column='trans_account_no', default=0, null=True),
        ),
    ]