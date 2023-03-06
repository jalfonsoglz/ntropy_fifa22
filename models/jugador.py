from odoo import models, fields

PLAYER_RELEVANCE = [
    ('prospect', 'Prospect'),
    ('sporadic', 'Sporadic'),
    ('rotation', 'Rotation'),
    ('important', 'Important'),
    ('crucial', 'Crucial')
]


class Jugador(models.Model):
    _name = 'ntropy.fifa22.jugador'
    _description = 'Jugador del FIFA 22'

    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    pais_id = fields.Many2one('res.country', string='País')
    media_global = fields.Float(string='Media Global')
    altura = fields.Float(string='Altura')
    valor_mercado = fields.Float(string='Valor de Mercado')
    salario = fields.Float(string='Salario')
    cuota_rescision = fields.Float(string='Cuota de Rescisión')
    valor_compra = fields.Float(string='Valor de Compra')
    valor_venta = fields.Float(string='Valor de Venta')
    posiciones = fields.Many2many('ntropy.fifa22.posicion', string='Posiciones')
    foot = fields.Selection([
        ("left", "Izquierdo"),
        ("right", "Derecho"),
        ("both", "Ambos")])
    plantilla = fields.Selection(PLAYER_RELEVANCE, string='Relevancia', default='promesa')

