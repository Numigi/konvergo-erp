# Copyright 2025 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Invoicing FR",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Invoicing FR Dependencies for Konvergo",
    "depends": [
        # Numigi/konvergo-erp
        "konvergo_invoicing",
        # OCA/l10n-france
        "l10n_fr_account_invoice_facturx",
        "l10n_fr_department",
        "l10n_fr_oca",
        "l10n_fr_siret",
        "l10n_fr_state",
        # OCA/account-financial-tools
        "account_invoice_constraint_chronology",
        # OCA/partner-contact
        "partner_firstname",
        # Numigi/odoo-account-addons
        "account_invoice_constraint_chronology_forced",
        # Numigi/odoo-partner-addons
        "partner_firstname_before_lastname",
    ],
    "data": [],
    "installable": True,
}
