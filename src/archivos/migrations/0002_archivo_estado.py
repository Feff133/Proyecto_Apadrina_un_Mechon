# Generated by Django 3.2 on 2021-12-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='estado',
            field=models.IntegerField(choices=[(0, 'activo'), (1, 'bajado')], default=0),
            preserve_default=False,
        ),
    ]
