from odoo import fields, models


class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'

    name = fields.Char(string="Device Name")
    code = fields.Char(string="Code")

    # sequence
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Device Attributes")
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="Device Models")
    device_ids = fields.One2many('device.device', 'device_type_id', string="Devices")

    #     give the sql constraint before execute


    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name must be unique'),
        ('code_unique', 'unique(code)', 'Code must be unique'),
    ]
