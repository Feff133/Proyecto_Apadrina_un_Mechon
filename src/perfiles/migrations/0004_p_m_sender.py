# Generated by Django 3.2 on 2021-11-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_alter_p_m_fecha_creada'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_m',
            name='sender',
            field=models.CharField(default='felipe', max_length=100),
            preserve_default=False,
        ),
    ]