document.getElementById('pdf-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var pdfFile = document.getElementById('pdf-file').files[0];
  var textInput = document.getElementById('text-input').value;
  var questionInput = document.getElementById('question-input').value;

  var formData = new FormData();
  formData.append('pdfFile', pdfFile);
  formData.append('textInput', textInput);
  formData.append('questionInput', questionInput);

  $.ajax({
    type: 'POST',
    url: 'https://docquery.kyutifer.repl.co/answer',
    data: formData,
    processData: false,
    contentType: false,
    success: function(response) {
      console.log(response)
      var answerContainer = document.getElementById('answer-container');
      answerContainer.innerHTML = '<p>Answer:</p><p class="answer">' + response['answer'] + '</p>';
    }
  });
});