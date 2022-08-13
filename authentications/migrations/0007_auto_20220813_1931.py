# Generated by Django 3.2.13 on 2022-08-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0006_auto_20220412_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='parent_phone',
            new_name='contact_no',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='dp',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='grantedby',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='hostler',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='id',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='roll_no',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='student_phone',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='user_id',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='type_of_account',
            field=models.CharField(choices=[('STARTUP', 'startup'), ('INVESTOR', 'investor')], default='STARTUP', max_length=20),
        ),
    ]