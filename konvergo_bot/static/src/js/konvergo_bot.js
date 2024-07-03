odoo.define("konvergo_bot", function (require) {
"use strict";

var MailBotService = require("mail_bot.MailBotService");

var odooBot = "OdooBot";
var konvergoBot = "Mon Key Bot";

MailBotService.include({
    getPreviews(filter) {
        var previews = this._super();
        previews.forEach((preview) => {
            replaceBotName(preview);
            replaceBotLogo(preview);
        });
        return previews;
    },
});

function replaceBotName(preview){
    while(preview.title && preview.title.indexOf(odooBot) !== -1){
        preview.title = preview.title.replace(odooBot, konvergoBot);
    }
}

function replaceBotLogo(preview){
    if(preview.imageSRC && preview.imageSRC.endsWith("odoobot.png")){
        preview.imageSRC = "/konvergo_bot/static/src/img/konvergo_bot.png";
    }
}

});
