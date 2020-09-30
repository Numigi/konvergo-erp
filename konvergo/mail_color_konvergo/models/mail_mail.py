# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


ODOO_FONT_COLOR = "#875a7b"
ODOO_BG_COLOR = "#f2dede"
KONVERGO_FONT_COLOR = "#1a62c6"
KONVERGO_BG_COLOR = "#ecf0f6"


class MailMessage(models.Model):

    _inherit = "mail.mail"

    @api.model
    def create(self, vals):
        new_vals = self._get_vals_with_konvergo_colors(vals)
        return super().create(new_vals)

    @api.multi
    def write(self, vals):
        new_vals = self._get_vals_with_konvergo_colors(vals)
        return super().write(new_vals)

    def _get_vals_with_konvergo_colors(self, vals):
        if "body_html" not in vals:
            return vals
        body = get_body_with_konvergo_colors(vals["body_html"])
        return dict(vals, body_html=body)


def get_body_with_konvergo_colors(body):
    if not body:
        return ""

    if isinstance(body, bytes):
        body = body.decode('utf-8')

    replacements = (
        (ODOO_FONT_COLOR, KONVERGO_FONT_COLOR),
        (ODOO_BG_COLOR, KONVERGO_BG_COLOR),
    )
    for color_from, color_to in replacements:
        body = _get_html_with_color_replaced(body, color_from, color_to)
    return body


def _get_html_with_color_replaced(html, color_from, color_to):
    return html.replace(color_from.upper(), color_to).replace(color_from, color_to)
