from odoo import http
from odoo.http import request
from odoo.orm.fields_misc import Json


class ModelDataController(http.Controller):

    @http.route('/js', website=True, auth='public')
    def modelDataShownMethod(self):
        # return "Hello Models"
        # model_name = self.pool.get('ir.model').search(cr, uid, [('modules','ilike','device_management')])
        # model_name = [1,2,3,4]

        model_name = request.env['ir.model'].sudo().search([
            ('model', 'like', 'device'),
        ])

        # for rendering the website page we will request to render that specific webpage we want
        return request.render("device_management.model_view_template", {
            'models': model_name
        })

    @http.route('/website_sale/addModuleInfo', type='json', website=True, auth='public')
    def modelSpecifcDataShown(self, model_name):
        print(f"The model I recieved is {model_name}")

        records = request.env[model_name].sudo().search_read([], ['id', 'display_name'])
        # sudo() means ignore access rights / record rules. if the public user does not have permission, Odoo will still fetch the data.
        return {
            'records': records,
        }

    @http.route('/website_sale/getUrlInfo', type='json', website=True, auth='public')
    def getSpecificUrl(self, model_name):
        domain = [('res_model', '=', model_name)]

        action_id = request.env['ir.actions.act_window'].sudo().search(domain).id

        return action_id
