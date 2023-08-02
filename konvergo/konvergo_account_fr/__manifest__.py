# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo / Accounting',
    'version': '1.0.1',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'summary': 'Accounting Dependencies for Konvergo France',
    'depends': [
        # OCA/account-financial-reporting
        'account_financial_report',
        'account_tax_balance',
        'partner_statement',        
        
        # OCA/account-financial-tools
        'account_move_name_sequence',

        # OCA/account-reconcile
        'account_reconciliation_widget',
        
        # OCA/l10n-france
        'l10n_fr_department',
        'l10n_fr_account_invoice_facturx',
        'l10n_fr_account_vat_return',
        'l10n_fr_department_delivery',
        'l10n_fr_fec_oca',
        'l10n_fr_mis_reports',
        'l10n_fr_oca',
        'l10n_fr_siret',
        'l10n_fr_state',

        # Numigi/odoo-base
        'konvergo_base',
        'numipack',

        # Numigi/odoo-base-addons
        'base_extended_security',

        # Numigi/odoo-account-addons
        'account_bank_menu',
        'account_move_reversal_access',
        'account_move_unique_reversal',
        'account_negative_debit_credit',
        'account_payment_cancel_group',
        'account_show_full_features',

        # Numigi/aeroo_reports
        'account_check_printing_aeroo',

        # Numigi/odoo-web-addons
        'web_search_date_range_account',

    ],
    'excludes': ["konvergo_account"],
    'data': [
    ],
    'installable': True,
}
