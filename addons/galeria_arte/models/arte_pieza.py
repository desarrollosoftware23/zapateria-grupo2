# -*- coding: utf-8 -*-
from odoo import models, fields

class ArtePieza(models.Model):
    _name = 'arte.pieza'
    _description = 'Piezas de Arte'

    name = fields.Char(string='Nombre de la Obra', required=True)
    artista = fields.Char(string='Artista / Autor')
    fecha_ingreso = fields.Date(string='Fecha de Ingreso', default=fields.Date.context_today)
    descripcion = fields.Text(string='Descripción / Estado de la Obra')