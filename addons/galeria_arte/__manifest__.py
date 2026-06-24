# -*- coding: utf-8 -*-
{
    'name': 'Galería de Arte',
    'version': '1.0',
    'summary': 'Gestión de piezas de arte para la universidad',
    'category': 'Custom',
    'author': 'Isaac Campaña',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/exposicion_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}