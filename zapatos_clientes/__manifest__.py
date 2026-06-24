{
    'name': 'zapatos_clientes',
    'version': '1.0',
    'summary': 'Modulo de registro y gestion de clientes para zapateria',
    'description': 'Modulo hijo para el registro y administracion de clientes que interactuan con la tienda de zapatos.',
    'author': 'Ander',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['zapatos'],
    'data': [
        'security/ir.model.access.csv',
        'views/zapatos_clientes_views.xml',
    ],
    'installable': True,
    'application': True,
}
