from odoo import http
from odoo.http import request

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