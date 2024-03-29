# Generated by Django 4.2.8 on 2024-02-19 11:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Main Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('inside_number', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('setting', models.CharField(max_length=20)),
                ('stone', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificate')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('sold', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='empty_f.jpeg', null=True, upload_to='items')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='main_cat_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.maincategory'),
        ),
    ]
