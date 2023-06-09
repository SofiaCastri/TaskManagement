# Generated by Django 4.2.1 on 2023-06-02 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_categoria_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Da fare', 'da Fare'), ('In corso', 'In corso'), ('Fatto', 'Fatto')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='stato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.stato'),
        ),
    ]
