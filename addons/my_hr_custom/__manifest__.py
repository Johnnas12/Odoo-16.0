# my_hr_custom/__manifest__.py
{
    'name': 'My HR Custom Module',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Custom modifications to the HR module',
    'description': 'This module adds custom features and modifications to the HR module.',
    'author': 'Yohanes Mesfin',
    'depends': ['hr'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
