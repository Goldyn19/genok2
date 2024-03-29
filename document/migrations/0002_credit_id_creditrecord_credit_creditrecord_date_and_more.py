# Generated by Django 4.2.3 on 2023-07-13 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cart_id_is_attended'),
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_ID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=125)),
                ('customer_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='creditrecord',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='creditrecord',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditrecord',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.cart_id'),
        ),
        migrations.AddField(
            model_name='creditrecord',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='document.credit_id'),
        ),
    ]
