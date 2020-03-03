# Generated by Django 3.0.3 on 2020-03-03 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('progress', models.FloatField()),
                ('aligned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Goal')),
            ],
        ),
    ]