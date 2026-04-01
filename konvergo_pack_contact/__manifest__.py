# © 2025 Numigi (tm) and all its contributors (https://numigi.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo Pack - Contact",
    "version": "18.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://numigi.com",
    "license": "LGPL-3",
    "category": "Contact Management",
    "summary": "Contact management pack for Konvergo",
    "depends": [
        "contacts",
        # OCA/partner-contact - Dépendances à activer
        # "partner_firstname",
        # "partner_email_duplicate_warn",
        # "partner_identification",
        # "partner_email_check",

        # Numigi/odoo-partner-addons - Dépendances à activer
        # "contacts_config_menu_moved_right",
        # "partner_edit_group",
        # "partner_category_type",
        # "partner_firstname_before_lastname",
        # "partner_full_text_search",
        # "partner_phone_no_envelope",
        # "partner_key_date",
    ],
    "data": [
        # TODO: Ajouter ir.config_parameter pour:
        # - Ordre d'affichage (Prénom Nom)
        # - lastname requis
    ],
    "installable": True,
    "auto_install": False,
}
