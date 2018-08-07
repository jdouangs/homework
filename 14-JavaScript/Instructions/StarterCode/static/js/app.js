// from data.js
var tableData = data;

// Console.log the alien sighting data from data.js
console.log(tableData);

// Get a reference to the table body
var tbody = d3.select("#ufo-table>tbody");

// Use d3 to update each cell's text with
// alien sighting report values
tableData.forEach(function(alienSighting) {
  console.log(alienSighting);
  let row = tbody.append("tr");
  Object.entries(alienSighting).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the alien sighting report object
    let cell = tbody.append("td");
    cell.text(value);
  })
});
        

// Select the Filter button
var filter = d3.select("#filter-btn");

filter.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);
  
  var filteredData = tableData.filter(date => date.datetime === inputValue);

  console.log(filteredData);
  tbody.selectAll('tr').remove();
  tbody.selectAll('td').remove();

  filteredData.forEach(function(alienSighting) {
    console.log(alienSighting);
    let row = tbody.append("tr");
    Object.entries(alienSighting).forEach(function([key, value]) {
      console.log(key, value);
      // Append a cell to the row for each value
      // in the alien sighting report object
      let cell = tbody.append("td");
      cell.text(value);
    })
  })
});


