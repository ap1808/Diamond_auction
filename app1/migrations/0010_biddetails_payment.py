# Generated by Django 4.1.2 on 2023-03-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_buyerregister_mailsend_sellerregister_mailsend'),
    ]

    operations = [
        migrations.AddField(
            model_name='biddetails',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]