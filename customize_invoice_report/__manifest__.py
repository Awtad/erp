# -*- coding: utf-8 -*-
{
    'name': "Customize Invoice Report",

    'summary': """Customize Invoice Report""",

    'description': """
        Customize Invoice Report
    """,

    'author': "Crevisoft Corporate",
    'website': "https://www.crevisoft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting & Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management','electronic_invoice'],

    # always loaded
    'data': [

        'security/security.xml',
        'views/templates.xml',
        'report/report_invoice.xml',
        'report/report_sale.xml',
    ]
}
