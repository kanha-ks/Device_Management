from odoo import models, fields

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'Device Attribute Assignment'

    device_id = fields.Many2one('device.device',string="Device",ondelete='cascade', required=True)
    device_attribute_id = fields.Many2one('device.attribute',string="Device Attribute", ondelete='cascade')
    device_attribute_value_id = fields.Many2one(
        'device.attribute.value',
        string="Device Attribute Value",
        required=True
    )
    # sql constraint
    _sql_constraint = [('device_id_unique', 'unique(device_id)', 'device_attribute_id', 'Each attribute can be assigned once per device')]
