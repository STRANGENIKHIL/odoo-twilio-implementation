FROM odoo:18.0

# Copy our custom addons folder into the container's standard extra-addons directory
COPY ./custom_addons /mnt/extra-addons

USER root

CMD ["sh", "-c", "unset PORT; exec /entrypoint.sh odoo --proxy-mode -d Nikhil -u web"]
