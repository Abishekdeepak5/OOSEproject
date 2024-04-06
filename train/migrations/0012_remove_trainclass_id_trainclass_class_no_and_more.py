# Generated by Django 4.2.5 on 2024-04-06 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0011_remove_trainclass_class_pk_trainclass_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainclass',
            name='id',
        ),
        migrations.AddField(
            model_name='trainclass',
            name='class_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='train.classtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainclass',
            name='class_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]