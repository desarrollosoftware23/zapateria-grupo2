{
    "name": "Zapatos - Envíos",
    "version": "18.0.1.0.0",
    "summary": "Gestión de envíos de zapatos",
    "description": """
Módulo para administrar los envíos de zapatos vendidos.
Permite registrar envíos, controlar estados, transportistas,
fechas de entrega y relacionar clientes con los envíos.
    """,
    "author": "Alejo",
    "category": "Sales",
    "license": "LGPL-3",

    "depends": [
        "base",
        "zapatos",
        "zapatos_clientes",
        "zapatos_ventas",
    ],

    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/envio_views.xml",
        "views/menu.xml",
    ],

    "application": False,
    "installable": True,
}

