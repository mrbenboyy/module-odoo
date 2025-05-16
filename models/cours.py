from odoo import api, models, fields, _
from odoo.exceptions import ValidationError
from datetime import date


class Cours(models.Model):
    _name = "cours"
    _description = "Modèle Cours"

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")
    etudiant_ids = fields.Many2many("gestion.etudiant", string="Étudiants")
    code = fields.Char(string="Code", required=True, unique=True)
    credits = fields.Integer(string="Crédits")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    professeur_id = fields.Many2one("professeur", string="Professeur")
    niveau = fields.Selection([
        ("debutant", "Débutant"),
        ("intermediaire", "Intermédiaire"),
        ("avance", "Avancé")
    ], default="debutant")
    actif = fields.Boolean(string="Actif", default=True)
    duree_totale = fields.Integer(string="Durée (jours)", compute="_compute_duree", store=True)

    @api.depends("date_debut", "date_fin")
    def _compute_duree(self):
        for record in self:
            if record.date_debut and record.date_fin:
                record.duree_totale = (record.date_fin - record.date_debut).days
            else:
                record.duree_totale = 0

    _sql_constraints = [
        ("unique_code", "UNIQUE(code)", "Le code du cours doit être unique !")
    ]
