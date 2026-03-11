/** @odoo-module **/

import { Interaction } from '@web/public/interaction';
import { registry } from '@web/core/registry';
import { rpc } from "@web/core/network/rpc";

export class ShowModelInfo extends Interaction {
    static selector = '.website_model_view';

    dynamicContent = {
        'select.js_model_click' : {'t-on-change': this.showModelInformation},
    };

        setup() {
            console.log("Setup func");
        }
        start() {
            console.log("Start func");
        }

    async showModelInformation(ev){
        console.log(ev.target.value); //model name
        let model_name = ev.target.value;

            const modelNameInfo = await rpc(
                '/website_sale/addModuleInfo',
                {
                    model_name : model_name,
                }
            );

            console.log(modelNameInfo)
//
//      const section = this.el.querySelector('#records_section');
//        if (!section) return; // agar element abhi na ho
//
//        section.innerHTML = ''; // purana data clear
//
//        modelNameInfo.field_ids.forEach(field => {
//            const p = document.createElement('p');
//            p.textContent = field[1]; // field name
//            section.appendChild(p);
//        });
         const section = this.el.querySelector('#records_section');
            if (!section) return;

            section.innerHTML = '';

            modelNameInfo.forEach(record => {
                const p = document.createElement('p');
                p.textContent = record.display_name;
                section.appendChild(p);
            });
    }
}


registry.category('public.interactions').add('device_management.model_view_template', ShowModelInfo);
