# Generated by Django 5.0.3 on 2024-04-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_noticia_sub_titulo_alter_noticia_autora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.CharField(max_length=200),
        ),
    ]
