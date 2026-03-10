import { Interaction } from '@web/public/interaction';
import { registry } from '@web/core/registry';


export class ShowModelInfo extends Interaction {
    static selector = '.website_model_view';

    dynamicContent = {
        'select.js_model_click' : {'t-on-click': this.showModelInformation},
    };

        setup() {
            console.log("Setup func");
        }
        start() {
            console.log("Start func");
        }

    showModelInformation(){
        console.log("Hey Selector worked !!")
    }
}


registry.category('public.interactions').add('device_management.model_view_template', ShowModelInfo);
