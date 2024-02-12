# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models
from ..bot import KONVERGO_BOT


class MailBot(models.AbstractModel):

    _inherit = 'mail.bot'

    def _get_answer(self, *args, **kwargs):
        answer = super()._get_answer(*args, **kwargs)
        if answer:
            answer = answer.replace('OdooBot', KONVERGO_BOT)
        return answer
