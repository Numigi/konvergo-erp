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
        "konvergo_brand",
        "konvergo_core",
        "konvergo_mail_notification",
        "konvergo_mail_templates",
        "konvergo_pack_contact",
        "konvergo_pack_crm",
        "konvergo_pack_pos",
        "konvergo_pack_product",
        "konvergo_pack_sale",
        "konvergo_ui",
        "lang_fr_activated",
        "mail_color_konvergo",
        "mail_template_fr_fields",
    ],
    "installable": True,
}
