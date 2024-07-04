# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Odoo Community Interface for Konvergo',
    'version': '16.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Render the Odoo Community interface for Konvergo',
    'depends': ['muk_web_theme'],
    'data': [],
    'assets': {
        "web._assets_primary_variables": [
            "ui_color_konvergo/static/src/sass/colors.scss",
        ],
        "web.assets_backend": [
            "ui_color_konvergo/static/src/sass/navbar.scss",
        ],
        "web._assets_backend_helpers": [
            "ui_color_konvergo/static/src/sass/variables.scss",
        ],
    },
    'installable': True,
}
