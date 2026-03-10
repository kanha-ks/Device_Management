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
        'views/model_view_template.xml',
        'views/device_management_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'device_management/static/src/js/list_button.js',
            'device_management/static/src/xml/list_button.xml',
        ],
        'web.assets_frontend': [
            'device_management/static/src/js/show_model_info.js',
        ],
    },
    'installable': True,
    'application': True,
}
