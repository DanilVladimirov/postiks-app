# Generated by Django 3.2.4 on 2021-07-15 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("postsapp", "0002_alter_post_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comments",
            old_name="publication",
            new_name="post",
        ),
    ]
