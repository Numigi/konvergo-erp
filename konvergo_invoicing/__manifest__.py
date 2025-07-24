# Copyright 2025 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Invoicing",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Accounting Dependencies for Konvergo",
    "depends": [
        # Numigi/odoo-account-addons
        "account_bank_menu",
        "account_move_reversal_access",
        "account_move_unique_reversal",
        "account_negative_debit_credit",
        "account_payment_cancel_group",
        # "account_payment_widget_link", NOT YET AVAILABLE ON V16
        "invoice_refund_not_earlier",
        # "account_show_full_features",
        "account_search_date_range",
        # Numigi/aeroo_reports
        "account_check_printing_aeroo",
        # # OCA/account-financial-reporting
        "partner_statement",
        # OCA/account-financial-tools
        "account_lock_date_update",
        "account_move_name_sequence",
        # OCA/account-reconcile
        "account_reconcile_oca",
    ],
    "data": [
        "views/menu.xml",
    ],
    "installable": True,
}
