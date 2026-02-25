from odoo import models, fields

class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'Device Assignment'

    name = fields.Char(string="Name", required=True)
    device_id = fields.Many2one('device.device', string="Device", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)

    date_start = fields.Date()
    date_expire = fields.Date()

    state = fields.Selection([
        ('new', 'New'),
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected'),
    ], default='new')

    # sql constraint
    _sql_constraint = [(
        'name_unique','unique(name)','Device name must be unique'
    )]