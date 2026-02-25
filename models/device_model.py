from odoo import fields, models, api
from odoo.exceptions import ValidationError


class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device Model'

    name = fields.Char(string="Model Name")

    device_type_id = fields.Many2one('device.type', string="Device Type", required=True)
    device_brand_id = fields.Many2one('device.brand', string="Device Brand", required=True)

    # sql constraint
    _sql_constraints = [
        ('name_type_unique',
         'unique(name, device_type_id, device_brand_id)',
         'Model must be unique per type'),
    ]

    @api.constrains('name', 'device_type_id', 'device_brand_id')
    def _check_unique_values(self):
       for rec in self:
           domain = [
               ('id', '!=', rec.id),
               ('name', '=', rec.name),
               ('device_type_id', '=', rec.device_type_id.id),
               ('device_brand_id','=', rec.device_brand_id.id),
           ]

           if self.search(domain) :
               raise ValidationError("Data already exists please add another")
