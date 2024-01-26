# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SampleWizard(models.TransientModel):
    _name = 'sample.wizard'

    name = fields.Char('Name')

    @api.multi
    def do_something(self):
        # Add your logic here
        pass
