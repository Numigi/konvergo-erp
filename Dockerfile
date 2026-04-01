# Dockerfile for Konvergo ERP v18
# OCA and Numigi stages commented out - will be re-enabled progressively during migration

# # Stage 1: Install OCA repositories
# FROM quay.io/numigi/odoo-public:18.latest as oca-stage
# LABEL maintainer="contact@numigi.com"
# USER root
# ARG GIT_TOKEN
# RUN mkdir -p /mnt/oca-addons && chown -R odoo /mnt/oca-addons
# COPY ./gitoo-oca.yml /gitoo-oca.yml
# RUN gitoo install-all --conf_file /gitoo-oca.yml --destination /mnt/oca-addons

# # Stage 2: Install Numigi repositories
# FROM quay.io/numigi/odoo-public:18.latest as numigi-stage
# USER root
# ARG GIT_TOKEN
# RUN mkdir -p /mnt/numigi-addons && chown -R odoo /mnt/numigi-addons
# COPY ./gitoo-numigi.yml /gitoo-numigi.yml
# RUN gitoo install-all --conf_file /gitoo-numigi.yml --destination /mnt/numigi-addons

# Stage 3: Final image with all dependencies
FROM quay.io/numigi/odoo-public:18.latest
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

# Copy modules from previous stages (commented out for now)
# COPY --from=oca-stage /mnt/oca-addons/ ${THIRD_PARTY_ADDONS}/
# COPY --from=numigi-stage /mnt/numigi-addons/ ${THIRD_PARTY_ADDONS}/

USER odoo

# Core architecture modules
COPY konvergo_base /mnt/extra-addons/konvergo_base
COPY konvergo_core /mnt/extra-addons/konvergo_core
COPY konvergo_ui /mnt/extra-addons/konvergo_ui
COPY konvergo_brand /mnt/extra-addons/konvergo_brand

# Functional packs
COPY konvergo_pack_contact /mnt/extra-addons/konvergo_pack_contact
COPY konvergo_pack_crm /mnt/extra-addons/konvergo_pack_crm
COPY konvergo_pack_pos /mnt/extra-addons/konvergo_pack_pos
COPY konvergo_pack_product /mnt/extra-addons/konvergo_pack_product
COPY konvergo_pack_sale /mnt/extra-addons/konvergo_pack_sale

# Modules to be migrated later (commented out)
# COPY canada_mis_report /mnt/extra-addons/canada_mis_report  # -> konvergo_l10n_ca
# COPY canada_vat_label /mnt/extra-addons/canada_vat_label    # -> konvergo_l10n_ca
# COPY konvergo_account /mnt/extra-addons/konvergo_account          # TBD
# COPY konvergo_account_fr /mnt/extra-addons/konvergo_account_fr    # -> konvergo_l10n_fr
# COPY konvergo_bot /mnt/extra-addons/konvergo_bot                  # -> konvergo_mail_core
# COPY konvergo_mail_notification /mnt/extra-addons/konvergo_mail_notification  # -> konvergo_mail_core
# COPY konvergo_mail_templates /mnt/extra-addons/konvergo_mail_templates          # -> konvergo_pack_templates
# COPY lang_fr_activated /mnt/extra-addons/lang_fr_activated  # -> konvergo_l10n_fr
# COPY mail_color_konvergo /mnt/extra-addons/mail_color_konvergo  # -> konvergo_mail_core
# COPY mail_template_fr_fields /mnt/extra-addons/mail_template_fr_fields      # TBD

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo
