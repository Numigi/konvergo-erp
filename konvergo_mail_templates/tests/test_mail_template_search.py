# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common
from ..models.mail_template import SHOW_KONVERGO_TEMPLATES


class TestMailTemplateSearch(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.template = cls.env["mail.template"].create(
            {
                "name": "My Konvergo Template",
                "is_konvergo_template": True,
            }
        )

    def test_konvergo_templates_excluded_from_search(self):
        templates = self.env["mail.template"].search([])
        assert self.template not in templates

    def test_search_with_context_parameter(self):
        context = {SHOW_KONVERGO_TEMPLATES: True}
        templates = self.env["mail.template"].with_context(**context).search([])
        assert self.template in templates

    def test_search_konvergo_templates_explicitly(self):
        templates = self.env["mail.template"].search(
            [("is_konvergo_template", "=", True)]
        )
        assert self.template in templates

    def test_konvergo_templates_excluded_from_read_group(self):
        domain = [("id", "=", self.template.id)]
        templates = self.env["mail.template"].read_group(domain, ["name"], ["name"])
        assert not templates

    def test_read_group_konvergo_templates_explicitly(self):
        domain = [("id", "=", self.template.id)]
        context = {SHOW_KONVERGO_TEMPLATES: True}
        templates = (
            self.env["mail.template"]
            .with_context(**context)
            .read_group(domain, ["name"], ["name"])
        )
        assert len(templates) == 1
