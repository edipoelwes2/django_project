# Generated by Django 2.2.4 on 2019-08-11 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_sportnews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SportNews',
            new_name='Esporte',
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='Novidades',
        ),
        migrations.RenameField(
            model_name='esporte',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='esporte',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='esporte',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='novidades',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='novidades',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='novidades',
            old_name='title',
            new_name='titulo',
        ),
    ]
