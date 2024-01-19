import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

class PreSaleOrder(models.Model):

    _name = 'pre.sale.order'
    _description = 'Pre Sale Order'

    name = fields.Char(string='Pre Sale Order Name')