# Generated by Django 4.2.1 on 2023-06-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_stato_alter_task_stato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Da fare', 'da fare'), ('In corso', 'In corso'), ('Fatto', 'Fatto')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='stato',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Allegato',
        ),
        migrations.DeleteModel(
            name='Stato',
        ),
    ]
