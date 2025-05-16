from odoo import models, fields


class Cours(models.Model):
    _name = "cours"
    _description = "Modèle Cours"

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")
    etudiant_ids = fields.Many2many("gestion.etudiant", string="Étudiants")
