# Copyright 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo / Account",
    "version": "16.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Accounting Dependencies for Konvergo",
    "depends": [
        # Numigi/konvergo-erp
        # "konvergo_invoicing", WIP FOR V16
        # Numigi/odoo-account-addons
        # "account_additional_settings", WIP FOR V16
        "account_show_full_features",
        "account_search_date_range",
        "old_accounts",
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
    ],
    "excludes": ["konvergo_account_fr"],
    "data": [
        "views/menu.xml",
    ],
    "installable": True,
}
