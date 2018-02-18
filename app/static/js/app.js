$(document).ready(function() {
    $.plot($('#placeholder'), [[[0, 0], [1, 1]]], {yaxis: {max: 1}});
    var button = $('#button');
    console.log('{{ day.instants }}');
    button.click(function() {
        console.log('hide!');
        $('#button').hide();
        $.post('/ajax_call', {
            text: 'texto',
        }).done(function(result) {
            console.log(result);
        }).fail(function(result) {
            console.log(result);
            console.log('fail');
        });
    });
});

