# Generated by Django 2.0.6 on 2018-06-26 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180620_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('submission', models.IntegerField(default=0)),
                ('handle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.User')),
            ],
        ),
    ]
