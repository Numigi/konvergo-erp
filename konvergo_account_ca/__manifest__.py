# Copyright 2025 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Account CA",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Account CA Dependencies for Konvergo",
    "depends": [
        # Numigi/konvergo-erp
        "konvergo_account",
        "konvergo_invoicing_ca",
        # Numigi/odoo-account-addons
        "bank_statement_import_csv",
        "canada_mis_report",
    ],
    "data": [],
    "installable": True,
}
