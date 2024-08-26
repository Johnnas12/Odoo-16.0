{
    'name': 'hospital management system',
    'author': 'yohanes Mesfin',
    'category': "Custom Apps",
    'website': 'www.hosp.com',
    'summary': "this is hospital management module developed by Yohanes",
    'depends': ["mail"],
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'data/sequence.xml',
        'data/app_category_data.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/hide_apps_menu.xml'

    ]
}