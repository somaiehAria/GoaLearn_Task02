# Generated by Django 4.1.5 on 2023-03-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogArticle", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ManyToManyField(
                related_name="articles", to="BlogArticle.category"
            ),
        ),
    ]