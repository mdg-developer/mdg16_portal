# -*- coding: utf-8 -*-

import logging
from odoo import fields, models, api, _
from odoo.osv import expression,osv
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class StockGIN(models.Model):

    _name = 'stock.gin'
    _description = 'Good Issue Note'
    _order = 'id desc'
    _track = {
        'state': {
            'StockGIN.mt_note_confirm': lambda self, cr, uid, obj, ctx = None: obj.state in ['confirm'],
            'StockGIN.mt_note_approve': lambda self, cr, uid, obj, ctx = None: obj.state in ['approve']
        },
    }  

    @api.model
    def _get_default_company(self):
        company_id = self.env.user.company_id
        if not company_id:
            raise UserError(_('Error!'), _('There is no default company for the current user!'))
        return company_id.id

    name = fields.Char(string='GIN Ref', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('stock.gin'), readonly=True)
    request_id = fields.Many2one(comodel_name='stock.rfi', string='RFI Ref')
    to_location_id = fields.Many2one(comodel_name='stock.location', string='Requesting Location')
    from_location_id = fields.Many2one(comodel_name='stock.location', string='Request Warehouse')
    sale_team_id = fields.Many2one(comodel_name='crm.team', string='Delivery Team')
    issue_by = fields.Char(string='Issuer')
    request_by = fields.Many2one(comodel_name='res.users', string='Requested By')
    approve_by = fields.Many2one(comodel_name='res.users', string='Approved By')
    receiver = fields.Char(string='Receiver')
    internal_ref = fields.Char(string='Internal Ref')
    issue_date = fields.Date(string='Date For issue')
    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle No.')
    state = fields.Selection([('draft', 'Pending'),('approve', 'Approved'),('issue','Issued'),('cancel', 'Cancel'),('reversed', 'Reversed')], string='Status', default='draft')
    line_ids = fields.One2many(comodel_name='stock.gin.line', inverse_name='gin_id', string='Good Issue Note Line')
    company_id = fields.Many2one(comodel_name='res.company', default='_get_default_company', string='Company')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    is_return = fields.Boolean(string='is Return', default=False)
    is_issue_from_optional_location = fields.Boolean(string='Is Issue From Optional Location')
    reverse_date = fields.Date(string='Date for Reverse')
    reverse_user_id = fields.Many2one(comodel_name='res.users', string='Reverse user')
    sub_d_customer_id = fields.Many2one(comodel_name='sub.d.customer', string='Sub-D Customer')
    principle_id = fields.Many2one(comodel_name='product.principal', string='Principal')

    def action_approve(self):
        vals = {'state':'cancel','approve_by':self._uid}
        self.write(vals)
        return True
    
    def action_cancel(self):
        req_obj = self.env['stock.rfi']
        sale_order_obj = self.env['sale.order']
        req_ids = req_obj.search([('gin_id','=',self._ids[0])])
        for req_id in req_ids:
            for line in req_id.order_line_ids:
                so_name = line.name
                order_id = sale_order_obj.search([('name','=',so_name)])
                if order_id:
                    sale_order_obj.order_id.write(order_id.id,{'is_generate':False})
            req_obj.write(req_id.id,{'state':'cancel'})
        vals = {'state':'cancel'}
        self.write(vals)
        return True
    
    def action_reversed(self):
        vals = {'state':'reversed'}
        self.write(vals)
        return True

class StockGINLine(models.Model):

    _name = 'stock.gin.line'
    _description = 'Good Issue Note Line'

    name = fields.Char(string='GIN Line Ref')
    gin_id = fields.Many2one(comodel_name='stock.gin', string='Good Issue Note', ondelete='cascade', select=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    issue_quantity = fields.Float(string='Qty', digits=(16,0))
    approved_quantity = fields.Float(string='Approved Qty', digits=(16,0))
    product_uom_id = fields.Many2one(comodel_name='uom.uom', string='Product UOM')
    uom_ratio = fields.Char(string='UOM Ratio')
    batch_no = fields.Many2one(comodel_name='stock.lot',string='Batch No')
    expiry_date = fields.Date(string='Expiry Date')
    remark = fields.Char(string='Remark')
    big_uom_id = fields.Many2one(comodel_name='uom.uom', string='Bigger UOM')
    big_issue_quantity = fields.Float(string='Qty')
    qty_on_hand = fields.Float(string='Qty on Hand', digits=(16,0))
    sequence = fields.Integer(string='Sequence')
    opening_qty = fields.Float(string='Opening Qty', digits=(16,0))
    opening_product_uom_id = fields.Many2one(comodel_name='uom.uom', string='Opening UOM', digits=(16,0))
    is_checked = fields.Boolean(string='Is Checked')
    order_qty = fields.Float(string='Order Qty', digits=(16,0))
    ecommerce_qty = fields.Float(string='Ecommerce Qty', digits=(16,0))
    total_request_qty = fields.Float(string='Total Request Qty', digits=(16,0))

    




    




