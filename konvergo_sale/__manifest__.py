# © Numigi (tm) and all its contributors (https://numigi.com/r/home)# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Konvergo / Sale",
    "version": "14.0.1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "AGPL-3",
    "category": "Other",
    "summary": "Sale Dependencies for Konvergo",
    "depends": [
        # Numigi/odoo-partner-addons
        "contacts_config_sale_manager",
        # Numigi/odoo-sale-addons
        "sale_stock_availability_popover",
        "sale_delivery_completion",
        # OCA/sale-workflow
        "product_form_sale_link",
        "sale_cancel_reason",
        "sale_force_invoiced",
        "sale_invoice_policy",
        "sale_order_price_recalculation",
        "sale_order_revision",
        "sale_stock_cancel_restriction",
    ],
    "data": [
        "security/extended_security_rule.xml",
    ],
    "installable": True,
}
