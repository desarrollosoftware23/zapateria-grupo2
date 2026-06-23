{
    'name': 'Zapatos Ventas',
    'version': '1.0',
    'summary': 'Registro y control de las ventas realizadas sobre los productos del módulo principal',
    'depends': ['base', 'zapatos'],
    'data': [
        'security/ir.model.access.csv',
        'views/zapatos_ventas_views.xml',
    ],
    'installable': True,
    'application': True,
}