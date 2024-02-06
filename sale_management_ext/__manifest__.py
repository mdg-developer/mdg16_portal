# -*- coding: utf-8 -*-
{
    'name': 'Sale Management Ext',
    'summary': 'Sale Management',
    'description': 'Sale Groups, Sale Teams , etc... management',
    'author': 'SHL MDG',
    'website': '',
    'category': 'sale',
    'version': '16.0.0.1',
    'depends': ['crm', 'inventory_management'],
    'data': [
        'views/view_sale_group.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
}
