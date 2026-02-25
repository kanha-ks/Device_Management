from odoo import fields, models

class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'

    name = fields.Char(required=True, string="Name")
    shared = fields.Boolean(string="is_shared")
    device_type_id = fields.Many2one('device.type', required=True, string="Device Type")
    device_brand_id = fields.Many2one('device.brand', string="Brand")
    device_model_id = fields.Many2one('device.model', string="Model")

    attribute_assignment_ids = fields.One2many(
        'device.attribute.assignment',
        'device_id',
        string="Attribute Assignment"
    )

    # sql constraint
    _sql_constraint = [('name_unique','unique(name)','Device name should be unique')]