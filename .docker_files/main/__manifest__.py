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
        # Core architecture
        "konvergo_base",
        "Konvergo_account",
        "konvergo_core",
        "konvergo_ui",
        "konvergo_brand",

        # Functional packs
        "konvergo_pack_contact",
        "konvergo_pack_crm",
        "konvergo_pack_pos",
        "konvergo_pack_product",
        "konvergo_pack_sale",

        # Modules to be migrated later (commented out)
        # "canada_mis_report",         # -> konvergo_l10n_ca
        # "canada_vat_label",          # -> konvergo_l10n_ca
        # "konvergo_account",              # TBD
        # "konvergo_account_fr",           # -> konvergo_l10n_fr
        # "konvergo_bot",                  # -> konvergo_mail_core
        # "konvergo_mail_notification",    # -> konvergo_mail_core
        # "konvergo_mail_templates",       # -> konvergo_pack_templates
        # "lang_fr_activated",         # -> konvergo_l10n_fr
        # "mail_color_konvergo",         # -> konvergo_mail_core
        # "mail_template_fr_fields",   # TBD
    ],
    "installable": True,
}
