import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

class SalesTransactions(models.Model):

    _name = 'sales.transactions'
    _description = 'Sales Transactions'

    name = fields.Char(string='SEN No')
    transaction = fields.Char('ID')
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    invoice_id = fields.Many2one(comodel_name='account.move', string='Invoice')
    customer_code = fields.Char(related='customer_id.customer_code', string='Customer Code')
    team_id = fields.Many2one(comodel_name='crm.team', string='Sale Team')
    date = fields.Datetime(string='Date')
    type = fields.Selection([('exchange', 'Exchange'), ('sale_return', 'Sale Return'),('sale_return_with_credit_note', 'Sale Return with Credit Note')], string='Type')
    line_ids = fields.One2many(comodel_name='sales.transactions.lines', inverse_name='transaction_id', string='Items Lines')
    void_flag = fields.Selection([('none','None'),('voided','Cancel')], string='Void Status')
    location_id = fields.Many2one(related='team_id.location_id', comodel_name='stock.location', string='Location')
    state = fields.Selection([('draft', 'Draft'),('done', 'Complete')],string='Status', default='draft')
    note = fields.Text(string='Note')
    location_type = fields.Selection([('normal_stock_returned', 'Normal stock returned'), ('expired', 'Expired'), ('near_expiry', 'Near expiry'),
             ('fresh_stock_minor_damage', 'Fresh stock minor damage'), ('damaged', 'Damaged')], string='Location Type')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    latitude = fields.Float(string='Geo Latitude')
    longitude = fields.Float(string='Geo Longitude')
    distance_status = fields.Char(string='Distance Status')
    geo_point = fields.Char(string='Geo Point')
    township_id = fields.Many2one(comodel_name='res.township', string='Township')
    total_value = fields.Float(string='Value Of Out')
    pricelist_id = fields.Many2one(comodel_name='product.pricelist', string='Product Pricelist')
    ams_total = fields.Float(string='3AMS Total')
    out_ams_percent = fields.Float(string='% Out on AMS')
    ams_budget_total = fields.Float(string='Budget')
    month_out_todate = fields.Float(string='Month To Date Out')
    balance_total = fields.Float(string='Balance')
    credit_note_id = fields.Many2one(comodel_name='account.creditnote', string='Credit Note')
    branch_id = fields.Many2one(comodel_name='res.branch', string='Branch')

    @api.model
    def create(self, vals):
        id_code = self.env['ir.sequence'].get('product.transaction.code') or '/'
        vals['name'] = id_code
        return super(SalesTransactions, self).create(vals)

    @api.onchange('location_type')
    def onChangeLocationType(self):
        if self.team_id:
            if self.location_type == 'normal_stock_returned':
                self.location_id = self.team_id.normal_return_location_id.id
            elif self.location_type == 'expired':
                self.location_id = self.team_id.exp_location_id.id
            elif self.location_type == 'near_expiry':
                self.location_id = self.team_id.near_exp_location_id.id
            elif self.location_type == 'fresh_stock_minor_damage':
                self.location_id = self.team_id.fresh_stock_not_good_location_id.id
            elif self.location_type == 'damaged':
                self.location_id = self.team_id.damage_location_id.id

    def action_create_invoice(self):
        line_obj = self.env['sales.transactions.lines']
        invoice_line_obj = self.env['account.invoice.line']
        invoice_obj = self.env['account.invoice']

class SalesTransactionsLines(models.Model):

    _name = 'sales.transactions.lines'
    _description = 'Sales Transactions Lines'

    name = fields.Char(string='Sales Transactions Lines')
    transaction_id = fields.Many2one(comodel_name='sales.transactions', string='Sales Transactions')
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    uom_id = fields.Many2one(comodel_name='uom.uom', string='UOM')
    product_qty = fields.Integer(string='Qty')
    so_no = fields.Char(string='SO Reference')
    trans_type = fields.Selection([('In', 'In'), ('Out', 'Out')], string='Type')
    transaction_name = fields.Char(string='Transaction Name')
    note = fields.Char(string='Note')
    exp_date = fields.Date(string='Expired Date')
    batch_no = fields.Char(string='Batch No')
    total_price = fields.Float(string='Value')

