var XMLHttpRequest = require('xhr2');
var fs = require('fs');
const readline = require("readline")

const rl =
 readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let userInput = NaN;
rl.question("How many Nitro links do you want to generate?\n", function (string) {
    userInput = parseInt(string);

    if (!isNaN(userInput)) {
        for (let i = 0; i < userInput; i++) {
            const data = JSON.stringify({
                "partnerUserId": "50be31b1-7b8a-45cc-9022-0d2c7adbf0da"
            });
            
            const xhr = new XMLHttpRequest();
            xhr.withCredentials = true;
            
            xhr.addEventListener("readystatechange", function () {
                if (this.readyState === this.DONE) {
                console.log(this.responseText);
    
                var jsonData = JSON.parse(this.responseText);
                var tokenValue = jsonData.token || '';
                var finalString = 'https://discord.com/billing/partner-promotions/1180231712274387115/' + tokenValue + '\n';
    
                fs.appendFile('nitro.txt', finalString, function (err) {
                    if (err) throw err;
                    console.log(`Saved!`);
                });
                }
            });
            
            xhr.open("POST", "https://api.discord.gx.games/v1/direct-fulfillment");
            xhr.setRequestHeader("authority", "api.discord.gx.games");
            xhr.setRequestHeader("accept", "*/*");
            xhr.setRequestHeader("accept-language", "nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5");
            xhr.setRequestHeader("content-type", "application/json");
            xhr.setRequestHeader("origin", "https://www.opera.com");
            xhr.setRequestHeader("referer", "https://www.opera.com/");
            xhr.setRequestHeader("sec-ch-ua", "\"Chromium\";v=\"118\", \"Opera GX\";v=\"104\", \"Not=A?Brand\";v=\"99\"");
            xhr.setRequestHeader("sec-ch-ua-mobile", "?0");
            xhr.setRequestHeader("sec-ch-ua-platform", "\"Windows\"");
            xhr.setRequestHeader("sec-fetch-dest", "empty");
            xhr.setRequestHeader("sec-fetch-mode", "cors");
            xhr.setRequestHeader("sec-fetch-site", "cross-site");
            xhr.setRequestHeader("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0");
            
            xhr.send(data);
        }
    } else {
      console.log("Please enter a valid number.");
    }

    rl.close();
});