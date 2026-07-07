# -*- coding: utf-8 -*-
{
    'name': 'Phone Call Notes',
    'version': '1.0',
    'summary': 'Log phone calls and notes directly from Contacts.',
    'category': 'Sales',
    'author': 'Antigravity',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/phone_call_wizard_views.xml',
        'views/phone_call_log_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'phone_call_notes/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
