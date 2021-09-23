var ticker;
function setup() {
    createCanvas(200,200);
    loadJSON('https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=3HuGvR5WMK3NuuWIUYfacONthB5wAAex');
}

function gotData(data) {
    println(data);
}

function draw() {
    background(0);
}