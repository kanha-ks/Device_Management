from odoo import models, fields;
from odoo.odoo.orm.decorators import readonly


class ModuleName(models.TransientModel):

    _name = 'device.modulename.wizard'
    _description = 'display the Module name wizard'

    moduleName = fields.Char(string="name", readonly=True)