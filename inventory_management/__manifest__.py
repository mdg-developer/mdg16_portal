# -*- coding: utf-8 -*-
{
    'name': 'inventory_management',
    'summary': 'Products and related customization',
    'description': 'Products and related customization',
    'author': 'SHL MDG',
    'website': 'www.myanmardistributiongroup.com',
    'category': 'general/inventory',
    'version': '16.0.0.1',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_product_principal.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
