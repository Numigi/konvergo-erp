# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo Mail Templates",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Add custom mail templates for Konvergo",
    "depends": ["mail", "mail_template_fr_fields"],
    "data": [
        "templates/account_invoice.xml",
        "templates/account_payment.xml",
        "templates/hr_recruitment_aknowledgment.xml",
        "templates/hr_recruitment_interest.xml",
        "templates/hr_recruitment_refuse.xml",
        "templates/portal_new_user.xml",
        "templates/purchase_order.xml",
        "templates/purchase_rfq.xml",
        "views/mail_template.xml",
        "views/menu.xml",
    ],
    "installable": True,
}
