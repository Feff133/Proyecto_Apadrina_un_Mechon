# Generated by Django 3.2 on 2021-10-27 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0003_alter_p_m_fecha_creada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('estado', models.IntegerField(choices=[(0, 'Activa'), (1, 'Realizada'), (2, 'Cancelada')])),
                ('fecha_creada', models.DateTimeField(auto_now_add=True)),
                ('fecha_agendada', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rut_m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno_mec', to='perfiles.persona_auth')),
                ('rut_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno_pad', to='perfiles.persona_auth')),
            ],
        ),
    ]
