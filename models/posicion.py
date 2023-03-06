from odoo import models, fields

PLAYER_POSITIONS = [('GK', 'POR'),
                    ('RWB', 'LD'),
                    ('RB', 'DFD'),
                    ('CB', 'DCF'),
                    ('LF', 'DFI'),
                    ('LWB', 'LI'),
                    ('CDM', 'MCD'),
                    ('CM', 'MC'),
                    ('RM', 'MD'),
                    ('LM', 'MI'),
                    ('CAM', 'MCO'),
                    ('RW', 'ED'),
                    ('LW', 'EI'),
                    ('CF', 'MP'),
                    ('ST', 'DC')
                    ]


class Posicion(models.Model):
    _name = 'ntropy.fifa22.posicion'
    _description = 'Posición del jugador en el campo'
    _order = 'name'

    name = fields.Char(string='Posición', required=True)
    code = fields.Selection(PLAYER_POSITIONS)
