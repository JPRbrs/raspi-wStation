var ractive = new Ractive({
    target: '#output',
    template: '#template',
    data: {
     items: [
         {page:' outdoor', image: '/static/images/outdoor.png'},
         {page: 'buses', image: '/static/images/bus.png'},
         {page: 'home_weather', image: '/static/images/house.png'},
         {page: 'video', image: '/static/images/camera.png'}
    ]
  },
});

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
    $(function() {
        $('#daypicker').datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function (date) {
                $.ajax({
                    type: 'POST',
                    url: '/get_day_ajax',
                    data: JSON.stringify({date: date}),
                    contentType: 'application/json;charset=UTF-8',
                    success: function(result) {
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
     $('#monthpicker').datepicker({
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        dateFormat: 'yy-mm-dd',
         onClose: function(date) {
             $(this).datepicker('setDate', date);
             $.ajax({
                 type: 'POST',
                 url: '/get_month_ajax',
                 data: JSON.stringify({date: date}),
                 contentType: 'application/json;charset=UTF-8',
                 success: function(result) {
                     var data = format_data(result);
                     plot_data('temp_chart', data['time'], data['temp'],
                               data['out_temp'], 'temperature');
                     plot_data('hum_chart', data['time'], data['hum'],
                               data['out_hum'], 'humidity');
                 }
             });
         },
     });
});
