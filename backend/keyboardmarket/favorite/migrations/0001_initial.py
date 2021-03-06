# Generated by Django 3.1.5 on 2021-10-09 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20210919_1826'),
        ('users', '0003_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='創建時間')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
                ('status', models.IntegerField(verbose_name='狀態')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='用戶')),
            ],
            options={
                'db_table': 'favorite',
            },
        ),
    ]
