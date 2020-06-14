var tableData = data;
console.log(data);
var tbody=d3.select("tbody");
// loop and access each object in the table
tableData.forEach(function(row) {
    var tr=tbody.append("tr");
    var vals=Object.values(row);
    vals.forEach(function(val){
        var td=tr.append("td");
        td.text(val);
        });
}); 
var submitbutton =d3.select("#filter-btn");
submitbutton.on("click", function(){
    //clean the data of the current table
    tbody.html("");
    //get the value from the html
    var input=d3.select("#datetime").property("value");
    //use the input date to filter the data 
    var inputArray=tableData.filter(item => item.datetime ===input);
    //display
    inputArray.forEach(function(row) {
        var tr=tbody.append("tr");
        var vals=Object.values(row);
        vals.forEach(function(val){
            var td=tr.append("td");
            td.text(val);
            });
    });
});
