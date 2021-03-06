# Generated by Django 3.2.12 on 2022-02-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kot_location', '0006_alter_kot_kot_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kot',
            name='kot_city',
            field=models.CharField(choices=[('Namur', 'Namur'), ('Louvain-la-Neuve', 'Louvain-la-Neuve'), ('Liège', 'Liège'), ('Bruxelles', 'Bruxelles')], max_length=30),
        ),
        migrations.AlterField(
            model_name='kot',
            name='kot_image',
            field=models.ImageField(upload_to='kot_location/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('OWNER', 'Propriétaire'), ('RENTER', 'Locataire')], max_length=30),
        ),
    ]
