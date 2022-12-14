# Generated by Django 3.2.7 on 2022-10-20 18:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(20)], verbose_name='Özet')),
                ('image_name', models.CharField(max_length=50, verbose_name='Resim')),
                ('image_cover', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=19)),
                ('language', models.CharField(max_length=100)),
                ('is_released', models.BooleanField(default=False)),
                ('is_coming', models.BooleanField(default=True)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('biography', models.CharField(max_length=3000)),
                ('image_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Erkek'), ('F', 'Kadın')], max_length=1, verbose_name='cinsiyet')),
                ('duty_type', models.CharField(choices=[('1', 'Görevli'), ('2', 'Oyuncu'), ('3', 'Yönetmen'), ('4', 'Senarist')], max_length=1, verbose_name='görev')),
            ],
            options={
                'verbose_name': 'Kişi',
                'verbose_name_plural': 'Kişiler',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(to='movies.Person'),
        ),
    ]
