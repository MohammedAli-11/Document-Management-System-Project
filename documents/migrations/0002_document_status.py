# Generated by Django 3.0.5 on 2021-05-07 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('Public', 'PUBLIC'), ('Private', 'PRIVATE')], default='exit', max_length=10),
            preserve_default=False,
        ),
    ]