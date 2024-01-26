# -*- coding: utf-8 -*-

from odoo import models, fields

class FleetVehicle(models.Model):

    _name = 'fleet.vehicle'
    _description = 'Fleet Vehicle'

    name = fields.Char(string='Fleet No')