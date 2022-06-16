# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : '菩提管理',
    'version' : '0.1',
    'author': "ericxu",
    # 摘要
    'summary': '菩提打卡数据管理',
    # 排序
    'sequence': 10,
    # 简要
    'description': """菩提学院管理""",
    # 模块分类
    # 'category': 'Accounting/Accounting',
    # 模块网站
    # 'website': 'https://www.odoo.com/page/billing',
    # 'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    # 依赖模块
    'depends' : [],
    # 各类模版文件
    'data': [
        'security/ir.model.access.csv',
        'views/ptcenter_user_views.xml',
        'views/ptcenter_user_type_views.xml',
        'views/ptcenter_class_views.xml',
        'views/ptcenter_class_standard_views.xml',
        'views/ptcenter_mygroup_views.xml',
        'views/ptcenter_dkform_views.xml',
        'views/ptcenter_attendance_views.xml',
        'wizard/ptcenter_report_select_view.xml',
        # 'views/ptcenter_month_summary_views.xml'
    ],
    #
    'demo': [],
    'qweb': [
        'static/src/xml/tree_view_odoo.xml'
    ],
    # 'installable': True,
    # 在应用中搜得到
    'application': True,
    # 'auto_install': False,
    # 'post_init_hook': '_account_post_init',
}
