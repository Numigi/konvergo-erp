# © 2021 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, _):
    env = Environment(cr, SUPERUSER_ID, {})
    env["res.company"].search([])._set_konvergo_favicon()
