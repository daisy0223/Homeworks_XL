// Store API endpoint inside url
var url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Perform a GET request to the query URL
d3.json(url, function(data) {
    console.log(url);
    var earthquakeData=data;
    // Once we get a response, send the data.features object to the createFeatures function
    createFeatures(earthquakeData);
  });

function createFeatures(earthquakeData) {
    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachFeature(feature, layer) {
      return new L.circle([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], {
        fillOpacity: 1,
        color: chooseColor(feature.properties.mag),
        fillColor: chooseColor(feature.properties.mag),
        radius:  markerSize(feature.properties.mag*2500) //increase the circle size by 2500
      });
    }
     // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeData, {
      pointToLayer: onEachFeature
    });
    console.log(earthquakes)
    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
};

function createMap(earthquakes) {

  // Define streetmap and darkmap layers
    var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
    });


    // Define a baseMaps object to hold our base layers
    var baseMaps = {
    "Street Map": streetmap,
    };

    // Create overlay object to hold our overlay layer
    var overlayMaps = {
    Earthquakes: earthquakes
    };

    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 3,
    layers: [streetmap, earthquakes]
    });

    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
    }).addTo(myMap);

    // Create a legend to display information about our map #activity 17.3.1 advanced
    var legend = L.control({position: "bottomright"});

    // When the layer control is added, insert a div with the class of "legend"
    legend.onAdd = function(map) {
      var div = L.DomUtil.create("div", "legend"),
      magnitudegrades=[1, 2, 3, 4, 5, 6];
      magnitudelables=["0-1", "1-2", "2-3", "3-4", "4-5", "5+"];
      colorblock = "&nbsp;&nbsp;&nbsp;&nbsp;"; //add four spaces
      for (var i=0; i < magnitudegrades.length; i++) {
        div.innerHTML += '<p><i style="background: ' + chooseColor(magnitudegrades[i]) + ';">' + 
        colorblock + '</i>&nbsp;&nbsp;' + magnitudelables[i] + '</p>';
      }
      return div;
    };
    // Add the info legend to the map
    legend.addTo(myMap);
};

// define a function to assign different colors based on earthquake magnitudes
function chooseColor(magnitude) {
  if (magnitude >5)
      return "red";
  if (magnitude >4)
      return "orange";
  if (magnitude >3)
      return "gold";
  if (magnitude >2)
      return "yellow";
  if (magnitude >1)
      return "yellowgreen"; 
  return "green";
};

function markerSize(magnitude) {
  return magnitude ;
};


