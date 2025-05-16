from odoo import models, fields


class Etudiant(models.Model):
    _name = 'gestion.etudiant'
    _description = 'Modèle étudiant'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')

    num_etudiant = fields.Char(
        string='Numéro étudiant',
        required=True,
        unique=True
    )

    sexe = fields.Selection(
        selection=[
            ('homme', 'Homme'),
            ('femme', 'Femme'),
            ('autre', 'Autre')
        ],
        string='Sexe',
        default='homme'  # Valeur par défaut
    )
