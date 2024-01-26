# -*- coding: utf-8 -*-
{
    'name': 'stock_management',
    'summary': 'Manage all Stock Transfering, Stock Requisition, Stock Receiving.',
    'description': 'Manage all Stock Transfering, Stock Requisition, Stock Receiving.',
    'author': 'SHL MDG',
    'website': 'www.myanmardistributiongroup.com',
    'category': 'General/Stock',
    'version': '16.0.0.1',
    'depends': ['base','stock','inventory_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_stock_rfi.xml',
        'views/view_stock_gin.xml',
        'data/ir_sequence_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
