# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common


class TestIcons(common.TransactionCase):

    def test_board_icon(self):
        menu_item = self.env.ref("base.menu_board_root")
        assert menu_item.web_icon == "konvergo_icons,static/icons/dashboard.png"
