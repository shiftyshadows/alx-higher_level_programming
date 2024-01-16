document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      // Iterate through the results and append each title to the list
      $.each(data.results, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      $('#list_movies').append('<li>Error loading movies</li>');
    }
  });
});
