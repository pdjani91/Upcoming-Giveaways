# Generated by Django 3.1.3 on 2021-03-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210313_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giveaways',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], default='open', max_length=6),
        ),
    ]
