$(document).ready(function () {
  function fetchTranslation () {
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
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when Enter is pressed in the language code input
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      // 13 is the ASCII code for Enter
      fetchTranslation();
    }
  });
});
