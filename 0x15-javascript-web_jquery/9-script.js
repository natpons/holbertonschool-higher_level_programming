// Fetches from url and displays the value of hello from that fetch in the HTML tag DIV#hello with JQuery API
// The translation of hello must be displayed in the HTML tag DIV#hello
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});
