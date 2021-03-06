# Generated by Django 3.1.4 on 2021-01-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('Wah', 'Wah'), ('Taxila', 'Taxila'), ('Kohat', 'Kohat'), ('Vehari', 'Vehari'), ('Chakwal', 'Chakwal'), ('Kalar Kahar', 'Kalar Kahar'), ('Sangla Hill', 'Sangla Hill'), ('Shah Kot', 'Shah Kot'), ('Gojra', 'Gojra'), ('Toba Tek Singh', 'Toba Tek Singh'), ('Multan', 'Multan')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='comany_name',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='industry',
            field=models.CharField(choices=[('Apparel & Fashion', 'Apparel & Fashion'), ('Banking', 'Banking'), ('Business Supplies & Equipment', 'Business Supplies & Equipment'), ('Civic & Social Organization', 'Civic & Social Organization'), ('Commercial Real Estate', 'Commercial Real Estate'), ('Computer Software', 'Computer Software'), ('Consumer Goods', 'Consumer Goods'), ('Consumer Services', 'Consumer Services'), ('Cosmetics', 'Cosmetics'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Events Services', 'Events Services'), ('Financial Services', 'Financial Services'), ('Food & Beverage', 'Food & Beverage'), ('Furniture', 'Furniture'), ('Government Administration', 'Government Administration'), ('Health, Wellness & Fitness', 'Health, Wellness & Fitness'), ('Hospitality, Hotels', 'Hospitality, Hotels'), ('Human Resources', 'Human Resources'), ('Information Technology & Services', 'Information Technology & Services'), ('Insurance', 'Insurance'), ('Leisure & Travel', 'Leisure & Travel'), ('Luxury Goods & Jewelry', 'Luxury Goods & Jewelry'), ('Marketing & Advertising', 'Marketing & Advertising'), ('Oil & Energy', 'Oil & Energy'), ('Other', 'Other'), ('Pharmaceuticals', 'Pharmaceuticals'), ('Public Relations', 'Public Relations'), ('Retail', 'Retail'), ('Telecommunications', 'Telecommunications'), ('Tobacco', 'Tobacco'), ('Utilities', 'Utilities')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='job_role',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='phone'),
        ),
    ]
