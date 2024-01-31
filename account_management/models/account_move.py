import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_type = fields.Selection([('open','Open'),('credit','Credit')], string='Payment Type')
    state = fields.Selection([('draft','Pending'),('proforma','Pro-forma'),('proforma2','Pro-forma'),('open','Open'),('paid','Paid'),('cancel','Cancelled')],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange', copy=False)
