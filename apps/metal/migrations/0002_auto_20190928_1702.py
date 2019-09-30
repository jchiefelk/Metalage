# Generated by Django 2.2.5 on 2019-09-28 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementTraceAssay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_method', models.CharField(blank=True, max_length=50, null=True)),
                ('iron_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('arsenic_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('copper_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('silver_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('gold_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('chromium_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('zinc_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('cobalt_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('nickel_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('antimony_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('sulfur_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('bismuth_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('cadmium_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('indium_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('manganese_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('lead_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('selenium_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('tellurium_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('tin_ppm', models.CharField(blank=True, max_length=50, null=True)),
                ('iron_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('arsenic_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('copper_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('silver_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('gold_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('chromium_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('zinc_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('cobalt_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('nickel_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('antimony_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('sulfur_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('bismuth_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('cadmium_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('indium_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('manganese_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('lead_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('selenium_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('tellurium_percent', models.CharField(blank=True, max_length=50, null=True)),
                ('tin_percent', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='metal',
            old_name='analysis_method',
            new_name='time_period',
        ),
        migrations.AddField(
            model_name='metal',
            name='element_trace_assay_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='metal.ElementTraceAssay'),
        ),
    ]
