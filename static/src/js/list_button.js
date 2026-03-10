import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";
import { Component } from "@odoo/owl";

patch(ListController.prototype, {
    onClickMyButton() {
//             this.createRecord(); // performing the functionality of new button
//             let resModel = this.modelParams.config.resModel; // getting the models Parameters here in the data variable
             let moduleName = this.env.config.actionXmlId.split('.')[0];

            this.env.services.action.doAction({
                type: "ir.actions.act_window",
                name : "Module Name",
                res_model: "device.modulename.wizard",
                context : {
                    'default_moduleName' : moduleName,
                },
                views: [[false, "form"]],
                target : "new",
            });
       }
});









//confirmation dialog, notification, wizard



//custom method call when we click on "Global" button :
//     onClickMyButton() {
//             this.createRecord(); // performing the functionality of new button
//
//             let resModel = this.modelParams.config.resModel; // getting the models Parameters here in the data variable
//             let moduleName = resModel.split('.')[0];
//
//             console.log("hey my module name is :  ", moduleName);
////             console.log("hey my module name is :  ", data.config.resModel);
////             console.log("Object is :  ", data);
////             console.log("Active fields name :  ", data.config.activeFields.name);
//
////             console.log("hey my module name is :  ", data.config.resModel);
//
//    }
//}




//export class ListButton extends ListController{
//    onClickMyButton() {
//              return super.createRecord();
////        return executeButtonCallback(super().rootRef.el, () => super().createRecord());
////             console.log("hey my button ");
//    }
//}

