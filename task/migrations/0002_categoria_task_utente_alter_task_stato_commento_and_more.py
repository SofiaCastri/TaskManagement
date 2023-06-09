# Generated by Django 4.2.1 on 2023-05-26 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='utente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='stato',
            field=models.BooleanField(),
        ),
        migrations.CreateModel(
            name='Commento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testo', models.TextField()),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
                ('utente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Allegato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='allegati/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.categoria'),
        ),
    ]