# Generated by Django 3.1.3 on 2021-10-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
            ],
            options={
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssetsRegistry.category')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='DepartmentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssetsRegistry.department')),
            ],
            options={
                'verbose_name_plural': 'DepartmentsItems',
            },
        ),
        migrations.CreateModel(
            name='AssetsRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_number', models.SlugField(blank=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, max_length=1250)),
                ('Amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('YearNow', models.CharField(default='2023/2024', max_length=25)),
                ('QuarterNow', models.CharField(default='Q1', max_length=25)),
                ('depreciation_type', models.CharField(max_length=225)),
                ('depreciation_rate', models.FloatField(default='0.1', max_length=225)),
                ('depreciation_date', models.DateTimeField()),
                ('item_serial_no', models.CharField(max_length=225)),
                ('item_make_model', models.CharField(max_length=225)),
                ('item_category_asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AssetsRegistry.category')),
                ('item_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AssetsRegistry.department')),
                ('item_name_asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AssetsRegistry.item')),
                ('item_name_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AssetsRegistry.itemtype')),
                ('items_dept_asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AssetsRegistry.departmentitem')),
            ],
        ),
    ]
