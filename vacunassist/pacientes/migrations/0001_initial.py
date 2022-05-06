# Generated by Django 4.0.3 on 2022-05-06 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientsDetails',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.IntegerField(unique=True, verbose_name='DNI')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Mail')),
                ('gender', models.CharField(max_length=20, verbose_name='Sexo')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('first_name', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('birth_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('security_token', models.IntegerField(verbose_name='Token')),
                ('is_risk_patient', models.BooleanField(verbose_name='Paciente de Riesgo')),
                ('has_yellow_fever_vaccine', models.BooleanField(verbose_name='Vacuna F.A Aplicada')),
            ],
            options={
                'db_table': 'patients_details',
            },
        ),
        migrations.CreateModel(
            name='PatientsRequests',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('estimated_date', models.DateField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.patientsdetails')),
            ],
            options={
                'db_table': 'patients_requests',
            },
        ),
        migrations.CreateModel(
            name='VaccinationCenters',
            fields=[
                ('vaccination_center_id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_description', models.CharField(max_length=200, verbose_name='Centro de Preferencia')),
            ],
            options={
                'db_table': 'vaccination_centers',
            },
        ),
        migrations.CreateModel(
            name='VaccinesDetails',
            fields=[
                ('vaccine_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('dose_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'vaccines_details',
            },
        ),
        migrations.CreateModel(
            name='UsersDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_id', models.IntegerField()),
                ('description', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_details',
            },
        ),
        migrations.CreateModel(
            name='PatientsShifts',
            fields=[
                ('shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('confirmed_shift_date', models.DateField(blank=True, null=True)),
                ('flag_done_shift', models.BooleanField(default=False)),
                ('flag_missed_shift', models.BooleanField(default=False)),
                ('flag_waiting_shift', models.BooleanField(default=True)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.patientsrequests')),
            ],
            options={
                'db_table': 'patients_shifts',
            },
        ),
        migrations.AddField(
            model_name='patientsrequests',
            name='vaccine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.vaccinesdetails'),
        ),
        migrations.AddField(
            model_name='patientsdetails',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.usersdetails'),
        ),
        migrations.AddField(
            model_name='patientsdetails',
            name='vaccination_center_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientess.vaccinationcenters'),
        ),
    ]
