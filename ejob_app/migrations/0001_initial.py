# Generated by Django 3.2.8 on 2021-12-15 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_recruiter', models.BooleanField(default=False)),
                ('is_seeker', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('register_Date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('seeker_name', models.CharField(max_length=255)),
                ('cover_letter', models.CharField(max_length=1000)),
                ('cv', models.CharField(max_length=1000)),
                ('matching_score', models.IntegerField()),
                ('status', models.CharField(choices=[('A', 'ACTIVE'), ('S', 'SELECTED'), ('R', 'REJECTED'), {'I', 'Interview'}], default='M', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('X', 'NO')], default='M', max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=10)),
                ('birthDate', models.DateField()),
                ('current_job_role', models.CharField(max_length=255)),
                ('current_company', models.CharField(max_length=255)),
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='SeekerSkillset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_1', models.CharField(max_length=255)),
                ('skill_2', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_3', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_4', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_5', models.CharField(blank=True, max_length=255, null=True)),
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('company_name', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=255)),
                ('company_phone', models.IntegerField()),
                ('job_role', models.CharField(max_length=255)),
                ('recruiter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.application')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.recruiterprofile')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=255)),
                ('job_description', models.CharField(max_length=1000)),
                ('organization', models.CharField(max_length=255)),
                ('remuneration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('skill_required_1', models.CharField(max_length=255)),
                ('skill_required_2', models.CharField(max_length=255)),
                ('skill_required_3', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_required_4', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_required_5', models.CharField(blank=True, max_length=255, null=True)),
                ('deadline', models.DateField()),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('job_ad_flag', models.CharField(max_length=1)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ejob_app.category')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.recruiterprofile')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ejob_app.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.application')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.job'),
        ),
        migrations.AddField(
            model_name='application',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejob_app.seekerprofile'),
        ),
    ]
