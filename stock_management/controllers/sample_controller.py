# -*- coding: utf-8 -*-

from odoo import http

class SampleController(http.Controller):

    @http.route('/sample', auth='public')
    def index(self, **kw):
        return 'Hello, World!'
