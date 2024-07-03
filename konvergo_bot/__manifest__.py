# Copyright 2024-today Numigi and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo Bot',
    'version': '16.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://www.numigi.com',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'summary': 'Change the name of OdooBot',
    'depends': [
        'mail_bot',
    ],
    'data': [],
    'assets': {
        "web.assets_backend": [
            "konvergo_bot/static/src/js/konvergo_bot.js",
        ]
    },
    'installable': True,
    'post_init_hook': 'post_init_hook',
}
