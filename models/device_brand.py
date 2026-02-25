from odoo import fields, models

class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device Brand'

    name = fields.Char(string="Device Name")
    device_models_ids = fields.One2many('device.model', 'device_brand_id', string="Device Model")

    # sql constraint
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Brand must be unique'),
    ]

