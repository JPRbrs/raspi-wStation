var app = new Ractive({
    el: '#output',
    template: '#template',
    data: {
        foo: 'test'
        }
});

function plot_data(canvas_id, xdata, ydata, label) {
    var ctx = document.getElementById(canvas_id);
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: xdata,
            datasets: [{
                lineTension: 0.23,
                label: label,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: ydata,
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:false,
                    }
                }],
                xAxes: [{
                    ticks: {}
                }],
            }
        }
    });
}

function format_data(result) {
    var time = [];
    var temp = [];
    var hum = [];
    result.instants.forEach((instant) => {
        time.push(instant.timestamp.slice(11, 16));
        temp.push(instant.temperature);
        hum.push(instant.humidity);
    });

    var data = {time: time, temp: temp, hum: hum};
    return data;
}

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
                        var data = format_data(result);
                        plot_data('temp_chart', data['time'], data['temp'],
                                  'temperature');
                        plot_data('hum_chart', data['time'], data['hum'], 'humidity');
                    }
                });
            }
        });
    });
});
