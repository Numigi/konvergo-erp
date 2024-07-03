# © 2021 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import base64
import logging
from odoo import fields, models, tools
from odoo.modules.module import get_resource_path

_logger = logging.getLogger(__name__)



class ResCompany(models.Model):

    _inherit = "res.company"

    def _set_konvergo_favicon(self):
        favicon = self._get_default_favicon()
        _logger.info(f"Setting Konvergo favicon for companies: {self.ids}")
        self.write({"favicon": favicon})

    def _get_default_favicon(self, original=False):
        img_path = get_resource_path('konvergo_favicon_title', 'static/src/img/favicon.ico')
        with tools.file_open(img_path, 'rb') as f:
            return base64.b64encode(f.read())

    favicon = fields.Binary(default=_get_default_favicon)
