from odoo import http
from odoo.http import request
from odoo.orm.fields_misc import Json


class ModelDataController(http.Controller):


    @http.route('/js', website=True, auth='public')
    def modelDataShownMethod(self):
        # return "Hello Models"
        # model_name = self.pool.get('ir.model').search(cr, uid, [('modules','ilike','device_management')])
        # model_name = [1,2,3,4]


        model_name = request.env['ir.model'].search([
            ('model', 'like', 'device'),
        ])

        # for rendering the website page we will request to render that specific webpage
        return request.render("device_management.model_view_template", {
            'models' : model_name
        })

    @http.route('/website_sale/addModuleInfo', type='json',  website=True, auth='public')
    def modelSpecifcDataShown(self, model_name):
        print(f"The model I recieved is {model_name}")

        # records = request.env[model_name].sudo().search_read([], [])

        # Fetch the model metadata
        model = request.env['ir.model'].sudo().search([('model', '=', model_name)])

        info = {
            'id': model.id,
            'name': model.name,
            'model': model.model,
            'module': model.module,
            'state': model.state,
            'transient': model.transient,
            'access_ids': [
                (access.id, access.name, access.perm_read, access.perm_write, access.perm_create, access.perm_unlink)
                for access in model.access_ids],
            'field_ids': [(field.id, field.name, field.ttype) for field in model.field_ids],
        }

        return info
        # return records

