import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

class SalePlanDay(models.Model):

    _name = 'sale.plan.day'
    _description = 'Sale Plan Day'

    name = fields.Char(string='Sale Plan Name')