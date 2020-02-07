# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import base64
from odoo import SUPERUSER_ID
from odoo.api import Environment
from odoo.tools.misc import file_open
from .bot import KONVERGO_BOT


def post_init_hook(cr, _):
    env = Environment(cr, SUPERUSER_ID, {})
    bot = env.ref('base.partner_root')
    bot.name = KONVERGO_BOT
    bot.email = "monkeybot@konvergo.com"
    bot.image = _get_bot_image_data()


def _get_bot_image_data():
    with file_open('konvergo_bot/static/src/img/konvergo_bot.png', 'rb') as file:
        data = file.read()
    return base64.b64encode(data)
