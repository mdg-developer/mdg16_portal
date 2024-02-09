# -*- coding: utf-8 -*-

import logging
from odoo import models, fields
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class ResTownship(models.Model):
    _name = 'res.township'

    name = fields.Char('Name')
    city_id = fields.Many2one(comodel_name='res.city', string='City')
