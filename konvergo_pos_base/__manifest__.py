# copyright 2025 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo / Accounting',
    'version': '14.0.1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Accounting Dependencies for Konvergo',
    'depends': [
        # odoo/odoo
        'point_of_sale',

        # OCA/pos
        'pos_edit_order_line',
        'pos_order_remove_line',
        'pos_order_product_search',
        'pos_product_sort',
        'pos_show_clock',
        'pos_show_config_name',
        'pos_supplierinfo_search',
        'pos_warning_exiting',
        'pos_payment_change',
        'pos_order_mgmt',
        'pos_receipt_hide_price',
        'pos_require_product_quantity',
        'pos_partner_birthdate',
        'pos_report_discount',
        'pos_timeout',
        'pos_empty_home',
        'pos_access_right',
    ],

    'installable': True,
}
