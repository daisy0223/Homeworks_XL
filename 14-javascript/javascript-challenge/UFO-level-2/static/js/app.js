var tableData = data;
console.log(data);
var tbody=d3.select("tbody");
// loop and access each object in the table
tableData.forEach(addrows);
function addrows(row) {
    var tr=tbody.append("tr");
    var vals=Object.values(row);
    vals.forEach(function(val){
        var td=tr.append("td");
        td.text(val);
        })
}
// define input variable
var filterdate =d3.select("#filter-btn");

//filter by input
filterdate.on("click", function(){
    tbody.html("");
    var enterInput=d3.select("#input").property("value");
    console.log(enterInput);
    var finalArray=tableData.filter(item => item.datetime ===enterInput||
                                    item.city===enterInput||
                                    item.state ===enterInput||
                                    item.country ===enterInput||
                                    item.shape ===enterInput);
    console.log(finalArray);
    finalArray.forEach(addrows)
});


