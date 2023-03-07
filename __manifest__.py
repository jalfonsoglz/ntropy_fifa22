# -*- coding: utf-8 -*-
{
    'name': "Ntropy FIFA 22",
    'summary': """Module to manage FIFA 22 player data""",
    'description': """This module allows you to manage player data, team data, and season statistics for FIFA 22.""",
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech/odoo",
    'category': 'Customizations',
    'version': '16.0.0.0.1',
    'license': "LGPL-3",
    'sequence': "-75",
    'depends': ['base'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Wizard
        # Reports
        # Views
        # 'views/main_menu.xml',
        'views/jugador.xml',
        'views/temporada.xml',
        'views/posiciones.xml',
        # Data
        # Sequence
        # Sample
    ],
    'currency': "MXN",
    'qweb': [''],
    'images': [''],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
