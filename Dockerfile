FROM odoo:18.0

# Copy our custom addons folder into the container's standard extra-addons directory
COPY ./custom_addons /mnt/extra-addons

CMD ["odoo", "--db_port=5432"]
