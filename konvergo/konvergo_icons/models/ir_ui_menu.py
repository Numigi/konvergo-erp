# © 2020 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class MenuItem(models.Model):

    _inherit = "ir.ui.menu"

    @api.multi
    def write(self, vals):
        super().write(vals)
        if self._should_update_konvergo_icons(vals):
            self.update_konvergo_icons()
        return True

    def _should_update_konvergo_icons(self, vals):
        return not self._context.get("is_updating_konvergo_icon") and "web_icon" in vals

    def _load_records(self, *args, **kwargs):
        res = super()._load_records(*args, **kwargs)
        self.update_konvergo_icons()
        return res

    @api.model
    def update_konvergo_icons(self):
        for xml_ref, filename in ICONS.items():
            self._update_single_konvergo_icon(xml_ref, filename)

    def _update_single_konvergo_icon(self, xml_ref, filename):
        menu = self.env.ref(xml_ref, raise_if_not_found=False)
        if menu:
            web_icon_value = "konvergo_icons,static/icons/{}".format(filename)
            menu._set_web_icon_value(web_icon_value)

    def _set_web_icon_value(self, web_icon_value):
        if self.web_icon != web_icon_value:
            self.with_context(is_updating_konvergo_icon=True).web_icon = web_icon_value


ICONS = {
    "account.menu_finance": "accounting.png",
    "admin_light_base.menu_admin": "admin_light.png",
    "base.menu_administration": "settings.png",
    "base.menu_board_root": "dashboard.png",
    "base.menu_management": "apps.png",
    "calendar.mail_menu_calendar": "calendar.png",
    "contacts.menu_contacts": "contacts.png",
    "crm.crm_menu_root": "crm.png",
    "event.event_main_menu": "events.png",
    "fleet.menu_root": "fleet.png",
    "github_connector.menu_github": "github.png",
    "helpdesk_mgmt.helpdesk_ticket_main_menu": "helpdesk.png",
    "hr.menu_hr_root": "employees.png",
    "hr_attendance.menu_hr_attendance_root": "presence.png",
    "hr_expense.menu_hr_expense_root": "expenses.png",
    "hr_holidays.menu_hr_holidays_root": "time_off.png",
    "hr_payroll.menu_hr_payroll_root": "payroll.png",
    "hr_recruitment.menu_hr_recruitment_root": "recruitment.png",
    "hr_timesheet.timesheet_menu_root": "timesheets.png",
    "im_livechat.menu_livechat_root": "live_chat.png",
    "karma.menu_karma_root": "karma.png",
    "mail.menu_root_discuss": "messages.png",
    "maintenance.menu_maintenance_title": "equipment_maintenance.png",
    "mass_mailing.mass_mailing_menu_root": "email_marketing.png",
    "mrp.menu_mrp_root": "manufacturing.png",
    "note.menu_note_notes": "notes.png",
    "ks_office365_base.ks_office365_main_sidemenu": "office-365.png",
    "product_panel_shortcut.menu_product_root": "products.png",
    "project.menu_main_pm": "project.png",
    "purchase.menu_purchase_root": "purchase.png",
    "queue_job.menu_queue_job_root": "job_queue.png",
    "recording.menu_recording_root": "music.png",
    "repair.menu_repair_order": "repair.png",
    "sale.sale_menu_root": "sales.png",
    "sale_warranty.menu_warranty": "warranty.png",
    "stock.menu_stock_root": "inventory.png",
    "survey.menu_surveys": "surveys.png",
    "utm.menu_link_tracker_root": "link_tracker.png",
    "website.menu_website_configuration": "website.png",
}
