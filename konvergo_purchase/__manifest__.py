# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Purchase",
    "version": "14.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Sale Dependencies for Konvergo",
    "depends": [
        # Numigi/odoo-product-addons
        "product_purchase_order_link",
        # Numigi/odoo-purchase-addons
        "purchase_order_line_price_history_currency",
        # OCA/purchase-workflow
        "partner_supplierinfo_smartbutton",
        "purchase_last_price_info",
        "purchase_cancel_reason",
        "purchase_order_line_stock_available",
        "purchase_order_line_price_history",
        "purchase_picking_state",
        # OCA/product-attribute
        "product_cost_security",
    ],
    "installable": True,
}
