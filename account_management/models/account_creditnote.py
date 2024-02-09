import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

class AccountCreditnote(models.Model):

    _name = 'account.creditnote'
    _description = 'Account Credit Note'

    name = fields.Char(string='Credit Note')