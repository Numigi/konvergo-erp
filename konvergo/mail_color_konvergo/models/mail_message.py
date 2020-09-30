# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models
from .mail_mail import get_body_with_konvergo_colors


class MailMessage(models.Model):

    _inherit = "mail.message"

    @api.model
    def create(self, vals):
        new_vals = self._get_vals_with_konvergo_colors(vals)
        return super().create(new_vals)

    @api.multi
    def write(self, vals):
        new_vals = self._get_vals_with_konvergo_colors(vals)
        return super().write(new_vals)

    def _get_vals_with_konvergo_colors(self, vals):
        if "body" not in vals:
            return vals
        body = get_body_with_konvergo_colors(vals["body"])
        return dict(vals, body=body)
