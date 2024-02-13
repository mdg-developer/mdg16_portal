import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class SalesTeam(models.Model):

    _inherit = 'crm.team'

    sale_group_id = fields.Many2one(comodel_name='sales.group', string='Sales Group')
    sales_person_id = fields.Many2one(comodel_name='sales.person', string='Sales Person')
    sales_supervisor_id = fields.Many2one(comodel_name='sales.supervisor', string='Sales Supervisor')
    sales_manager_id = fields.Many2one(comodel_name='sales.manager', string='Sales Manager')
    join_date = fields.Date(string='Join Date')
    location_id = fields.Many2one('stock.location', string='Location')
    normal_return_location_id = fields.Many2one(comodel_name='stock.location', string='Normal Return Location')
    exp_location_id = fields.Many2one(comodel_name='stock.location', string='Expiry Location')
    near_exp_location_id = fields.Many2one(comodel_name='stock.location', string='Near Expiry Location')
    fresh_stock_not_good_location_id = fields.Many2one(comodel_name='stock.location', string='Fresh Stock Minor Damage Location')
    damage_location_id = fields.Many2one(comodel_name='stock.location', string='Damage location')

class SalesPerson(models.Model):
    _name = 'sales.person'
    _description = 'Sales Person'

    name = fields.Char(string='Salesperson Name')
    branch_id = fields.Many2one(comodel_name='res.branch', string='Branch')
    active = fields.Boolean(string='Active', default=True)

class SalesSupervisor(models.Model):
    _name = 'sales.supervisor'
    _description = 'Sales Supervisor'

    name = fields.Char('Sales Supervisor Name')
    branch_ids = fields.Many2many('res.branch', 'sales_supervisor_branch_rel',
                                  'sales_supervisor_id', 'branch_id', string='Branch')
    sales_team_ids = fields.One2many('crm.team', 'sales_supervisor_id', string='Sales Teams')
    active = fields.Boolean(string='Active', default=True)

class SalesManager(models.Model):
    _name = 'sales.manager'
    _description = 'Sales Manager'

    name = fields.Char('Sales Manager Name')
    branch_ids = fields.Many2many('res.branch', 'sales_manager_branch_rel', 'sales_manager_id', 'branch_id', string='Branch')
    sales_team_ids = fields.One2many('crm.team', 'sales_manager_id', string='Sales Teams')
    active = fields.Boolean('Active', default=True)



