{
    'name': "Automatic Database Backup To Local Server, Remote Server,"
            "Google Drive, Dropbox, Onedrive, Nextcloud and Amazon S3 Odoo17",
    'version': '17.0.6.0.1',
    'live_test_url': 'https://youtu.be/Q2yMZyYjuTI',
    'category': 'Extra Tools',
    'summary': 'Odoo Database Backup, Automatic Backup, Database Backup, Automatic Backup,Database auto-backup, odoo backup'
               'google drive, dropbox, nextcloud, amazon S3, onedrive or '
               'remote server, Odoo17, Backup, Database, Odoo Apps',
    'description': 'Odoo Database Backup, Database Backup, Automatic Backup, automatic database backup, odoo17, odoo apps,backup, automatic backup,odoo17 automatic database backup,backup google drive,backup dropbox, backup nextcloud, backup amazon S3, backup onedrive',
    'author': "Farid MOUZOUNE",
    'company': 'Farid MOUZOUNE',
    'maintainer': 'Farid MOUZOUNE',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'views/db_backup_configure_views.xml',
        'wizard/dropbox_auth_code_views.xml',
    ],
    'external_dependencies': {
        'python': ['dropbox', 'pyncclient', 'boto3', 'nextcloud-api-wrapper','paramiko']},
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
