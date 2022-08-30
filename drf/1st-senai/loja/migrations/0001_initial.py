# Generated by Django 4.1 on 2022-08-30 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.PositiveSmallIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.categoria')),
            ],
        ),
    ]