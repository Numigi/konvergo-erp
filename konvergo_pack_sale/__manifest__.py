# © 2025 Numigi (tm) and all its contributors (https://numigi.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo Pack - Sale",
    "version": "18.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://numigi.com",
    "license": "LGPL-3",
    "category": "Sales",
    "summary": "Sales management pack for Konvergo",
    "depends": [
        "sale_management",
        "konvergo_pack_contact",
        # OCA/sale-workflow - Dépendances à activer
        # "product_form_sale_link",
        # "sale_cancel_reason",
        # "sale_force_invoiced",
        # "sale_invoice_policy",
        # "sale_order_price_recalculation",
        # "sale_order_revision",

        # Numigi/odoo-partner-addons - Dépendances à activer
        # "contacts_config_sale_manager",

        # Numigi/odoo-sale-addons - Dépendances à activer
        # "sale_stock_availability_popover",
        # "sale_delivery_completion",
    ],
    "data": [],
    "installable": True,
    "auto_install": False,
}
