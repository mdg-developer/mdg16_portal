# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductPrincipal(models.Model):
    _name = 'product.principal'

    name = fields.Char('Name')
