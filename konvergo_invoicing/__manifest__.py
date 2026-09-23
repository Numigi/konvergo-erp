# Copyright 2026 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Invoicing",
    "version": "18.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Invoicing Dependencies for Konvergo",
    "depends": [
        # Numigi/odoo-account-addons
        "account_bank_menu",
        "account_move_reversal_access",
        "account_move_unique_reversal",
      #  "account_negative_debit_credit", #todo NOT AVAILABLE ON V18
        "account_payment_cancel_group",
        # "account_payment_widget_link",  #todo NOT AVAILABLE ON V18
        "invoice_refund_not_earlier",
        #"account_search_date_range",  #todo NOT AVAILA ON V18BLE
        # Numigi/aeroo_reports
        "account_check_printing_aeroo",
        # # OCA/account-financial-reporting
        "partner_statement",

        # OCA/account-financial-tools
        "account_lock_date_update",
        "account_move_name_sequence",
        "account_usability",
        # OCA/account-reconcile
        "account_reconcile_oca",
    ],
    "data": [],
    "installable": True,
}
