# Generated by Django 2.1.5 on 2019-01-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190113_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('KO', 'Korean'), ('EN', 'English')], default='KO', max_length=2),
            preserve_default=False,
        ),
    ]
