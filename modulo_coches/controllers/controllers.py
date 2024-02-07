# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCoches(http.Controller):
#     @http.route('/modulo_coches/modulo_coches/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_coches/modulo_coches/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_coches.listing', {
#             'root': '/modulo_coches/modulo_coches',
#             'objects': http.request.env['modulo_coches.modulo_coches'].search([]),
#         })

#     @http.route('/modulo_coches/modulo_coches/objects/<model("modulo_coches.modulo_coches"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_coches.object', {
#             'object': obj
#         })
