odoo.define('konvergo_icons.settings', function (require) {
    "use strict";

    // Declare dictionary to store the icon of each possible app having settings
    // and icon is available in konvergo_icons module
    var moduleIcons = {
        'account': 'accounting.png',
        'admin_light_base': 'admin_light.png',
        'contacts': 'contacts.png',
        'crm': 'crm.png',
        'event': 'events.png',
        'fleet': 'fleet.png',
        'github_connector': 'github.png',
        'hr': 'employees.png',
        'hr_attendance': 'presence.png',
        'hr_expense': 'expenses.png',
        'hr_holidays': 'time_off.png',
        'hr_payroll': 'payroll.png',
        'hr_recruitment': 'recruitment.png',
        'hr_timesheet': 'timesheets.png',
        'im_livechat': 'live_chat.png',
        'karma': 'karma.png',
        'ks_office365_base': 'office-365.png',
        'mail': 'messages.png',
        'maintenance': 'equipment_maintenance.png',
        'mass_mailing': 'email_marketing.png',
        'mrp': 'manufacturing.png',
        'note': 'notes.png',
        'point_of_sale': 'pos.png',
        'product_configurator': 'configurator.png',
        'project': 'project.png',
        'purchase': 'purchase.png',
        'purchase_request': 'purchase_request.png',
        'queue_job': 'job_queue.png',
        'rma': 'rma.png',
        'recording': 'music.png',
        'repair': 'repair.png',
        'sale_management': 'sales.png',
        'sale_warranty': 'warranty.png',
        'stock': 'inventory.png',
        'stock_barcodes': 'stock_barcodes.png',
        'survey': 'surveys.png',
        'sync_plm': 'sync_plm.png',
        'utm': 'link_tracker.png',
        'website': 'website.png',
        'website_slides': 'e-learning.png'
    }

    var BaseSettingRenderer = require('base.settings').Renderer;
    BaseSettingRenderer.include({
        _getAppIconUrl: function (module) {
            var iconUrl = this._super.apply(this, arguments);
            // Replace the icon of general settings with the new icon
            iconUrl = iconUrl.replace("/base/static/description/settings.png", "/konvergo_icons/static/icons/settings.png");
                if (module in moduleIcons) {
                    // Set the module with konvergo_icons icon if it is found
                    iconUrl = iconUrl.replace("/"+module+"/static/description/icon.png", "/konvergo_icons/static/icons/"+moduleIcons[module]);
                }
                // Keep the default icon if it is not found
                else {
                    iconUrl = iconUrl;
                }
            return iconUrl
        }
    });

});
