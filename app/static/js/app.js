$(document).ready(function() {
    var button = $('#button');
    button.click(function() {
        console.log('hide!');
        $('#button').hide();
        $.post('/ajax_call', {
            text: 'texto',
        }).done(function(result) {
            console.log(result.result);
        }).fail(function(result) {
            console.log(result);
            console.log('fail');
        });
    });
});
