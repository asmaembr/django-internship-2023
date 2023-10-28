# Generated by Django 4.2.3 on 2023-07-26 22:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('num_activite', models.CharField(max_length=10)),
                ('type_activite', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('compteur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('num_agence', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_agence', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('matricule', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_complet', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('num_agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.agence')),
            ],
        ),
        migrations.CreateModel(
            name='Expediteur',
            fields=[
                ('num_expediteur', models.AutoField(primary_key=True, serialize=False)),
                ('type_expediteur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('num_Panier', models.AutoField(primary_key=True, serialize=False)),
                ('prix_ht', models.DecimalField(decimal_places=2, max_digits=8)),
                ('prix_ttc', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(max_length=100)),
                ('tva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('num_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.agent')),
            ],
        ),
        migrations.CreateModel(
            name='PrixBoiteReexpedition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois_abonnement', models.CharField(default=None, max_length=10)),
                ('prix', models.DecimalField(decimal_places=3, max_digits=8)),
                ('type_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.activite')),
                ('type_expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.expediteur')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('code_postale', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_ville', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reexpedition',
            fields=[
                ('num_reexp', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adresse_nouvelle', models.CharField(max_length=100)),
                ('adresse_actuelle', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('piece_identite', models.CharField(max_length=100)),
                ('code_postale', models.IntegerField()),
                ('nom_ville', models.CharField(max_length=20)),
                ('num_tel_exp', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.agent')),
                ('mois_abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reexpedition_mois_abonnement', to='playground.prixboitereexpedition')),
                ('num_panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.panier')),
                ('type_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.activite')),
                ('type_expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reexpedition_type_expediteur', to='playground.prixboitereexpedition')),
            ],
        ),
        migrations.CreateModel(
            name='Recu',
            fields=[
                ('num_recu', models.IntegerField(primary_key=True, serialize=False)),
                ('num_panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.panier')),
            ],
        ),
        migrations.CreateModel(
            name='PrixColisCourrier',
            fields=[
                ('custom_id', models.CharField(default=1, max_length=10, primary_key=True, serialize=False)),
                ('poids_inf', models.DecimalField(decimal_places=3, max_digits=5)),
                ('poids_sup', models.DecimalField(decimal_places=3, max_digits=5)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('type_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Courrier',
            fields=[
                ('num_courrier', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adresse_destinataire', models.CharField(max_length=100)),
                ('email_dest', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('email_exped', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('piece_identite', models.CharField(max_length=100)),
                ('code_postale', models.IntegerField()),
                ('nom_ville', models.CharField(max_length=20)),
                ('poids_inf', models.DecimalField(decimal_places=3, max_digits=5)),
                ('poids_sup', models.DecimalField(decimal_places=3, max_digits=5)),
                ('num_tel_exp', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.agent')),
                ('num_panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.panier')),
                ('type_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.activite')),
                ('type_expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.prixcoliscourrier')),
            ],
        ),
        migrations.CreateModel(
            name='Colis',
            fields=[
                ('num_colis', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adresse_destinataire', models.CharField(max_length=100)),
                ('email_dest', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('email_exped', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('piece_identite', models.CharField(max_length=100)),
                ('code_postale', models.IntegerField()),
                ('nom_ville', models.CharField(max_length=20)),
                ('poids_inf', models.DecimalField(decimal_places=3, max_digits=5)),
                ('poids_sup', models.DecimalField(decimal_places=3, max_digits=5)),
                ('num_tel_exp', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.agent')),
                ('num_panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.panier')),
                ('type_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.activite')),
                ('type_expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.prixcoliscourrier')),
            ],
        ),
        migrations.CreateModel(
            name='BoitePostale',
            fields=[
                ('num_boite', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adresse_client', models.CharField(max_length=100)),
                ('email_client', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('piece_identite', models.CharField(max_length=100)),
                ('nom_client', models.CharField(max_length=100)),
                ('code_postale', models.IntegerField()),
                ('nom_ville', models.CharField(max_length=20)),
                ('num_tel_exp', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.agent')),
                ('mois_abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boitepostale_mois_abonnement', to='playground.prixboitereexpedition')),
                ('num_panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.panier')),
                ('type_activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boitepostale_type_activite', to='playground.prixboitereexpedition')),
                ('type_expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boitepostale_type_expediteur', to='playground.prixboitereexpedition')),
            ],
        ),
        migrations.AddField(
            model_name='agence',
            name='code_postal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.ville'),
        ),
        migrations.AddConstraint(
            model_name='prixcoliscourrier',
            constraint=models.UniqueConstraint(fields=('type_activite', 'poids_inf', 'poids_sup'), name='prix_colis_courrier_unique_constraint'),
        ),
        migrations.AddConstraint(
            model_name='prixboitereexpedition',
            constraint=models.UniqueConstraint(fields=('type_activite', 'mois_abonnement', 'type_expediteur'), name='prix_boite_reexpedition_unique_constraint'),
        ),
    ]
