# Generated by Django 3.0.7 on 2020-07-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writername',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Writernames',
            },
        ),
        migrations.CreateModel(
            name='Blogdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=500)),
                ('blog', models.TextField(max_length=20000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('writer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Writername')),
            ],
            options={
                'verbose_name_plural': 'Blogdetails',
            },
        ),
    ]
