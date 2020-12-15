# Generated by Django 3.0.5 on 2020-04-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('shirtunchi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('chest', models.DecimalField(decimal_places=3, max_digits=6)),
                ('shoulder', models.DecimalField(decimal_places=3, max_digits=6)),
                ('astin', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sfront', models.DecimalField(decimal_places=3, max_digits=6)),
                ('coller', models.DecimalField(decimal_places=3, max_digits=6)),
                ('cuf', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pantunchi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('kambar', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sit', models.DecimalField(decimal_places=3, max_digits=6)),
                ('mandi', models.DecimalField(decimal_places=3, max_digits=6)),
                ('gudhga', models.DecimalField(decimal_places=3, max_digits=6)),
                ('bottom', models.DecimalField(decimal_places=3, max_digits=6)),
                ('description', models.CharField(max_length=20)),
                ('payment', models.CharField(max_length=20)),
            ],
        ),
    ]
