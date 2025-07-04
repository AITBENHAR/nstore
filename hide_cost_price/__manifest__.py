
{
    'name': 'Hide Cost Price',
    'version': '17.0.1.0.0',
    'category': 'Stock',
    'summary': """Hide cost price of product for specified users""",
    'description': """Product cost price will be visible only for specified group""",
    'author': 'Farid MOUZOUNE',
    'company': 'Farid MOUZOUNE',
    'maintainer': 'Farid MOUZOUNE',
    'depends': ['product'],
    'license': 'AGPL-3',
    'data': [
        'security/hide_cost_price_groups.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/res_users.xml'
    ],
    'installable': True,
    'auto_install': False,
    "application": False,
}
