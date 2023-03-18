# Generated by Django 4.1.7 on 2023-03-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogArticle", "0002_alter_article_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.IntegerField(max_length=3)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("F", "Female"),
                            ("M", "Male"),
                            ("R", "Rather not say"),
                            ("C", "Custom"),
                        ],
                        max_length=1,
                    ),
                ),
                ("mobile_number", models.CharField(max_length=10)),
                ("user_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
