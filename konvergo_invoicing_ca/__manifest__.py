# Copyright 2025 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Invoicing CA",
    "version": "18.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Invoicing CA Dependencies for Konvergo",
    "depends": [
        # odoo/odoo
        "l10n_ca",
        # Numigi/konvergo-erp
        "konvergo_invoicing",
        # Numigi/odoo-base-addons
        "base_translation_manager",
        #"currency_rate_update_boc", # Not Available in v18
    ],
    "data": [],
    "installable": True,
}
