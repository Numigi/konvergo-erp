# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Konvergo / Inventory',
    'version': '1.1.2',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Other',
    'summary': 'Invetory Dependencies for Konvergo',
    'depends': [
        # odoo/odoo
        'stock',

        # Numigi/odoo-base
        'konvergo_base',

        # Numigi/odoo-stock-addons



        # OCA/stock-logistics-workflow
        "stock_account_show_automatic_valuation", # TA#82002



    ],
    'data': [
    ],
    'installable': True,
}
