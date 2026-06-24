from odoo import models, fields, api


class ZapatosEnvio(models.Model):
    _name = "zapatos.envio"
    _description = "Envío de Zapatos"
    _rec_name = "codigo"

    codigo = fields.Char(
        string="Código",
        required=True,
        readonly=True,
        copy=False,
        default="Nuevo"
    )

    zapato_id = fields.Many2one(
        "zapatos.zapato",
        string="Zapato",
        required=True
    )

    cliente_id = fields.Many2one(
        "zapatos.cliente",
        string="Cliente",
        required=True
    )

    telefono = fields.Char(
        string="Teléfono",
        related="cliente_id.telefono",
        readonly=True
    )

    email = fields.Char(
        string="Correo electrónico",
        related="cliente_id.email",
        readonly=True
    )

    direccion = fields.Text(
        string="Dirección",
        related="cliente_id.direccion",
        readonly=True
    )

    ciudad = fields.Char(
        string="Ciudad"
    )

    provincia = fields.Char(
        string="Provincia"
    )

    transportista = fields.Char(
        string="Transportista"
    )

    numero_guia = fields.Char(
        string="Número de guía"
    )

    fecha_envio = fields.Date(
        string="Fecha de envío",
        default=fields.Date.context_today
    )

    fecha_entrega = fields.Date(
        string="Fecha estimada de entrega"
    )

    costo = fields.Float(
        string="Costo del envío"
    )

    prioridad = fields.Selection(
        [
            ("baja", "Baja"),
            ("media", "Media"),
            ("alta", "Alta"),
        ],
        string="Prioridad",
        default="media"
    )

    estado = fields.Selection(
        [
            ("pendiente", "Pendiente"),
            ("preparando", "Preparando"),
            ("enviado", "Enviado"),
            ("transito", "En tránsito"),
            ("entregado", "Entregado"),
            ("cancelado", "Cancelado"),
        ],
        string="Estado",
        default="pendiente"
    )

    observaciones = fields.Text(
        string="Observaciones"
    )

    dias_entrega = fields.Integer(
        string="Días de entrega",
        compute="_compute_dias_entrega",
        store=True
    )

    entregado = fields.Boolean(
        string="Entregado",
        compute="_compute_entregado",
        store=True
    )

    @api.depends("fecha_envio", "fecha_entrega")
    def _compute_dias_entrega(self):
        for record in self:
            if record.fecha_envio and record.fecha_entrega:
                record.dias_entrega = (
                    record.fecha_entrega - record.fecha_envio
                ).days
            else:
                record.dias_entrega = 0

    @api.depends("estado")
    def _compute_entregado(self):
        for record in self:
            record.entregado = record.estado == "entregado"

    @api.model
    def create(self, vals):
        if vals.get("codigo", "Nuevo") == "Nuevo":
            vals["codigo"] = (
                self.env["ir.sequence"].next_by_code("zapatos.envio")
                or "Nuevo"
            )
        return super().create(vals)