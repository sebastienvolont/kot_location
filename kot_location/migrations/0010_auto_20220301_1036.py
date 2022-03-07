# Generated by Django 3.2.12 on 2022-03-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kot_location', '0009_auto_20220228_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kot',
            name='kot_city',
            field=models.CharField(choices=[('Liège', 'Liège'), ('Namur', 'Namur'), ('Louvain-la-Neuve', 'Louvain-la-Neuve'), ('Bruxelles', 'Bruxelles')], max_length=30),
        ),
        migrations.AlterField(
            model_name='kot',
            name='kot_image',
            field=models.ImageField(default='img-placeholder.jpg', upload_to='kot_location/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('RENTER', 'Locataire'), ('OWNER', 'Propriétaire')], max_length=30),
        ),
    ]
