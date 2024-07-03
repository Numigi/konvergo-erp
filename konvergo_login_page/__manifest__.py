# © 2019 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo Login Page',
    'version': '16.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Design of the login page of Konvergo',
    'depends': [
        'web',
    ],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        "web._assets_primary_variables": [
            "konvergo_login_page/static/src/scss/colors.scss",
        ],
        "web.assets_frontend": [
            "konvergo_login_page/static/src/scss/components.scss",
            "konvergo_login_page/static/src/scss/database-powered.scss",
        ],
    },
    'installable': True,
}
