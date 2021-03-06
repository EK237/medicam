# Generated by Django 3.0.4 on 2020-04-04 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0024_auto_20200401_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callevent',
            name='room_name',
            field=models.CharField(db_index=True, max_length=254),
        ),
        migrations.CreateModel(
            name='CallSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_connected', models.DurationField(blank=True, null=True, verbose_name='caller connected')),
                ('patient_audio_start', models.DurationField(blank=True, null=True, verbose_name='caller video started')),
                ('patient_video_start', models.DurationField(blank=True, null=True, verbose_name='caller audio started')),
                ('doctor_connected', models.DurationField(blank=True, null=True, verbose_name='provider connected')),
                ('doctor_audio_start', models.DurationField(blank=True, null=True, verbose_name='provider video started')),
                ('doctor_video_start', models.DurationField(blank=True, null=True, verbose_name='provider audio started')),
                ('duration', models.DurationField(blank=True, null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='clinic.Patient')),
            ],
        ),
    ]
