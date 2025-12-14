# Odoo Tutorial On Building a Module

This is a implementation repo from [this Odoo tutorial](https://www.odoo.com/documentation/19.0/developer/tutorials/backend.html#relations-between-models)

## Prerequisite

- Postgres (I use Docker)
- Python

## Installation

    - Clone this repo
    - Deploy postgres using docker-compose
      
        ```
        docker compose up -d
        ```
    
    - Create and activate python virtualenv
    
        ```
        uv venv
        . .venv/bin/activate
    - Install postgres and libpq if you haven't already (I used brew)
    
        ```
        brew install postgresql libpq
        ```
    - Install required dependencies
        ```
        cd odoo19
        uv pip install -r requirements.txt
        ```
        
    - Create ~/.odoorc.d/odoo.conf file for database connection
    
        ```
        mkdir -p ~/.odoorc.d
        nano ~/.odoorc.d/odoo.conf
        ```
    - Paste this to ~/.odoorc.d/odoo.conf:
    
        ```
        [options]
        admin_passwd = admin
        db_host = localhost
        db_port = 5432
        db_user = odoo
        db_password = odoo
        addons_path = /path-to-this-directory/odoo19/custom-addons,/path-to-this-directory/odoo19/addons,/path-to-this-directory/odoo19/odoo/addons
        ```
    - Initialize odoo database

        ```
        ./odoo-bin -c ~/.odoorc.d/odoo.conf -d odoo19_dev -i base --stop-after-init
        ```

## Exercise

    - Create openacademy module inside custom-addon directory

        ```
        ./odoo-bin scaffold openacademy custom-addons/
        ```
    - Run odoo and update openacademy module

        ```
        ./odoo-bin -c ~/.odoorc.d/odoo.conf -d odoo19_dev -u openacademy
        ```
