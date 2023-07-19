const axios = require('axios');
const jsdom = require("jsdom");
const fs = require("fs");
const {JSDOM} = jsdom;

const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
const getDaysInMonth = (month, year) => new Date(year, month, 0).getDate();

const baseURL = "https://nakedsecurity.sophos.com/";

const main = async () => {
    let successURL;

    if (fs.existsSync('success-urls.txt'))
        successURL = fs.readFileSync('success-urls.txt').toString().split('\n');
    else
        successURL = []

    for (let year = 2020; year <= 2021; year++) {
        for (let month = 1; month <= 12; month++) {
            for (let day = 1; day <= getDaysInMonth(month, year); day++) {

                const dateString = year +
                    "/" + String(month).padStart(2, '0') +
                    "/" + String(day).padStart(2, '0');

                const url = baseURL  + dateString;

                if (successURL.includes(url))
                    continue;

                try {
                    const response = await axios.get(url);
                    // console.log(response.data);
                    const dom = new JSDOM(response.data);
                    const document = dom.window.document;
                    const elements = document.getElementsByTagName('a');
                    for (const element of elements) {
                        // console.log(element.href);
                        const articleURL = element.href;
                        if (articleURL.includes(dateString) && !articleURL.endsWith(dateString)) {
                            fs.appendFileSync('article-urls.txt', articleURL + '\n');
                        }
                    }

                    fs.appendFileSync('success-urls.txt', url + '\n');
                    successURL.push(url);
                    // console.log(element["0"].innerHTML);
                } catch (e) {
                    fs.appendFileSync('failed-urls.txt', url + '\n');
                }
                // break;

                await delay(100);
            }
        }
    }
}

main();
