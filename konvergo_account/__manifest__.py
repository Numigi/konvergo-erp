# Copyright 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo / Accounting",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Accounting Dependencies for Konvergo",
    "depends": [
        # odoo/odoo
        "l10n_ca",
        # Numigi/konvergo-erp
        "konvergo_base",
        # Numigi/odoo-base-addons
        "base_fr_ca_labels",
        # Numigi/odoo-account-addons
        "account_bank_menu",
        "account_move_reversal_access",
        "account_move_unique_reversal",
        "account_negative_debit_credit",
        "account_payment_cancel_group",
        "account_show_full_features",
        "bank_statement_import_csv",
        "canada_account_types",
        "invoice_refund_not_earlier",
        "account_search_date_range",
        "old_accounts",
        # Numigi/aeroo_reports
        "account_check_printing_aeroo",
        # OCA/mis-builder
        "mis_builder",
        # OCA/reporting-engine
        "report_xlsx",
        # OCA/server-ux
        "date_range_account",
        # OCA/account-financial-reporting
        "account_financial_report",
        "account_tax_balance",
        "mis_builder_cash_flow",
        "partner_statement",
        # OCA/account-financial-tools
        "account_lock_date_update",
        "account_move_name_sequence",
        # OCA/account-reconcile
        "account_reconcile_oca",
    ],
    "excludes": ["konvergo_account_fr"],
    "data": [
        "views/menu.xml",
    ],
    "installable": True,
}
