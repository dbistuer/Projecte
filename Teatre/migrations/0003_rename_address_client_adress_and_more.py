# Generated by Django 4.0.3 on 2022-03-19 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Teatre', '0002_alter_client_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='address',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='idCinema',
            new_name='Cinema',
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('number', 'Cinema')},
        ),
    ]