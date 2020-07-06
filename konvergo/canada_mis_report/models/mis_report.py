# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


kpi_descriptions = [
    ('BALANCE', 'Actifs moins le passif et les capitaux propres'),
    ('CGS', 'CMV - Coût des marchandises vendues'),
    ('CREDIT_CARDS', 'Cartes de crédit'),
    ('EBIT', 'BAII - Bénéfice avant intérêts et impôts'),
    ('EBT', 'BAI - Bénéfice avant impôts'),
    ('EQUITY', 'Capitaux propres et bénéfices non-répartis'),
    ('FIXED_ASSETS', 'Immobilisations'),
    ('GROSS_PROFIT', 'Bénéfice brut'),
    ('INC', 'Revenus'),
    ('INDIRECT_COSTS', 'Coûts indirects'),
    ('INTEREST', 'Intérêts'),
    ('LIQUIDITY', 'Liquidités'),
    ('NET_PROFIT', 'Bénéfice net'),
    ('NON_CURRENT_LIABILITIES', 'Passif non courant'),
    ('ONE_TIME_CHARGES', 'Charges ponctuelles'),
    ('ONE_TIME_REVENUES', 'Revenus ponctuels'),
    ('OTHER_CURRENT_ASSETS', 'Autres actifs courants'),
    ('OTHER_CURRENT_LIABILITIES', 'Autre passif non courant'),
    ('OTHER_NON_CURRENT_ASSETS', 'Autres actifs non courants'),
    ('PAYABLE', 'Comptes payables'),
    ('PRE_PAID_EXPENSES', 'Charges prépayées'),
    ('RECEIVABLE', 'Comptes recevables'),
    ('TAXES', 'Impôts'),
    ('TOTAL_ASSETS', 'Total actifs'),
    ('TOTAL_CURRENT_ASSETS', 'Total actifs courants'),
    ('TOTAL_EQUITY', 'Total capitaux propres'),
    ('TOTAL_EQUITY_LIABILITIES', 'Total passif et capitaux propres'),
    ('TOTAL_LIABILITIES', 'Total passif'),
    ('TOTAL_NON_CURRENT_ASSETS', 'Total actifs non courants'),
]


class MisReport(models.Model):

    _inherit = "mis.report"

    @api.model
    def translate_canada_reports(self):
        """Translate the canada reports.

        This method is called from an xml data file.
        It translates the kpi lines of the reports.

        The reason to use python to translate these descriptions
        is that a po file can not be used.

        In order to use a po file, each kpi would need to be declared
        as a disctint xml record.

        Kpi lines can not be declared with xml ids because a deleted
        line would be loaded when updating the module (even with noupdate='1').
        """
        for kpi_name, fr_term in kpi_descriptions:
            self._translate_canada_kpi(kpi_name, fr_term)

    def _translate_canada_kpi(self, kpi_name, fr_term):
        reports = (
            self.env.ref("canada_mis_report.income_statement_summary") |
            self.env.ref("canada_mis_report.income_statement_detailed") |
            self.env.ref("canada_mis_report.balance_sheet_summary") |
            self.env.ref("canada_mis_report.balance_sheet_detailed")
        )
        kpi_lines = reports.mapped("kpi_ids").filtered(lambda k: k.name == kpi_name)

        for kpi in kpi_lines:
            if not _has_been_translated(kpi):
                _with_lang_fr(kpi).description = fr_term


def _has_been_translated(kpi):
    en_term = _with_lang_en(kpi).description
    fr_term = _with_lang_fr(kpi).description
    return en_term != fr_term


def _with_lang_en(kpi):
    return kpi.with_context(lang="en_US")


def _with_lang_fr(kpi):
    return kpi.with_context(lang="fr_FR")
