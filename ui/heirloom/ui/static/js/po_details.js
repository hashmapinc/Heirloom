/** plot transactions on a map
 * 
 * This function takes the data array response of a successful GET call to the
 * transactions API, cleans the array for location transactions, and plots
 * the locations on a plotly map.
 * 
 * @param raw_transactions - array of transactions to plot on map. 
 */
function plot_map(raw_transactions) {
    // get location transactions
    txns = (raw_transactions
        .filter(txn => {return txn.type === "Location"})
        .sort((a,b) => { a.timestamp > b.timestamp ? 1 : -1 }));

    if (txns.length < 1) {
        return; // nothing to do with no transactions
    }

    // parse the transactions
    var labels = [];
    var hover_text = []
    var lons = [];
    var lats = [];
    txns.forEach(txn => {
        labels.push(txn.notes);
        hover_text.push(txn.timestamp + ': ' + txn.notes);
        var coordinates = JSON.parse(txn.value);
        lons.push(coordinates.lon);
        lats.push(coordinates.lat);
    });

    var data = [{
        type: 'scattergeo',
        mode: 'markers+text+lines',
        text: labels,
        hovertext: hover_text,
        textposition: "top left",
        customdata: txns,
        lon: lons,
        lat: lats,
        showlegend: false,
        line: {
            width: 2,
            color: 'rgb(96,125,139)'
        },
        marker: {
            color: 'rgb(255,82,82)'
        }
    }];

    var layout = {
        autosize: true,
        margin: {
            l: 25,
            r: 25,
            b: 25,
            t: 25,
        },
        geo: {
            showland: true,
            landcolor: 'rgb(250,250,250)',
            subunitcolor: 'rgb(217,217,217)',
            countrycolor: 'rgb(217,217,217)',
            countrywidth: 0.5,
            subunitwidth: 0.5,
            showcountries: true,
            scope: "usa"
        }
    };
    Plotly.newPlot('map-container', data, layout);
}

/**
 * handle a window resize by adjusting the plot size
 */
function on_resize() {
    var update = {
        margin: {
            l: 25,
            r: 25,
            b: 25,
            t: 25,
        }
    };

    Plotly.relayout('map-container', update);
};

/** handle a plotly click
 * 
 * @param data - plotly click data
 */
function on_plotly_click(data) {
    var txn = data.points[0].customdata;
    var txn_url = '/transaction/' + txn.id;
    window.open(txn_url);
}


// get the transactions query path
var curr_path = window.location.pathname;
var query_path = curr_path + '/transactions';

// query for transactions with the JS-native FETCH function and plot in map
fetch(
    query_path
).then((resp) => resp.json()
    .then(function (data) { 
        console.log("Successfully loaded transactions");
        plot_map(data); // plot the data
        window.onresize = on_resize; // wire up the onresize listener
        document.getElementById('map-container').on('plotly_click', on_plotly_click); // wire up the on click listener for plotly
    }).catch(function(err) {
        console.log("Error loading transactions")
        console.log(err);
    })
).catch(function(err) {
    console.log("Error loading transactions")
    console.log(err);
});