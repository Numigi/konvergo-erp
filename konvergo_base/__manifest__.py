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
        'konvergo_bot',  # TA#16528
        'konvergo_cron_publisher',  # TA#16530
        'konvergo_favicon_title',  # TA#16527
        'konvergo_icons',
        'konvergo_login_page',  # TA#18145
        'konvergo_mail_notification',
        'konvergo_mail_templates',  # TA#54157
        'konvergo_web_logo',  # TA#25792
        'mail_color_konvergo',
        'numipack',

        # Numigi/odoo-base-addons
        'mail_bot_no_pong',
        'mail_notification_no_action_button',

        # OCA/server-brand
        'disable_odoo_online',  # TA#45124
        'remove_odoo_enterprise',  # TA#45105

        # theme
        'muk_web_theme',
    ],
    'installable': True,
}
