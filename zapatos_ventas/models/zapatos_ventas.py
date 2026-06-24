from odoo import models, fields, api

class ZapatosVenta(models.Model):
    _name = 'zapatos.venta'
    _description = 'Registro de Ventas de Zapatos'

    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    zapato_id = fields.Many2one('zapatos.zapato', string='Producto (Zapato)', required=True)
    cantidad = fields.Integer(string='Cantidad', default=1, required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    fecha_venta = fields.Date(string='Fecha de Venta', default=fields.Date.context_today, required=True)
    total_venta = fields.Float(string='Total de Venta', compute='_compute_total_venta', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_total_venta(self):
        for record in self:
            record.total_venta = record.cantidad * record.precio_unitario