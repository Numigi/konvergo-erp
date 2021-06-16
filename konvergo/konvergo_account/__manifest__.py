# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo / Accounting',
    'version': '1.1.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Accounting Dependencies for Konvergo',
    'depends': [
        # odoo/odoo
        'l10n_ca',

        # Numigi/odoo-base
        'konvergo_base',
        'numipack_account',
        'canada_mis_report',

        # Numigi/odoo-account-addons
        'account_closing_journal',  # TA#22629
        'account_payment_widget_link',
        'account_report_trial_balance',
        'account_show_full_features',  # TA#16549
        'account_unaffected_earnings_disabled',  # TA#22357
        'canada_account_types',  # TA#22360
        'invoice_refund_not_earlier',
        'old_accounts',

        # OCA/mis-builder
        'mis_builder',  # TA#16549

        # OCA/reporting-engine
        'report_xlsx',  # TA#16549 (dependency of mis_builder)

        # OCA/server-ux
        'date_range',  # TA#16549 (dependency of mis_builder)

        # OCA/account-financial-reporting
        # 'account_export_csv',  # TA#16549
        'account_financial_report',  # TA#16549
        # 'mis_builder_cash_flow',  # TA#16549
        # 'partner_statement',  # TA#16549

        # OCA/account-financial-tools
        'account_lock_date_update',  # TA#30205

        # OCA/bank-statement-import
        # 'account_bank_statement_import_txt_xlsx',  # TA#20564

        # akretion
        # 'account_viewer',  # TA#16549
        # 'account_report_viewer',  # TA#16549
    ],
    'data': [
        'views/menu.xml',
    ],
    'installable': True,
}
