{
    'name': 'Zapatos Proveedores',
    'version': '1.0',
    'summary': 'Extensión para administrar proveedores de zapatos',
    'category': 'Custom',
    'author': 'Isaac Campaña',
    'depends': ['zapatos'],
    'data': [
        'security/ir.model.access.csv',
        'views/proveedores_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}