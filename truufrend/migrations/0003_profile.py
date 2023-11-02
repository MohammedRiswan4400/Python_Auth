# Generated by Django 4.2.6 on 2023-10-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truufrend', '0002_otp_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(blank=True, null=True, upload_to='img/profile_pictures')),
                ('name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('challenges', models.TextField(choices=[('1', 'Anxiety'), ('2', 'Motivation'), ('3', 'Confidence'), ('4', 'Sleep'), ('5', 'Depression'), ('6', 'Work Stress'), ('7', 'Relationships'), ('8', 'Exam stress'), ('9', 'Pregnancy'), ('10', 'Loss'), ('11', 'LGBTQ+'), ('12', 'Low Energy'), ('13', 'Self Esteem'), ('14', 'Loneliness'), ('15', 'Trauma'), ('16', 'Health issues')])),
            ],
        ),
    ]