# -*- coding: utf-8 -*-
from odoo import http

# class Openacademy(http.Controller):
#       @http.route('/openacademy/openacademy/', auth='public')
#       def index(self, **kw):
#           return "Hello World"

#       @http.route('/openacademy/openacademy/objects/', auth='public')
#       def list(self, **kw):
#           return http.request.render('openacademy.listing', {
#               'root': '/openacademy/openacademy'
#               'objects': http.request.env['openacademy.openacademy'].search([])
#           })

#       @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>)
#       def object(self, object, **kw):
#           return http.request.render('openacademy.object', {
#               'object': obj
#           })