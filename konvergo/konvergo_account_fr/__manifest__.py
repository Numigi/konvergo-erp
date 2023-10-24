# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo / Accounting France',
    'version': '1.0.6',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'summary': 'Accounting Dependencies for Konvergo France',
    'depends': [
        # OCA/account-financial-reporting
        'account_financial_report',
        'account_lock_date_update',  # TA#55969
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

        # OCA/partner-contact
        'partner_firstname',  # TA#56107

        # Numigi/odoo-base
        'konvergo_base',
        'numipack',

        # Numigi/odoo-base-addons
        'base_extended_security',

        # Numigi/odoo-account-addons
        'account_bank_menu',
        'account_fiscalyear_end_on_company',  # TA#58024
        'account_invoice_constraint_chronology',  # TA#55774
        'account_move_reversal_access',
        'account_move_unique_reversal',
        'account_negative_debit_credit',
        'account_payment_cancel_group',
        'account_payment_widget_link',  # TA#55969
        'account_show_full_features',
        'bank_statement_import_csv',

        # Numigi/aeroo_reports
        'account_check_printing_aeroo',

        # Numigi/odoo-partner-addons
        'partner_firstname_before_lastname',  # TA#56107

        # Numigi/odoo-web-addons
        'web_search_date_range_account',

    ],
    'excludes': ["konvergo_account"],
    'data': [
    ],
    'installable': True,
}
