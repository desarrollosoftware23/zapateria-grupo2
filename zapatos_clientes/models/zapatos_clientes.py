from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class ZapatosCliente(models.Model):
    _name = 'zapatos.cliente'
    _description = 'Cliente de Zapateria'

    name = fields.Char(string='Nombre completo', required=True)
    cedula = fields.Char(string='Cedula o identificacion', required=True)
    telefono = fields.Char(string='Telefono')
    email = fields.Char(string='Correo electronico')
    direccion = fields.Text(string='Direccion')
    fecha_registro = fields.Date(string='Fecha de registro', default=fields.Date.context_today)
    zapato_id = fields.Many2one('zapatos.zapato', string='Zapato de interes')

    _sql_constraints = [
        ('cedula_unica', 'UNIQUE(cedula)', 'Ya existe un cliente con esta cedula.'),
    ]

    @api.constrains('cedula')
    def _check_cedula(self):
        for record in self:
            if record.cedula:
                if not record.cedula.isdigit():
                    raise ValidationError('La cedula solo debe contener numeros.')
                if len(record.cedula) != 10:
                    raise ValidationError('La cedula debe tener exactamente 10 digitos.')

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(patron, record.email):
                    raise ValidationError('El correo electronico no tiene un formato valido.')

    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            if record.telefono:
                if not record.telefono.isdigit():
                    raise ValidationError('El telefono solo debe contener numeros.')
                if len(record.telefono) != 10:
                    raise ValidationError('El telefono debe tener 10 digitos.')
