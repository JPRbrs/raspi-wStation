$(document).ready(function() {
    $(function() {
        $('#datepicker').datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function (date) {
                $.ajax({
                    type: 'POST',
                    url: '/ajax_call',
                    data: JSON.stringify({date: date}),
                    contentType: 'application/json;charset=UTF-8',
                    success: function(result) {
                        var array = [];
                        var x = 0;
                        result.instants.forEach((instant) => {
                            var timestamp = instant.timestamp.slice(-8);
                            console.log(instant.timestamp, instant.temperature);
                            array.push([x, instant.temperature]);
                            x += 1;
                        });
                        array = [array];
                        console.log(array);
                        $.plot($('#placeholder'), array);
                    },
                    failure: function(result){
                        console.log(result);
                    }
                });
            }
        });
    });
});

