FROM quay.io/numigi/odoo-public:14.latest
LABEL maintainer="contact@numigi.com"

USER root

COPY .docker_files/test-requirements.txt .
RUN pip3 install -r test-requirements.txt

COPY .docker_files/requirements.txt .
RUN pip3 install -r requirements.txt

# Variable used for fetching private git repositories.
ARG GIT_TOKEN

ENV THIRD_PARTY_ADDONS /mnt/third-party-addons
RUN mkdir -p "${THIRD_PARTY_ADDONS}" && chown -R odoo "${THIRD_PARTY_ADDONS}"
COPY ./gitoo.yml /gitoo.yml
RUN gitoo install-all --conf_file /gitoo.yml --destination "${THIRD_PARTY_ADDONS}"

USER odoo

COPY canada_mis_report /mnt/extra-addons/canada_mis_report
COPY canada_vat_label /mnt/extra-addons/canada_vat_label
COPY konvergo_account /mnt/extra-addons/konvergo_account
COPY konvergo_account_fr /mnt/extra-addons/konvergo_account_fr
COPY konvergo_base /mnt/extra-addons/konvergo_base
COPY konvergo_bot /mnt/extra-addons/konvergo_bot
COPY konvergo_contact /mnt/extra-addons/konvergo_contact
COPY konvergo_cron_publisher /mnt/extra-addons/konvergo_cron_publisher
COPY konvergo_favicon_title /mnt/extra-addons/konvergo_favicon_title
COPY konvergo_icons /mnt/extra-addons/konvergo_icons
COPY konvergo_login_page /mnt/extra-addons/konvergo_login_page
COPY konvergo_login_page_website /mnt/extra-addons/konvergo_login_page_website
COPY konvergo_mail_notification /mnt/extra-addons/konvergo_mail_notification
COPY konvergo_mail_templates /mnt/extra-addons/konvergo_mail_templates
COPY konvergo_pos /mnt/extra-addons/konvergo_pos
COPY konvergo_product /mnt/extra-addons/konvergo_product
COPY konvergo_sale /mnt/extra-addons/konvergo_sale
COPY konvergo_web_logo /mnt/extra-addons/konvergo_web_logo
COPY lang_fr_activated /mnt/extra-addons/lang_fr_activated
COPY mail_color_konvergo /mnt/extra-addons/mail_color_konvergo
COPY mail_template_fr_fields /mnt/extra-addons/mail_template_fr_fields
COPY ui_color_konvergo /mnt/extra-addons/ui_color_konvergo

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo
