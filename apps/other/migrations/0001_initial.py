# Generated by Django 2.2 on 2020-02-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='菜单名称')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单链接')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单图标')),
                ('status', models.CharField(choices=[('y', '显示'), ('n', '隐藏')], default='y', max_length=1, verbose_name='显示状态')),
            ],
            options={
                'verbose_name_plural': '菜单栏',
                'verbose_name': '菜单栏',
            },
        ),
    ]