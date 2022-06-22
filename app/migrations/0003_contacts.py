

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_profile_caption_alter_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('m_number', models.IntegerField(default=0)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.neighborhood')),
            ],
        ),
    ]
