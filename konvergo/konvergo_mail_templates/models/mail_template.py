# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models
from odoo.osv.expression import AND
import logging

_logger = logging.getLogger(__name__)

SHOW_KONVERGO_TEMPLATES = "show_konvergo_mail_templates"


class MailTemplate(models.Model):

    _inherit = "mail.template"

    is_konvergo_template = fields.Boolean()
    updated_from_konvergo = fields.Boolean()
    odoo_template_ref = fields.Char()

    @api.model
    def _search(self, args, *args_, **kwargs):
        """Hide konvergo templates from searches by default."""
        if _should_apply_konvergo_template_filter(args, self._context):
            args = AND((args or [], [("is_konvergo_template", "=", False)]))
        return super()._search(args, *args_, **kwargs)

    @api.model
    def read_group(self, domain, *args, **kwargs):
        """Hide konvergo templates from grouped searches by default."""
        if _should_apply_konvergo_template_filter(domain, self._context):
            domain = AND((domain or [], [("is_konvergo_template", "=", False)]))
        return super().read_group(domain, *args, **kwargs)

    def _load_records(self, *args, **kwargs):
        res = super()._load_records(*args, **kwargs)
        self.update_from_konvergo_templates()
        return res

    @api.model
    def update_from_konvergo_templates(self):
        _logger.info("Updating mail templates from konvergo templates")
        konvergo_templates = self._get_konvergo_templates()
        for template in konvergo_templates:
            template._update_odoo_template_if_exists()

    def _get_konvergo_templates(self):
        return self.env["mail.template"].search([("is_konvergo_template", "=", True)])

    def _update_odoo_template_if_exists(self):
        template = self.env.ref(self.odoo_template_ref or "", raise_if_not_found=False)
        if template.updated_from_konvergo:
            _logger.info(
                "The template {} was already updated from konvergo".format(
                    self.odoo_template_ref
                )
            )
        elif template:
            self._update_odoo_template(template)
            _logger.info("Template {} updated".format(self.odoo_template_ref))
        else:
            _logger.info(
                "No mail template found for the xml ID {}".format(
                    self.odoo_template_ref
                )
            )

    def _update_odoo_template(self, odoo_template):
        self._update_odoo_template_vals(odoo_template)
        self._update_odoo_template_translations(odoo_template)

    def _update_odoo_template_vals(self, odoo_template):
        vals = self.with_context(lang="en_US")._get_konvergo_template_vals()
        odoo_template.with_context(lang="en_US").write(vals)

    def _update_odoo_template_translations(self, odoo_template):
        self.copy_translations(odoo_template)

    def _get_konvergo_template_vals(self):
        return {
            "attachment_ids": [(6, 0, self.attachment_ids.ids)],
            "auto_delete": self.auto_delete,
            "body_html": self.body_html,
            "email_cc": self.email_cc,
            "email_from": self.email_from,
            "email_to": self.email_to,
            "lang": self.lang,
            "partner_to": self.partner_to,
            "reply_to": self.reply_to,
            "report_name": self.report_name,
            "report_template": self.report_template.id,
            "subject": self.subject,
            "updated_from_konvergo": True,
            "use_default_to": self.use_default_to,
            "user_signature": self.user_signature,
        }


def _should_apply_konvergo_template_filter(domain, context):
    template_field_in_domain = any(
        isinstance(el, (list, tuple)) and el[0] == "is_konvergo_template"
        for el in domain
    )
    return not (template_field_in_domain or context.get(SHOW_KONVERGO_TEMPLATES))
