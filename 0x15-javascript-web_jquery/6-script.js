// Updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header with JQuery API
$('#update_header').click(function () {
  $('header').replaceWith('New Header!!!');
});
