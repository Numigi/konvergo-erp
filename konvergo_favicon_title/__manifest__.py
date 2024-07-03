# © 2020 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Konvergo Favicon & title",
    "version": "16.0.1.0.0",
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
        "views/res_company.xml",
    ],
    'assets': {
        "web.assets_backend": [
            "konvergo_favicon_title/static/src/js/title.js",
        ],
    },
    "installable": True,
    "post_init_hook": "post_init_hook",
}
