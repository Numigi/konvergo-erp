# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo Favicon & title",
    "version": "1.1.1",
    "author": "Numigi",
    "maintainer": "Numigi",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Setup of favicon and title for konvergo instance",
    "depends": [
        "web",
    ],
    "data": [
        "views/webclient_templates.xml",
        "views/assets.xml",
        "views/res_company.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
}
