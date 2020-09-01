# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Dependencies for Konvergo',
    'depends': [
        # Numigi/odoo-base
        'numipack',
        'konvergo_bot',  # TA#16528
        'konvergo_cron_publisher',  # TA#16530
        'konvergo_favicon_title',  # TA#16527
        'konvergo_icons',
        'konvergo_login_page',  # TA#18145

        # OCA/social
        'mail_debrand',  # TA#16549

        # OCA/server-brand
        'remove_odoo_enterprise',  # TA#22257

        # theme
        'muk_web_theme',
    ],
    'installable': True,
}
