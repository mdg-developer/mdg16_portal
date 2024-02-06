import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    sale_group_id = fields.Many2one('sales.group', string='Sale Group')

class SalesGroup(models.Model):
    _name = 'sales.group'

    name = fields.Char('Name')
    principal_ids = fields.Many2many('product.principal', 'product_sale_group_principal_rel',
                                     'sale_group_id', 'principal_id', string='Principals')
    product_ids = fields.Many2many('product.product', 'product_sale_group_rel',
                                   'sale_group_id', 'product_id', string='Products')
    sale_team_ids = fields.One2many('crm.team', 'sale_group_id', string='Sales Teams')
    note = fields.Text(string='Note')
