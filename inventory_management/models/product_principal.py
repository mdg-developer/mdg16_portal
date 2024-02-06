# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductPrincipal(models.Model):
    _name = 'product.principal'
    _description = 'Product Principal'

    name = fields.Char(string='Description')
    code = fields.Char(string='Code', copy=False)
    property_account_receivable_id = fields.Many2one(comodel_name='account.account',
                                                  string='Cash Sale Clearing',
                                                  domain="[('account_type','=','asset_receivable')]")
    property_account_receivable_control_id = fields.Many2one(comodel_name='account.account',
                                                  string='Receivable Control',
                                                  domain="[('account_type','=','asset_receivable')]")
    property_account_foc_id = fields.Many2one(comodel_name='account.account',
                                                  string='Foc Account',
                                                  domain="[('account_type','=','income_other')]")
    property_account_discount_id = fields.Many2one(comodel_name='account.account',
                                                  string='Discount Account',
                                                  domain="[('account_type','=','income_other')]")
    property_account_receivable_clearing_id = fields.Many2one(comodel_name='account.account',
                                                  string='Receivable Clearing',
                                                  domain="[('account_type','=','asset_receivable')]")
    property_account_difference_id = fields.Many2one(comodel_name='account.account',
                                                  string='Price Difference Account')
    property_donation_account_id = fields.Many2one(comodel_name='account.account',
                                                  string='Donation Account')
    property_sampling_account_id = fields.Many2one(comodel_name='account.account',
                                                  string='Sampling Account')
    property_uses_account_id = fields.Many2one(comodel_name='account.account',
                                                  string='Uses Account')
    property_destruction_account_id = fields.Many2one(comodel_name='account.account',
                                                  string='Destruction Account')
    property_difference_receivable_account_id = fields.Many2one(comodel_name='account.account',
                                                domain="[('account_type','in', ('asset_receivable','payable'))]",
                                                string='Difference Receivable Account')
    property_difference_payable_account_id = fields.Many2one(comodel_name='account.account',
                                                domain="[('account_type','in', ('asset_receivable','payable'))]",
                                                string='Difference Payable Account')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Supplier')
    pricelist_id = fields.Many2one(comodel_name='product.pricelist', string='FOC Price List')
    property_trade_payable_account_id = fields.Many2one(comodel_name='account.account',
                                                domain="[('account_type','in', ('asset_receivable','payable'))]",
                                                string='Trade Payable Account')
    property_receivable_clearing_account_id = fields.Many2one(comodel_name='account.account',
                                                domain="[('account_type','in', ('asset_receivable','payable'))]",
                                                string='A/R Receivable Clearing Account')
    is_separate_transition = fields.Boolean(string='Is Separate Transition', default=False)
    is_skip_checking = fields.Boolean(string='Skip Checking in Tablet', default=False)
    is_active_two = fields.Boolean(string='Active Two', default=False)
