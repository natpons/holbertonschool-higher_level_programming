// Fetches and lists the title for all movies by using this URL with  JQuery API
// All movie titles must be list in the HTML tag UL#list_movies
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    const list = data.results;
    for (const i in data.results) {
      $('#list_movies').append('<li>' + list[i].title + '</li>');
    }
  }
  );
});
