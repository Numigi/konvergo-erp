# © 2023 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import re

from odoo.addons.web.controllers.main import Database


class Database(Database):
    def _render_template(self, **d):
        html = super(Database, self)._render_template(**d)
        html = re.sub(
            r"""(<img(?=\s)[^>]*\ssrc="/web)(/[^/][^"]+logo2.png)""",
            """<img src="/konvergo_web_logo/static/src/img/logo-konvergo.png""",
            html,
        )
        return html
