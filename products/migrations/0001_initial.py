# Generated by Django 3.2 on 2022-11-20 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max_length=100', max_length=100, unique=True, verbose_name='Brand name')),
                ('slug', models.SlugField(help_text='format: required, max_length=150', max_length=100, unique=True, verbose_name='Brand slug')),
                ('description', models.TextField(help_text='format: reqd, max_length=500', max_length=500, verbose_name='Brand description')),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max_length=150', max_length=100, unique=True, verbose_name='Category title')),
                ('slug', models.SlugField(help_text='format: required, max_length=250', max_length=150, unique=True, verbose_name='Category slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Main_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max_length=150', max_length=100, unique=True, verbose_name='Main Category title')),
                ('slug', models.SlugField(help_text='format: required, max_length=150', max_length=150, unique=True, verbose_name='Main Category slug')),
            ],
            options={
                'verbose_name': 'Main Category',
                'verbose_name_plural': 'Main Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max_length=100', max_length=100, unique=True, verbose_name='Subcategory title')),
                ('slug', models.SlugField(help_text='format: required, max_length=250', max_length=250, unique=True, verbose_name='Subcategory slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='category title')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(help_text='format: required,max_length=50', max_length=50)),
                ('name', models.CharField(help_text='format: required, max_length=200', max_length=200, unique=True, verbose_name='Product name')),
                ('slug', models.SlugField(help_text='format: required, max_length=250', max_length=250, unique=True, verbose_name='Product slug')),
                ('is_featured', models.BooleanField(default=False)),
                ('total_quantity', models.IntegerField(unique=True, verbose_name='Product quantity')),
                ('availability', models.IntegerField(unique=True)),
                ('description', models.TextField(help_text='format: required, max_length=50', max_length=500, verbose_name='Product description')),
                ('how_to_use', models.TextField(help_text='format: required, max_length=500', max_length=500, verbose_name='How to use')),
                ('ingredients', models.TextField(help_text='format: reqd, max_length=500', max_length=500, verbose_name='Product ingredients')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField(max_length=1500)),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand', verbose_name='brand title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='category title')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.main_category', verbose_name='main category title'),
        ),
    ]
