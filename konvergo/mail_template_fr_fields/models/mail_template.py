# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class MailTemplate(models.Model):

    _inherit = "mail.template"

    body_html_fr = fields.Char(
        compute="_compute_body_html_fr",
        inverse=lambda self: None,
    )
    body_html_en = fields.Char(
        compute="_compute_body_html_en",
        inverse=lambda self: None,
    )
    subject_fr = fields.Char(
        compute="_compute_subject_fr",
        inverse=lambda self: None,
    )
    subject_en = fields.Char(
        compute="_compute_subject_en",
        inverse=lambda self: None,
    )

    def _compute_body_html_fr(self):
        for record in self:
            record.body_html_fr = record.with_fr().body_html

    def _compute_body_html_en(self):
        for record in self:
            record.body_html_en = record.with_en().body_html

    def _compute_subject_fr(self):
        for record in self:
            record.subject_fr = record.with_fr().subject

    def _compute_subject_en(self):
        for record in self:
            record.subject_en = record.with_en().subject

    @api.model
    def create(self, vals):
        vals_copy = vals.copy()
        template = super().create(vals)
        template._set_fr_field_values(vals_copy)
        template._set_en_field_values(vals_copy)
        return template

    @api.multi
    def write(self, vals):
        vals_copy = vals.copy()
        super().write(vals)
        self._set_fr_field_values(vals_copy)
        self._set_en_field_values(vals_copy)
        return True

    def _set_fr_field_values(self, vals):
        fields = {
            "subject_fr": "subject",
            "body_html_fr": "body_html",
        }
        fr_vals = {fields[k]: v for k, v in vals.items() if k in fields}
        if fr_vals:
            self.with_fr().write(fr_vals)

    def _set_en_field_values(self, vals):
        fields = {
            "subject_en": "subject",
            "body_html_en": "body_html",
        }
        en_vals = {fields[k]: v for k, v in vals.items() if k in fields}
        if en_vals:
            self.with_en().write(en_vals)

    def with_en(self):
        return _with_lang(self, "en_US")

    def with_fr(self):
        return _with_lang(self, "fr_FR")


def _with_lang(record, lang):
    return record.with_context(lang=lang)
