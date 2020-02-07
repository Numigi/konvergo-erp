# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common
from ..bot import KONVERGO_BOT


class TestBotAnwsers(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.bot_partner = cls.env.ref('base.partner_root')
        cls.channel = cls.env['mail.channel'].create({
            'name': 'Test',
            'channel_type': 'chat',
            'channel_partner_ids': [(4, cls.bot_partner.id)],
        })

    def get_answer(self, message_body, command):
        return self.env['mail.bot']._get_answer(self.channel, message_body, {}, command)

    def test_onboarding_command_help(self):
        self.env.user.odoobot_state = "onboarding_command"
        answer = self.get_answer('', command='help')
        assert 'OdooBot' not in answer
        assert KONVERGO_BOT in answer
