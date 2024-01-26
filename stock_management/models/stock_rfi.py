# -*- coding: utf-8 -*-

import logging
from odoo import fields, models, api, _
from odoo.osv import expression,osv
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

STATE = [
    ('draft', 'Draft'),
    ('approve', 'Approved'),
    ('cancel', 'Cancel'),
    ('reversed', 'Reversed'),
]

class StockRFI(models.Model):

    _name = 'stock.rfi'
    _description = 'Stock RFI'

    def _default_request_date(self):
        vals = fields.datetime.now
        return vals
    
    def _default_from_date(self):
        vals = fields.datetime.now
        return vals
    
    def _default_to_date(self):
        vals = fields.datetime.now
        return vals

    def _default_request_by(self):
        return self._uid
    
    def _get_default_company(self):
        company_id = self.env.user.company_id
        if not company_id:
            raise osv.except_osv(_('Error!'), _('There is no default company for the current user!'))
        return company_id

    def _get_default_sub_d_customer(self):
        sub_d_customer_id = self.env['sub.d.customer'].search([('name', '=', 'None')])
        if sub_d_customer_id:
            return sub_d_customer_id.id

    name = fields.Char(string='RFI Reference', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('stock.rfi'), readonly=True)
    delivery_team_id = fields.Many2one(comodel_name='crm.team', string='Delivery Team', required=True)
    from_location_id = fields.Many2one(comodel_name='stock.location', string='From Location')
    to_location_id = fields.Many2one(comodel_name='stock.location', string='To Location')
    sale_order_no = fields.Char(string='Sales Order/Inv Ref; No')
    receiver = fields.Char(string='Receiver')
    request_by = fields.Many2one(comodel_name='res.users', string='Request By', default=lambda self: self._default_request_by(),readonly=True)
    approve_by = fields.Many2one(comodel_name='res.users', string='Approve By', readonly=True)
    request_date = fields.Date(string='Date Requested')
    rfi_from_date = fields.Date(string='Order Date From')
    rfi_to_date = fields.Date(string='Order Date To')
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle No.')
    state = fields.Selection(STATE, string='Status', copy='False', default='draft')
    stock_rfi_line_ids = fields.One2many(comodel_name='stock.rfi.lines', inverse_name='rfi_id', string='RFI Lines', copy=True)
    company_id = fields.Many2one(comodel_name='res.company', default=lambda self: self._get_default_company(),string='Company')
    order_line_ids = fields.One2many(comodel_name='stock.rfi.order', inverse_name='rfi_id', string='Sale Order Lines', copy=True)
    is_pre_rfi = fields.Boolean(string='Is Pre RFI')
    is_direct_rfi = fields.Boolean(string='Is Direct RFI')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    gin_id = fields.Many2one(comodel_name='stock.gin', string='GIN No')
    is_issue_from_optional_location = fields.Boolean(string='Is Issue From Optional Location')
    sub_d_customer_id = fields.Many2one(comodel_name='sub.d.customer', default=lambda self: self._get_default_sub_d_customer(),string='Sub-D Customer')
    principal_id = fields.Many2one(comodel_name='product.principal', string='Principal')

    def create(self, vals):

        rfi_code = self.env['ir.sequence'].get('request.code') or '/'
        vals.update({})

        return super(StockRFI, self).create(vals)

    def action_cancel(self):
        vals = {'state':'cancel'}
        self.write(vals)
        return True

    def action_approve(self):
        vals = {'state':'approve'}
        self.write(vals)
        return True
    
    def action_reversed(self):
        vals = {'state':'reversed'}
        self.write(vals)
        return True
    
class StockRFILines(models.Model):

    _name = 'stock.rfi.lines'
    _description = 'Stock RFI Lines'

    name = fields.Char(string='Line No')
    rfi_id = fields.Many2one(comodel_name='stock.rfi', string='Stock RFI')
    is_pre_rfi = fields.Boolean(related='rfi_id.is_pre_rfi', string='Is Pre RFI')
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    req_quantity = fields.Float(string='Request Quantity', digits=(16, 0))
    uom_id = fields.Many2one(comodel_name='uom.uom', string='Product UOM')
    uom_ratio = fields.Char(string='UOM Ratio')
    remark = fields.Char(string='Remark')
    big_uom_id = fields.Many2one(comodel_name='uom.uom', string='Bigger UOM')
    big_req_quantity = fields.Float(string='Bigger UOM Req Qty', digits=(16, 0))
    sale_req_quantity = fields.Float(string='Small UOM Req Qty', digits=(16, 0))
    additional_req_quantity = fields.Float(string='Small Add Qty', digits=(16, 0))
    qty_on_hand = fields.Float(string='Qty On Hand', digits=(16, 0))
    sequence = fields.Integer(string='Sequence')
    order_qty = fields.Float(string='Order Qty', digits=(16, 0))
    ecommerce_qty = fields.Float(string='Ecommerce Qty', digits=(16, 0))
    
class StockRequisitionOrder(models.Model):
    
    _name = 'stock.rfi.order'
    _description = 'Stock RFI Order'

    name = fields.Char(string='Order No')
    rfi_id = fields.Many2one(comodel_name='stock.rfi', string='Stock RFI')
    ref_no = fields.Char(string='Order Reference')
    amount = fields.Float(string='Amount')
    date = fields.Date(string='Date')
    sale_team_id = fields.Many2one(comodel_name='crm.team', string='Sales Team')
    state = fields.Selection([
            ('draft', 'Draft Quotation'),
            ('sent', 'Quotation Sent'),
            ('cancel', 'Cancelled'),
            ('waiting_date', 'Waiting Schedule'),
            ('progress', 'Sales Order'),
            ('manual', 'Sale to Invoice'),
            ('shipping_except', 'Shipping Exception'),
            ('invoice_except', 'Invoice Exception'),
            ('done', 'Done'),
            ], string='Status')

class SubDCustomer(models.Model):

    _name = 'sub.d.customer'
    _description = 'Sub D Customer'

    name = fields.Char(string='Sub D Customer')

