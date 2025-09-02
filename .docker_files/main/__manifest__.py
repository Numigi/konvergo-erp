# © 2018 Numigi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Main Module",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://www.numigi.com",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Install all addons required for testing.",
    "depends": [
        # odoo/odoo #  For unit test
        "crm",
        # -
        "canada_mis_report",
        "canada_vat_label",
        "konvergo_account",
        # "konvergo_account_fr", Conflict with konvergo_account
        "konvergo_base",
        "konvergo_bot",
        "konvergo_contact",
        "konvergo_crm",
        "konvergo_cron_publisher",
        "konvergo_favicon_title",
        "konvergo_icons",
        "konvergo_login_page",
        "konvergo_login_page_website",
        "konvergo_mail_notification",
        "konvergo_mail_templates",
        "konvergo_pos",
        "konvergo_product",
        "konvergo_purchase",
        "konvergo_sale",
        "konvergo_web_logo",
        "lang_fr_activated",
        "mail_color_konvergo",
        "mail_template_fr_fields",
        "ui_color_konvergo",
    ],
    "installable": True,
}
