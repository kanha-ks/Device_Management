from odoo import models, fields

class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    name = fields.Char(required=True, string="Name")
    device_attribute_id = fields.Many2one('device.attribute', string="Attributes", ondelete="cascade")

    # sql constraint
    _sql_constraint = [
        ('unique_device_attribute_value','unique(name,device_attribute_id)','Both should be unique')
    ]