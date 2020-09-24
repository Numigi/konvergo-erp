# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from ddt import ddt, data
from odoo.tests import common


@ddt
class TestMailTemplateSearch(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.email_from = "test@example.com"
        cls.partner_to = "123"
        cls.subject = "My Subject"
        cls.lang = "fr"
        cls.konvergo_template = cls.env["mail.template"].create(
            {
                "name": "My Konvergo Template",
                "is_konvergo_template": True,
                "email_from": cls.email_from,
                "partner_to": cls.partner_to,
                "subject": cls.subject,
                "lang": cls.lang,
                "odoo_template_ref": "test.my_odoo_template_ref",
            }
        )
        cls.odoo_template = cls.env["mail.template"].create(
            {"name": "My Odoo Template"}
        )
        cls.env["ir.model.data"].create(
            {
                "model": "mail.template",
                "res_id": cls.odoo_template.id,
                "name": "my_odoo_template_ref",
                "module": "test",
            }
        )

    def test_update_from_konvergo_templates(self):
        self.env["mail.template"].update_from_konvergo_templates()
        assert self.odoo_template.updated_from_konvergo
        assert self.odoo_template.email_from == self.email_from
        assert self.odoo_template.partner_to == self.partner_to
        assert self.odoo_template.subject == self.subject
        assert self.odoo_template.lang == self.lang

    @data("body_html", "subject")
    def test_translated_fields(self, field):
        en_value = "My beautiful content"
        fr_value = "Mon beau contenu"
        _with_en(self.konvergo_template)[field] = en_value
        _with_fr(self.konvergo_template)[field] = fr_value
        _with_en(self.odoo_template)[field] = "Old Body"
        _with_fr(self.odoo_template)[field] = "Ancien contenu"
        self.env["mail.template"].update_from_konvergo_templates()
        assert _with_en(self.odoo_template)[field] == en_value
        assert _with_fr(self.odoo_template)[field] == fr_value

    def test_template_not_updated_twice(self):
        self.env["mail.template"].update_from_konvergo_templates()
        self.konvergo_template.email_from = "newvalue@example.com"
        self.env["mail.template"].update_from_konvergo_templates()
        assert self.odoo_template.email_from == self.email_from


def _with_en(record):
    return _with_lang(record, "en_US")


def _with_fr(record):
    return _with_lang(record, "fr_FR")


def _with_lang(record, lang):
    return record.with_context(lang=lang)
