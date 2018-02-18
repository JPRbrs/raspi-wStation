$(document).ready(function() {
    var button = $('#button');
    button.click(function() {
        console.log('hide!');
        $('#button').hide();
        $.post('/ajax_call', {
            text: 'texto',
        }).done(function(result) {
            console.log(result);
            var array = [];
            var x = 0;
            result.instants.forEach((instant) => {
                var timestamp = instant.timestamp.slice(-8);
                console.log(timestamp, instant.temperature);
                array.push([x, instant.temperature]);
                x += 1;
            });
            array = [array];
            $.plot($('#placeholder'), array);
        }).fail(function(result) {
            console.log(result);
            console.log('fail');
        });
    });
});
