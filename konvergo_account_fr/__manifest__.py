# Copyright 2025 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Account FR",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Account FR Dependencies for Konvergo",
    "depends": [
        # Numigi/konvergo-erp
        "konvergo_account",
        "konvergo_invoicing_fr",
        # OCA/l10n-france
        "l10n_fr_account_vat_return",
        "l10n_fr_oca",
        "l10n_fr_fec_oca",
        "l10n_fr_mis_reports",
    ],
    "data": ["data/menu.xml"],
    "installable": True,
}
