String.prototype.endsWith = function(suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
};

String.prototype.startsWith = function(prefix) {
    return this.lastIndexOf(prefix, 0) === 0
};


// yaxis formatting
function formatmoney(symbol, v, axis) {
    return symbol + v.toFixed(axis.tickDecimals);
}
function formatshare(v, axis) {
    return v.toFixed(axis.tickDecimals) + "%";
}
function formatcount(v, axis) {
    return v.toFixed(axis.tickDecimals);
}


// function format_chartdata(chart_data) {
//     for (var series in chart_data) {
//         for (var p in series.data) {
//             // date = new Date(date);
//             p[0] = get_timestamp(p[0]);
//         }
//     }
// }

// placeholder for feature formatter
var getFormatter = null;

// placeholder for current line-chart
var lineChart = null;


var linechartOptions = {
    series: {
        lines: { show: true },
        points: { show: true }
    },
    grid: {
        hoverable: true,
        clickable: true
    },
    xaxis: {
        mode: "time",
        tickLength: 5,
        timeformat: "%d/%m",
        minTickSize: [1, "day"]
    },
    yaxis: {
        min: null,
    },
    legend: { show: false },        
    selection: { mode: "xy" }
};

var piechartOptions = {
    series: {
        pie: {
            show: true,
            label: { show: false },
            // highlight: { opacity: 0.0 }
        }
    },
    grid: {
        hoverable: true,
        clickable: true,
    },
    legend: { show: false },
};

var currentLinechartData = null;

function initCurrentLinechartData() {
    data = new Array();
    for (var feature in linechartData) {
        data[feature] = linechartData[feature];
    }
    currentLinechartData = data;
}

// bindings for switching linechart feature when clicking on piechart titles
function drawLinechart(options) {
    if (!currentLinechartData)
        currentLinechartData = initCurrentLinechartData();
    options.yaxis.tickFormatter = getFormatter(chosen_feature);
    linechart = $.plot($("#placeholder.linechart"), currentLinechartData[chosen_feature], options);
    return linechart;
}


function drawPiecharts(piechartdata) {
    for (var feature in piechartdata) {
       $.plot($("#placeholder." + feature), piechartdata[feature], piechartOptions);
    }
}


// add tooltips to line chart points
function showTooltip(x, y, contents, color) {
    $('<div id="tooltip">' + contents + '</div>').css( {
        position: 'absolute',
        display: 'none',
        top: y + 5,
        left: x + 5,
        border: '1px solid #fdd',
        padding: '2px',
        color: 'white',
        'background-color': color,
        'background-opacity': 0.5,
        // opacity: 0.80
    }).appendTo("body").fadeIn(200);
}



// toggle hotel on/off when clicking on piechart portion
function updateVisibleHotels() {
    for (var feature in linechartData) {
        currentLinechartData[feature] = [];
        var linedata = linechartData[feature];
        var nHotels = linedata.length;
        for (var i = 0; i < nHotels; i++) {
            var hoteldata = linedata[i];
            var hotelname = linedata[i].label;
            var show = (visibleHotelColors[hotelname] != "#666666");
            if (show)
                currentLinechartData[feature].push(hoteldata);
        }        
    }

    for (var feature in piechartData) {
        nHotels = piechartData[feature].length;
        for (var i = 0; i < nHotels; i++) {
            pieslice = piechartData[feature][i];
            pieslice.color = visibleHotelColors[pieslice.label];
        }
    }

    drawLinechart(linechartOptions);
    drawPiecharts(piechartData);
}

var hotelColors = null;

var visibleHotelColors = null;
// we set to grey (#666666) the hotels we don't
// want to see in the linechart.
// in that way, the same array serves for coloring the piecharts

function initHotelArray() {
    visibleHotelColors = new Array();
    hotelColors = new Array();
    // TODO: find a better way to fetch first feature data
    var linedata;
    for (feature in linechartData) {
        linedata = linechartData[feature];
        break;        
    }
    var nHotels = linedata.length;
    for (var i = 0; i < nHotels; i++) {
        var hotelname = linedata[i].label;
        visibleHotelColors[hotelname] = linedata[i].color;
        hotelColors[hotelname] = linedata[i].color;
    }

}

function toggleHotel(hotelname) {
    if (visibleHotelColors[hotelname] == "#666666")
        visibleHotelColors[hotelname] = hotelColors[hotelname];
    else
        visibleHotelColors[hotelname] = "#666666";
    updateVisibleHotels();
}

