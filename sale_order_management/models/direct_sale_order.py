import logging
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

PAYMENT_TYPE = [
    ('credit', 'Credit'),
    ('cash', 'Cash'),
    ('consignment', 'Consignment'),
    ('advanced', 'Advanced')
]

DELIVERY_REMARK = [
                ('partial', 'Partial'),
                ('delivered', 'Delivered'),
                ('none', 'None')
            ]

VOID = [
    ('voided', 'Voided'),
    ('none', 'Unvoid')
]

STATE = [
    ('draft', 'Draft'),
('done', 'Complete')
]

class OutletType(models.Model):

    _name = 'outlet.type'
    _description = 'Outlet Type'

    name = fields.Char(string='Outlet Type')

class DirectSaleOrder(models.Model):

    _name = 'direct.sale.order'
    _description = 'Direct Sale Order'

    name = fields.Char('Order Reference', size=64)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', copy=True)
    customer_code = fields.Char( string='Customer Code', copy=True)
    outlettype_id = fields.Many2one(comodel_name='outlet.type', string='Outlet Type', copy=True)
    user_id = fields.Many2one(comodel_name='res.users', string='Salesman Name', copy=True)
    sale_plan_name = fields.Char('Sale Plan Name', copy=True)
    latitude = fields.Float('Geo Latitude', copy=True)
    longitude = fields.Float('Geo Longitude', copy=True)
    amount_total = fields.Float('Amount Total', copy=True)
    payment_type = fields.Selection(PAYMENT_TYPE, string='Payment Type', copy=True)
    delivery_remark = fields.Selection(DELIVERY_REMARK, string='Delivery Remark', copy=True)
    additional_discount = fields.Float(string='Additional Discount', copy=True)
    deduction_amount = fields.Float(string='Deduction Amount', copy=True)
    net_amount = fields.Float(string='Net Amount', copy=True)
    change_amount = fields.Float(string='Change Amount', copy=True)
    remaining_amount = fields.Float(string='Remaining Amount', copy=True)
    balance = fields.Float(string='Balance', copy=True)
    paid_amount = fields.Float(string='Paid Amount', copy=True)
    is_paid = fields.Boolean(string='Is Paid', copy=True)
    void = fields.Selection(VOID, string='Void', copy=True)
    date = fields.Datetime(string='Date', copy=True)
    note = fields.Text('Note', copy=True)
    order_line_ids = fields.One2many(comodel_name='direct.sale.order.lines', inverse_name ='order_id', string='Order Lines', copy=True)
    delivery_order_ids = fields.One2many(comodel_name='product.delivery.order', inverse_name ='order_id', string='Delivery Order Lines', copy=True)
    tablet_id = fields.Many2one(comodel_name='tablet.information', string='Tablet Information')
    sale_plan_day_id = fields.Many2one(comodel_name='sale.plan.day', string='Sale Plan Day')
    sale_plan_trip_id = fields.Many2one(comodel_name='sale.plan.trip', string='Sale Plan Trip')
    warehouse_id = fields.Many2one(comodel_name='stock.warehouse', string='Warehouse')
    sale_team_id = fields.Many2one(comodel_name='crm.team', string='Sale Team')
    location_id = fields.Many2one(comodel_name='stock.location', string='Stock Location')
    state = fields.Selection(STATE,string='Status')
    due_date = fields.Date(string='Due Date')
    payment_term_id = fields.Many2one(comodel_name='account.payment.term', string='Payment Term')
    promotion_ids = fields.One2many(comodel_name='promotion.lines', inverse_name='order_id', string='Promotions')
    pricelist_id = fields.Many2one(comodel_name='product.pricelist', string='Pricelist')
    payment_line_ids = fields.One2many(comodel_name='account.payment', inverse_name='order_id', string='Payment Lines')
    # branch_id = fields.Many2one(comodel_name='res.branch', string='Branch')
    is_convert = fields.Boolean(string='Is Convert')
    unvoid_reprint_count = fields.Integer(string='Unvoid Reprint Count')
    void_reprint_count = fields.Integer(string='void Reprint Count')
    order_team = fields.Many2one(comodel_name='crm.team', string='Order Team')
    is_rebate_later = fields.Boolean(string='Is Rebate Later')
    sale_person_id = fields.Many2one(comodel_name='res.users', string='Sale Person')
    pre_sale_order_id = fields.Many2one(comodel_name='pre.sale.order', string='Pre Sale Order')
    revise_reason_id = fields.Many2one(comodel_name='revise.reason', string='Revise Reason')
    cancel_reason_id = fields.Many2one(comodel_name='cancel.reason', string='Cancel Reason')
    payment_ref = fields.Char(string='Payment Reference')

class DirectSaleOrderLines(models.Model):
    
    _name = 'direct.sale.order.lines'
    _description = 'Direct Sale order Lines'

    name = fields.Char(string='Order Line Reference', copy=True)
    product_type = fields.Char(string='Product Type', copy=True)
    product_id = fields.Many2one(comodel_name='product.template', string='Products', copy=True)
    product_uos_qty = fields.Float(string='Quantity', copy=True)
    uom_id = fields.Many2one(comodel_name='product.uom', string='Product UOM', copy=True)
    prict_unit = fields.Float(string='Unit Price', copy=True)
    discount = fields.Float(string='Discount (%)', copy=True)
    discount_amt = fields.Float(string='Discount (Amount)', copy=True)
    order_id = fields.Many2one(comodel_name='direct.sale.order', string='Sale Order', copy=True)
    sub_total = fields.Float('Sub Total', copy=True)
    is_foc = fields.Boolean('Is FOC', copy=True)
    is_manual_foc = fields.Boolean('Is Manual FOC', copy=True)
    promotion_id = fields.Many2one(comodel_name='promos.rules', string='Promotion', readonly=True, copy=True)

class ProductDeliveryOrder(models.Model):

    _name = 'product.delivery.order'
    _description = 'Product Delivery Order'

    product_id = fields.Many2one(comodel_name='product.product', string='Products')
    uom_id = fields.Many2one(comodel_name='product.uom', string='UOM')
    product_qty = fields.Float(string='Product Quantity')
    product_qty_to_deliver = fields.Float(string='Quantity to Deliver')
    order_id = fields.Many2one(comodel_name='direct.sale.order', string='Sale Order')

class PromotionLines(models.Model):
    
    _name = 'promotion.lines'
    _description = 'Promotion Lines'

    name = fields.Char(string='Promotion Line Name')
    order_id = fields.Many2one(comodel_name='direct.sale.order', string='Sale Order')
    
class AccountPayment(models.Model):

    _inherit = 'account.payment'

    order_id = fields.Many2one(comodel_name='direct.sale.order', string='Sale Order')

class ReviseReason(models.Model):

    _name = 'revise.reason'
    _description = 'Revise Reason'

    name = fields.Char(string='Revise Reason')

class CancelReason(models.Model):

    _name = 'cancel.reason'
    _description = 'Cancel Reason'

    name = fields.Char(string='Cancel Reason')

class PaymentType(models.Model):

    _name = 'account.payment.type'
    _description = 'Account Payment Type'

    name = fields.Char(string='Payment Type')


