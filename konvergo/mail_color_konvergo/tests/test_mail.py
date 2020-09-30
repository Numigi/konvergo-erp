# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import SavepointCase
from ..models.mail_mail import (
    ODOO_FONT_COLOR,
    ODOO_BG_COLOR,
    KONVERGO_FONT_COLOR,
    KONVERGO_BG_COLOR,
)


class TestColorizedBody(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = cls.env["res.users"].create(
            {
                "name": "test@example.com",
                "email": "test@example.com",
                "login": "test@example.com",
            }
        )
        cls.partner = cls.user.partner_id
        cls.lead = cls.env["res.partner"].create({"name": "M Lead",})
        cls.lead.message_subscribe([cls.partner.id])

    def send_notification_email(self):
        message = self.lead.message_post(body="Test")
        message._notify(
            self.lead, {"partner_ids": [(4, self.partner.id)]}, mail_auto_delete=False
        )
        return self.env["mail.mail"].search(
            [("mail_message_id", "=", message.id)], limit=1
        )

    def test_old_colours_not_in_body(self):
        email = self.send_notification_email()
        assert ODOO_FONT_COLOR not in email.body_html
        assert ODOO_BG_COLOR not in email.body_html
        assert ODOO_FONT_COLOR.upper() not in email.body_html
        assert ODOO_BG_COLOR.upper() not in email.body_html

    def test_new_coulours_in_body(self):
        email = self.send_notification_email()
        assert KONVERGO_FONT_COLOR in email.body_html
        assert KONVERGO_BG_COLOR in email.body_html

    def test_new_coulours_in_mail_message(self):
        message = self.lead.message_post(body=ODOO_FONT_COLOR)
        assert KONVERGO_FONT_COLOR in message.body

    def test_post_message_in_bytes(self):
        message = self.lead.message_post(body=ODOO_FONT_COLOR.encode('utf-8'))
        assert KONVERGO_FONT_COLOR in message.body
