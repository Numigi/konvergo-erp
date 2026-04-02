# © 2025 Numigi (tm) and all its contributors (https://numigi.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo Core",
    "version": "18.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://numigi.com",
    "license": "LGPL-3",
    "category": "Technical",
    "summary": "Technical foundations and security for Konvergo",
    "depends": [
        "base",
        # OCA/server-tools
        "module_change_auto_install",
        # "web_session_auto_close",
        # "web_disable_export_group",
        # "base_optional_quick_create",

        # OCA/server-brand
        # "disable_odoo_online",
        # "remove_odoo_enterprise",

        # Numigi/odoo-base-addons
        # "mail_bot_no_pong",
        # "mail_notification_no_action_button",
        # "base_extended_security",
    ],
    "installable": True,
}
