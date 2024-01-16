$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX request to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'GET',
      data: { lang: languageCode },
      success: function (data) {
        // Display the translation in the DIV#hello element
        $('#hello').text(data.hello);
      },
      error: function () {
        // Display an error message if the translation cannot be fetched
        $('#hello').text('Error fetching translation');
      }
    });
  });
});
