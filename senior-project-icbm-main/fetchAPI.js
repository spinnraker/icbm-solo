var ticker;

var original = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=3HuGvR5WMK3NuuWIUYfacONthB5wAAex";

var api = "https://api.polygon.io/v2/aggs/ticker/";
var dataRange = "/range/1/day/2020-06-01/2020-06-17?";
var apiKey = "apiKey=3HuGvR5WMK3NuuWIUYfacONthB5wAAex";

var input; //this is used later to let user input stock ticker

function setup() {
    createCanvas(1000,1000);

    var button = select('#submit');
    button.mousePressed(query);

    input = select('#ticker');

}

function query() {
    var url = api + input.value() + dataRange + apiKey; //url is strung together to call api
    loadJSON(url, gotData);
}

function gotData(tickerInfo) {
    ticker = tickerInfo;
}

//this function needs to be debugged
function printData() {
    background(0);
    console.log(tickerInfo.h) //high
    console.log(tickerInfo.l) //low
    console.log(tickerInfo.o) //open
    console.log(tickerInfo.c) //close
}

//fetch() is a more elegant API call that I was trying to use, but kept having issues. Would like to integrate this or AXIOS later
/*fetch("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=3HuGvR5WMK3NuuWIUYfacONthB5wAAex")
.then(response => {
    return response.json();
})
.then(users => {
    console.log(users);
});*/