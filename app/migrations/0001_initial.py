# Generated by Django 4.1.7 on 2023-04-07 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('Deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=30)),
                ('Loc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('Empno', models.IntegerField(primary_key=True, serialize=False)),
                ('Ename', models.CharField(max_length=50)),
                ('Job', models.CharField(max_length=50)),
                ('Mgr', models.IntegerField()),
                ('Hiredate', models.DateField()),
                ('Sal', models.IntegerField()),
                ('Comm', models.IntegerField()),
                ('Deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
