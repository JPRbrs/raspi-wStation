var app = new Ractive({
    el: '#output',
    template: '#template',
    data: {
        foo: 'test'
        }
});

var month_mode;

function plot_data(canvas_id, xdata, in_data, out_data, label) {
    var ctx = document.getElementById(canvas_id);
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: xdata,
            datasets: [{
                fill: false,
                lineTension: 0.23,
                label: 'indoor ' + label,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: in_data,
            }, {
                fill: false,
                lineTension: 0.23,
                label: 'outdoor ' + label,
                backgroundColor: 'rgb(255, 99, 255)',
                borderColor: 'rgb(255, 99, 255)',
                data: out_data,
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true,
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
    var out_temp = [];
    var out_hum = [];

    result.instants.forEach((instant) => {
        time.push(instant.timestamp);
        temp.push(instant.temperature);
        hum.push(instant.humidity);
    });
    result.outdoor_instants.forEach((out_instant) => {
        out_temp.push(out_instant.temperature);
        out_hum.push(out_instant.humidity);
    });

    var data = {time: time, temp: temp, hum: hum, out_temp: out_temp, out_hum: out_hum};
    return data;
}


$(document).ready(function() {
    $('#loadingDiv').hide();
    $('#month_mode').click(function() {
        month_mode = $('#month_mode').is(':checked');
    });
    $(function() {
        $('#daypicker').datepicker({
            dateFormat: 'yy-mm-dd',
            changeMonth: true,
            changeYear: true,
            showButtonPanel: true,
            onSelect: function (date) {
                $('#loadingDiv').show();
                $('#hum_chart').hide();
                $('#temp_chart').hide();
                $.ajax({
                    type: 'POST',
                    url: month_mode ? '/get_month_ajax' : '/get_day_ajax',
                    data: JSON.stringify({date: date}),
                    contentType: 'application/json;charset=UTF-8',
                    success: function(result) {
                        $('#hum_chart').show();
                        $('#temp_chart').show();
                        $('#loadingDiv').hide();
                        var data = format_data(result);
                        plot_data('temp_chart', data['time'], data['temp'],
                                  data['out_temp'], 'temperature');
                        plot_data('hum_chart', data['time'], data['hum'],
                                  data['out_hum'], 'humidity');
                    }
                });
            }
        });
    });
});
