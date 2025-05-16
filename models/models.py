# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gestion_etudiants(models.Model):
#     _name = 'gestion_etudiants.gestion_etudiants'
#     _description = 'gestion_etudiants.gestion_etudiants'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

