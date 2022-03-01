# Generated by Django 3.2.12 on 2022-02-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kot_location', '0008_auto_20220228_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kot',
            name='kot_city',
            field=models.CharField(choices=[('Namur', 'Namur'), ('Liège', 'Liège'), ('Louvain-la-Neuve', 'Louvain-la-Neuve'), ('Bruxelles', 'Bruxelles')], max_length=30),
        ),
        migrations.AlterField(
            model_name='kot',
            name='kot_image',
            field=models.ImageField(default='https://d34ip4tojxno3w.cloudfront.net/app/uploads/placeholder.jpg', upload_to='kot_location/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('OWNER', 'Propriétaire'), ('RENTER', 'Locataire')], max_length=30),
        ),
    ]
