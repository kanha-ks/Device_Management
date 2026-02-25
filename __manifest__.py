{
    'name': 'Device Management',
    'author': 'Ksolves',
    'version': '1.0',
    'depends': ['hr'],
    'sequence': 1,
    'data': [
        'security/ir.model.access.csv',
        'views/device_management_device_assignment_views.xml',
        'views/device_management_device_attribute_views.xml',
        'views/device_management_device_views.xml',
        'views/device_management_device_brand_views.xml',
        'views/device_management_device_models_view.xml',
        'views/device_management_device_types_views.xml',
        'views/device_management_menus.xml',
    ],
    'installable': True,
    'application': True,
}
