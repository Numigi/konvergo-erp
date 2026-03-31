# © 2025 Numigi (tm) and all its contributors (https://numigi.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo",
    "version": "18.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://numigi.com",
    "license": "LGPL-3",
    "category": "Hidden",
    "summary": "Konvergo ERP - Main dependencies module",
    "depends": [
        # Konvergo core layers
        "konvergo_core",
        "konvergo_ui",
        "konvergo_brand",

        # Mail modules (to be migrated to konvergo_mail_core)
        # "konvergo_bot",
        # "konvergo_mail_notification",
        # "mail_color_konvergo",

        # Templates (to be migrated to konvergo_pack_templates)
        # "konvergo_mail_templates",

        # Legacy modules - Dépendances à activer progressivement
        # Numigi/odoo-base-addons
        # "mail_bot_no_pong",
        # "mail_notification_no_action_button",

        # Numigi/odoo-web-addons
        # "resize_observer_error_catcher",

        # OCA/server-brand
        # "disable_odoo_online",
        # "remove_odoo_enterprise",

        # OCA/server-tools
        # "tracking_manager",
    ],
    "installable": True,
}
