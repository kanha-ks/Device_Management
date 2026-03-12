/** @odoo-module **/

import { Interaction } from '@web/public/interaction';
import { useService } from "@web/core/utils/hooks";
import { registry } from '@web/core/registry';
import { rpc } from "@web/core/network/rpc";


export class ShowModelInfo extends Interaction {
    static selector = '.website_model_view';

    dynamicContent = {
        'select.js_model_click' : {'t-on-change': this.showModelInformation},
    };

        setup() {
//            this.actionService = useService("action");
            console.log("Setup func");
        }
        start() {
            console.log("Start func");
        }

    //with this the main logic for printing the modelInformation on the record section
    onChangeModelSection(modelNameInfo, modelName){
//    debugger;
        const recordDropdownField = this.el.querySelector('.s_record_select');
        if (recordDropdownField) {
            recordDropdownField.innerHTML = '<option value=""> see records</option>';
//
            if(modelNameInfo){
                modelNameInfo['records'].forEach(
                record => { //iqoo, samsung...
                    const option = document.createElement('option'); //isse ham blank option element create kr rhe hai for further data insertion
                    option.value = record.id;

                    option.textContent = record.display_name;

                    recordDropdownField.appendChild(option);
                })
            }else{
                console.log("Model Information is empty")
            }
        }

         //now i am adding the functionality to specific
            const actionButton = this.el.querySelector('.s_action_button');

            recordDropdownField.onchange = function() {
                    if (recordDropdownField.value) {
                        actionButton.style.display = 'inline-block';
                    } else {
                        actionButton.style.display = 'none';
                    }
            }

//debugger;

     //now perfoming some action after clicking the button
         actionButton.onclick = async function() {
           const recordId = recordDropdownField.value; //model value from another dropdown

            if (recordId) {

                const actionId = await rpc(
                    '/website_sale/getUrlInfo',
                    {
                        model_name : modelName,
                    }
                );
                const baseUrl = window.location.origin; // I am getitng this with <- this eg: http://localhost:8019
                return window.open(
                  `${baseUrl}/odoo/action-${actionId}/${recordId}`,
                );
            }
          }
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

            //after getting all data we are calling this method mendatory
            this.onChangeModelSection(modelNameInfo, model_name);
            console.log(modelNameInfo['records'])
    }
}


registry.category('public.interactions').add('device_management.model_view_template', ShowModelInfo);










            //once we get the record id we will call rpc method and pass all the data to it
            // python controller fetch all the essentials info and send it back to the variable url
//
//            const actionId = rpc(
//                        '/website_sale/getUrlInfo',
//                        {
//                            model_name : modelName,
//                            record_id : recordId,
//                        }
//                    );


                // js hit that url
//                return window.open(targetUrl, '_blank');

//
//            this.actionService.doAction({
//                type: "ir.actions.act_window",
//                res_model: modelName,
//                res_id: parseInt(this.recordId),
//                views: [[false, "form"]],
//                target: "current",
//            });

                // Redirect to the Odoo form view
//                const baseUrl = window.location.origin; // eg: http://localhost:8019
//                const modelName =   recordDropdownField.model; // store model in data-model attribute
                // Redirect to form view URL
//                window.location.href = `${baseUrl}/web#id=${recordId}&view_type=form&model=${device}`;

//window.open(
//  `${baseUrl}/odoo/web#id=${recordId}&model=${modelName}&view_type=form`,
//);

//                     window.open(`${baseUrl}/odoo/action-519/${recordId}`, "_blank");



//the blank space is occur because i am not clearing the space first






//    document.getElementById('models_name').addEventListener('change', async function(ev) {
//    const model_name = ev.target.value;
//
//    // Call your backend route
//    const records = await rpc('/website_sale/addModuleInfo', { model_name });
//
//    const recordSelect = document.getElementById('record_select');
//
//    // Clear old options
//    recordSelect.innerHTML = '<option value="">Select a record</option>';
//
//    // Populate new options
//    records.forEach(record => {
//        const option = document.createElement('option');
//        option.value = record.id;
//        option.textContent = record.display_name;
//        recordSelect.appendChild(option);
//    });
//});



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



//         const section = this.el.querySelector('#records_section');
//            if (!section) return;
//
//            section.innerHTML = '';
//
//            modelNameInfo.forEach(record => {
//                const p = document.createElement('p');
//                p.textContent = record.display_name;
//                section.appendChild(p);
//            });