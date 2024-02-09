# -*- coding: utf-8 -*-
{
    'name': 'address_management',
    'summary': 'All about Addresses',
    'description': 'All about Addresses',
    'author': 'SHL MDG',
    'website': '',
    'category': 'address, contact ext',
    'version': '16.0.0.1',
    'depends': ['base', 'contacts'],
    'data': [
        'views/view_res_township.xml',
        'views/view_res_city.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
