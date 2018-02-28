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
                        var data = [];
                        console.log(result.instants);
                        console.log(typeof (result));
                        result.instants.forEach((instant) => {
                            data.push({name: 'temperatura',
                                       time: instant.timestamp,
                                       value: instant.temperature
                                      });
                        });
                        console.log(data);
                        d3plus.viz()
                            .container('#viz') // container DIV to hold the visualization
                            .data(data) // data to use with the visualization
                            .type('line') // visualization type
                            .id('name') // key for which our data is unique on
                            .text('name') // key to use for display text
                            .y('value') // key to use for y-axis
                            .x('time') // key to use for x-axis
                            .draw(); // finally, draw the visualization!
                    },
                    failure: function(result) {
                        console.log('Error on ajax request');
                        console.log(result);
                    }
                });
            }
        });
    });
});


