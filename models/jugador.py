from odoo import models, fields

PLAYER_RELEVANCE = [
    ('prospect', 'Prospecto'),
    ('sporadic', 'Esporádico'),
    ('rotation', 'Rotación'),
    ('important', 'Importante'),
    ('crucial', 'Esencial')
]


class Jugador(models.Model):
    _name = 'ntropy.fifa22.jugador'
    _description = 'Jugador del FIFA 22'

    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    pais_id = fields.Many2one('res.country', string='País')
    media_global = fields.Float(string='Media Global')
    altura = fields.Float(string='Altura')
    valor_mercado = fields.Monetary(string='Valor de Mercado')
    salario = fields.Monetary(string='Salario')
    cuota_rescision = fields.Monetary(string='Cuota de Rescisión')
    valor_compra = fields.Monetary(string='Valor de Compra')
    valor_venta = fields.Monetary(string='Valor de Venta')
    currency_id = fields.Many2one('res.currency', string='Moneda', required=True,
                                  default=lambda self: self.env.company.currency_id)
    posiciones = fields.Many2many('ntropy.fifa22.posicion', string='Posiciones')
    foot = fields.Selection([
        ("left", "Izquierdo"),
        ("right", "Derecho"),
        ("both", "Ambos")])
    plantilla = fields.Selection(PLAYER_RELEVANCE, string='Relevancia', default='promesa')