# Generated by Django 5.1.3 on 2024-11-30 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0002_rename_ricao_produtos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produtos', verbose_name='Produto')),
            ],
        ),
    ]
