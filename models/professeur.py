from odoo import models, fields


class Professeur(models.Model):
    _name = "professeur"
    _description = "Professeur"

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    email = fields.Char(string="Email")
    specialite = fields.Char(string="Spécialité")
    cours_ids = fields.One2many("cours", "professeur_id", string="Cours")


    _sql_constraints = [
        ("unique_email", "UNIQUE(email)", "L'email du professeur doit être unique!"),
        ("check_email_format", "CHECK(email LIKE '%@%' AND email LIKE '%.%')",
         "Le format de l'email du professeur semble incorrect."),
    ]
