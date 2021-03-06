# Generated by Django 3.2.7 on 2021-12-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(choices=[(1, 'small'), (2, 'tall')])),
                ('color', models.PositiveSmallIntegerField(choices=[(1, 'black'), (2, 'white')])),
                ('top', models.PositiveSmallIntegerField(choices=[(1, 'holed'), (2, 'fill')])),
            ],
        ),
    ]
