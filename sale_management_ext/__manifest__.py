# -*- coding: utf-8 -*-
{
    'name': 'Sale Management Ext',
    'summary': 'Sale Management',
    'description': 'Sale Groups, Sale Teams , etc... management',
    'author': 'SHL MDG',
    'website': '',
    'category': 'sale',
    'version': '16.0.0.1',
    'depends': ['crm', 'inventory_management', 'account_management', 'crm_management_ext'],
    'data': [
        'data/ir_sequence_view.xml',
        'views/view_sales_group.xml',
        'views/view_sales_return_exchange.xml',
        'views/view_sales_team.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
}
