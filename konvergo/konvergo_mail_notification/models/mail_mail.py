# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import re
from odoo import api, models


ODOO_REGEX = r">\s*Odoo\s*</a>"
KONVERGO = ">Konvergo</a>"
ODOO_WEBSITE_REGEX = r"\"https://www\.odoo\.com\??(\w|\=|\&|\;)*\""
KONVERGO_WEBSITE = "\"https://www.konvergo.com\""


class MailMessage(models.Model):

    _inherit = "mail.mail"

    @api.model
    def create(self, vals):
        new_vals = self._get_vals_with_konvergo_body(vals)
        return super().create(new_vals)

    @api.multi
    def write(self, vals):
        new_vals = self._get_vals_with_konvergo_body(vals)
        return super().write(new_vals)

    def _get_vals_with_konvergo_body(self, vals):
        if "body_html" not in vals:
            return vals
        body = get_body_for_konvergo(vals["body_html"])
        return dict(vals, body_html=body)


def get_body_for_konvergo(body):
    if not body:
        return body

    if isinstance(body, bytes):
        body = body.decode('utf-8')

    body = re.sub(ODOO_REGEX, KONVERGO, body)
    body = re.sub(ODOO_WEBSITE_REGEX, KONVERGO_WEBSITE, body)
    return body
