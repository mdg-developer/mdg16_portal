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

class ResUsers(models.Model):

    _inherit = 'res.users'

    is_subscribe_job = fields.Boolean(string='Jobs Notification',
                                      default=True,
                                      help='If this flag is checked and the'
                                           ' user is Connector Manager, he will'
                                           ' receive job notifications.',
                                      select=True)