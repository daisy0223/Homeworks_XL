// @TODO: YOUR CODE HERE!
var svgWidth = 800;
var svgHeight = 600;

// Define the chart's margins as an object
var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 100
  }; 
// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// create an SVG element
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append a group area, then set its margins
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Load csv data
d3.csv("/assets/data/data.csv").then(function(hmData) {
  console.log(hmData);
  // cast the data from the csv as numbers
  hmData.forEach(function(data) {
    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare;
  });

// Create a scale for your independent (x) coordinates
var xScale=d3.scaleLinear()
              .domain([8.1, d3.max(hmData, d=> d.poverty)+2]) //change domain to be same as the example pic
              .range([0, chartWidth]);
// Create a scale for your dependent (y) coordinates
var yScale = d3.scaleLinear()
              .domain([4.1, d3.max(hmData, d => d.healthcare)+2])
              .range([chartHeight,0]);

// create axes
var yAxis = d3.axisLeft(yScale); 
var xAxis = d3.axisBottom(xScale).ticks();

// set x to the bottom of the chart
chartGroup.append("g")
  .attr("transform", `translate(0, ${chartHeight})`)
  .call(xAxis);

// set y to the y axis
chartGroup.append("g")
  .call(yAxis);
//apply values as circles
chartGroup.selectAll("circle")
      .data(hmData)
      .enter()
      .append("circle")
      .attr("cx", d => xScale(d.poverty))
      .attr("cy", d => yScale(d.healthcare))
      .attr("r",8)
      .style("fill", "#3090C7")
      .attr("opacity",'.7');
 //add state info into each circle
  chartGroup.selectAll("#scatter")
    .data(hmData)
    .enter()
    .append("text")
    .text(d=>d.abbr)
    .attr("x", d => xScale(d.poverty))
    .attr("y", d => yScale(d.healthcare)) 
    .attr("font-size", "7px")
    .attr("text-anchor", "middle")
    .style("fill", "white");

  //lableGroup
  chartGroup.append("g")
    .attr("transform", `translate(${chartWidth/2}, ${chartHeight+20})`);

  //text label for the x axis
  chartGroup.append("text")
    .attr("y", chartHeight +1.5 *margin.bottom/2)
    .attr("x", chartWidth/ 2)
    .classed("axis-text", true)
    .text("In Poverty (%)");

  //text label for the y axis
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0-margin.left)
    .attr("x", 0 - (chartHeight / 2))
    .attr("dy", "1em")
    //.style("text-anchor", "middle") 
    .classed("axis-text", true)
    .text("Lacks Healthcare (%)");
});




