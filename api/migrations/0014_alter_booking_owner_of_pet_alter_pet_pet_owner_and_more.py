# Generated by Django 4.0.1 on 2022-01-11 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_booking_owner_of_pet_alter_booking_sitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='owner_of_pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets_owmed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]