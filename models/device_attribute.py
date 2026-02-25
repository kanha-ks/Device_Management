from odoo import models, fields
from odoo.odoo.orm.decorators import ondelete


class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    name = fields.Char(required=True, string="Name")
    device_type_id = fields.Many2one('device.type',string="Device Type")
    required = fields.Boolean(string="Is Required")

    value_ids = fields.One2many(
        'device.attribute.value',
        'device_attribute_id',
        string="Values"
    )

    # sql constraint
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Attribute must be unique'),
    ]
