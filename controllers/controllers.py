# -*- coding: utf-8 -*-
# from odoo import http


# class GestionEtudiants(http.Controller):
#     @http.route('/gestion_etudiants/gestion_etudiants', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_etudiants/gestion_etudiants/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_etudiants.listing', {
#             'root': '/gestion_etudiants/gestion_etudiants',
#             'objects': http.request.env['gestion_etudiants.gestion_etudiants'].search([]),
#         })

#     @http.route('/gestion_etudiants/gestion_etudiants/objects/<model("gestion_etudiants.gestion_etudiants"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_etudiants.object', {
#             'object': obj
#         })

