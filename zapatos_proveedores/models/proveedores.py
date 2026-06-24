from odoo import models, fields

class ZapateriaProveedor(models.Model):
    _name = 'zapateria.proveedor'
    _description = 'Proveedores de la Zapatería'

    # Campos principales del proveedor
    name = fields.Char(string='Nombre del Proveedor', required=True)
    ruc = fields.Char(string='RUC / Identificación', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    direccion = fields.Text(string='Dirección')
    activo = fields.Boolean(string='Activo', default=True)