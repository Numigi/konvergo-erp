# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import SavepointCase
from ..models.mail_mail import (
    KONVERGO,
    KONVERGO_WEBSITE,
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
        cls.lead = cls.env["crm.lead"].create({"name": "M Lead",})
        cls.subtype = cls.env.ref("mail.mt_comment")
        cls.lead.message_subscribe([cls.partner.id], subtype_ids=[cls.subtype.id])

    def send_notification_email(self):
        message = self.lead.message_post(
            body="Test", mail_auto_delete=False, send_after_commit=False, force_send=True,
            subtype_id=self.subtype.id,
        )
        return self.env["mail.mail"].search(
            [("mail_message_id", "=", message.id)], limit=1
        )

    def test_odoo_replaced_with_konvergo(self):
        email = self.send_notification_email()
        assert KONVERGO in email.body_html
        assert KONVERGO_WEBSITE in email.body_html

    def test_odoo_only_replaced_in_links(self):
        message = self.lead.message_post(body="Odoo")
        assert "Odoo" in message.body
