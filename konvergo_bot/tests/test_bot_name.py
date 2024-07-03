# Copyright 2024-today Numigi and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common
from ..bot import KONVERGO_BOT


class TestBotName(common.TransactionCase):

    def test_bot_name(self):
        bot = self.env.ref('base.partner_root')
        assert bot.name == KONVERGO_BOT
