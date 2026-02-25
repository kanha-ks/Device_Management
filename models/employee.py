from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    device_assignment_ids = fields.One2many(
        'device.assignment',
        'employee_id'
    )

    # sql constraint
