# Generated by Django 3.1.2 on 2020-10-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catagory',
            options={'verbose_name_plural': 'catagories'},
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='store.catagory')),
            ],
        ),
    ]