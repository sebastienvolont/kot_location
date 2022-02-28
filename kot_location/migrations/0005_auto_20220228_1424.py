# Generated by Django 3.2.12 on 2022-02-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kot_location', '0004_auto_20220228_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kot',
            name='kot_city',
            field=models.CharField(choices=[('Namur', 'Namur'), ('Louvain-la-Neuve', 'Louvain-la-Neuve'), ('Bruxelles', 'Bruxelles'), ('Liège', 'Liège')], max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('RENTER', 'Locataire'), ('OWNER', 'Propriétaire')], max_length=30),
        ),
    ]
