# Generated by Django 3.0.3 on 2020-03-07 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adtaa', '0004_auto_20200307_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Adtaa.Instructor'),
        ),
    ]
