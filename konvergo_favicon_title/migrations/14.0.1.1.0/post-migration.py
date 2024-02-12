# © 2021 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, _):
    env["res.company"].search([])._set_konvergo_favicon()
