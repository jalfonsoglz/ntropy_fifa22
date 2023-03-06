from odoo import models, fields


class Temporada(models.Model):
    _name = 'ntropy.fifa22.temporada'
    _description = 'Temporada del FIFA 22'

    name = fields.Char(string='Nombre', required=True)
    temporada = fields.Selection([('2021/2022', '2021/2022'),
                                  ('2022/2023', '2022/2023'),
                                  ('2023/2024', '2023/2024'),
                                  ('2024/2025', '2024/2025'),
                                  ('2025/2026', '2025/2026'),
                                  ('2026/2027', '2026/2027'),
                                  ('2027/2028', '2027/2028'),
                                  ('2028/2029', '2028/2029'),
                                  ('2029/2030', '2029/2030'),
                                  ('2030/2031', '2030/2031'),
                                  ('2031/2032', '2031/2032'),
                                  ('2032/2033', '2032/2033'),
                                  ('2033/2034', '2033/2034'),
                                  ('2034/2035', '2034/2035'),
                                  ('2035/2036', '2035/2036')],
                                 string='Temporada', required=True, index=True, copy=False, default='2021/2022',
                                 track_visibility='onchange', help='Temporada')
    jugador_ids = fields.Many2many('ntropy.fifa22.jugador', string='Jugadores')
    partidos = fields.Integer(string='Partidos Jugados')
    goles = fields.Integer(string='Goles')
    asistencias = fields.Integer(string='Asistencias')
    tarjetas_amarillas = fields.Integer(string='Tarjetas Amarillas')
    tarjetas_rojas = fields.Integer(string='Tarjetas Rojas')
    prm = fields.Integer(string='Calificación Promedio')