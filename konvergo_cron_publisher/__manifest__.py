# Copyright 2024-today Numigi and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo Cron Publicher',
    'version': '16.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Disable the cron notifying odoo',
    'depends': [
        'mail',
    ],
    'data': [
        'data/ir_cron_data.xml',
    ],
    'installable': True,
}
