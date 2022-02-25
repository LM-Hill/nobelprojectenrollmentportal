# Generated by Django 2.2.4 on 2021-07-20 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enroll_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StipendSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talent', models.CharField(max_length=3)),
                ('payable', models.CharField(max_length=60)),
                ('citizen', models.CharField(max_length=3)),
                ('soc_sec', models.CharField(max_length=11)),
                ('dateofbirth', models.DateTimeField()),
                ('pmtaddr', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stipend_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stipendapplicant', to='enroll_app.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='IRBConsentSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consentq1', models.CharField(max_length=255)),
                ('consentq2', models.CharField(max_length=255)),
                ('consentq3', models.CharField(max_length=255)),
                ('consentq4', models.CharField(blank=True, max_length=255)),
                ('cvideo', models.CharField(max_length=3)),
                ('caudio', models.CharField(max_length=3)),
                ('cvideohouse', models.CharField(max_length=3)),
                ('cvideoroom', models.CharField(max_length=3)),
                ('cvideome', models.CharField(max_length=3)),
                ('cvideocontents', models.CharField(max_length=3)),
                ('csign', models.CharField(max_length=255)),
                ('cfuture', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('irb_consent_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consentee', to='enroll_app.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='IRBAssentSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assentq1', models.CharField(max_length=255)),
                ('assentq2', models.CharField(max_length=255)),
                ('assentq3', models.CharField(max_length=255)),
                ('assentq4', models.CharField(blank=True, max_length=255)),
                ('svideo', models.CharField(max_length=3)),
                ('saudio', models.CharField(max_length=3)),
                ('stusign', models.CharField(max_length=255)),
                ('sfuture', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('irb_assent_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assentee', to='enroll_app.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='InterestSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral', models.CharField(max_length=255)),
                ('expectation', models.TextField()),
                ('goals', models.TextField()),
                ('dream_career', models.TextField()),
                ('social_issue', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('interest_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest_survey', to='enroll_app.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='DemographicsSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('grade_level', models.CharField(max_length=5)),
                ('household', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('school', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='enroll_app.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverInterestSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caregiver_expectation', models.TextField()),
                ('caregiver_goals', models.TextField()),
                ('caregiver_dream_career', models.TextField()),
                ('career', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('caregiver_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caregiver_interest_survey', to='enroll_app.Caregiver')),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverDemographicsSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caregiver_race', models.CharField(max_length=50)),
                ('caregiver_gender', models.CharField(max_length=50)),
                ('education_level', models.CharField(max_length=50)),
                ('professional_certs', models.TextField(blank=True)),
                ('household_income', models.CharField(choices=[('1', 'Less than $10,000'), ('2', '$10,000 - $19,000'), ('3', '$20,000 - $29,000'), ('4', '$30,000 - $39,000'), ('5', '$40,000 - $49,000'), ('6', '$50,000 - $75,000'), ('7', '$75,000 - $100,000'), ('8', '$100,000 or More')], max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caregiver_targets', to='enroll_app.Caregiver')),
            ],
        ),
    ]