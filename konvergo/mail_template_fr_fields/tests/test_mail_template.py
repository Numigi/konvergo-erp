# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from ddt import ddt, data, unpack
from odoo.tests import common


@ddt
class TestMailTemplate(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.body_html_fr = "Mon contenu en français"
        cls.body_html_en = "My content in english"
        cls.subject_fr = "Mon sujet en français"
        cls.subject_en = "My subject in english"
        cls.template = cls.env["mail.template"].create(
            {
                "name": "My Email Template",
                "body_html_fr": cls.body_html_fr,
                "body_html_en": cls.body_html_en,
                "subject_fr": cls.subject_fr,
                "subject_en": cls.subject_en,
            }
        )

    def test_body_html_fr(self):
        assert self.template.with_fr().body_html == self.body_html_fr

    def test_body_html_en(self):
        assert self.template.with_en().body_html == self.body_html_en

    def test_subject_fr(self):
        assert self.template.with_fr().subject == self.subject_fr

    def test_subject_en(self):
        assert self.template.with_en().subject == self.subject_en

    def test_write_body_html(self):
        new_value_fr = "Nouvelle valeur du contenu"
        new_value_en = "New content value"
        self.template.write({
            'body_html_fr': new_value_fr,
            'body_html_en': new_value_en,
        })
        assert self.template.body_html == new_value_en
        assert self.template.body_html_fr == new_value_fr
        assert self.template.body_html_en == new_value_en

    def test_write_body_html__original_field(self):
        new_value_en = "New content value"
        self.template.body_html = new_value_en
        assert self.template.body_html == new_value_en
        assert self.template.body_html_fr == self.body_html_fr
        assert self.template.body_html_en == new_value_en
