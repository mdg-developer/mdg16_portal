# -*- coding: utf-8 -*-
{
    'name': 'connector_ext',
    'summary': 'Connector Extension',
    'description': 'Connector Extension',
    'author': 'SHL MDG',
    'website': '',
    'category': '',
    'version': '16.0.0.1',
    'depends': ['base', 'connector'],
    'data': [
        'views/view_queue_job.xml',
        'security/ir.model.access.csv',
        'wizards/view_connector_wizard.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
