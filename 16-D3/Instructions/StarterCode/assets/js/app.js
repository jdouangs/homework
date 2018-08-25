// @TODO: YOUR CODE HERE!

// Add Chart parameters
var svgWidth = 960
var svgHeight = 500

var margin = {top: 20, right: 40, bottom: 100, left: 120};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper
var svg = d3
    .select("body")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import csv file
d3.csv("assets/data/data.csv", function(error, healthData) {
    if (error) throw error;

    console.log(healthData);
    console.log([healthData]);

    // Cast csv data as a number
    healthData.forEach(function(data) {
        data.poverty = +data.poverty;
        data.age = +data.age;
        data.income = +data.income;
        data.healthcare = +data.healthcare;
        data.obesity = +data.obesity;
        data.smokes = +data.smokes
    })

    // Create Scales

    var xLinearScale1 = d3.scaleLinear()
        .domain(d3.extent(healthData, d => d.poverty))
        .range([0, width]);

    var xLinearScale2 = d3.scaleLinear()
        .domain(d3.extent(healthData, d => d.age))
        .range([0, width]);
    
    var xLinearScale3 = d3.scaleLinear()
        .domain(d3.extent(healthData, d => d.income))
        .range([0, width]);

    var yLinearScale1 = d3.scaleLinear()
        .domain([0, d3.max(healthData, d => d.healthcare)])
        .range([height, 0]);

    var yLinearScale2 = d3.scaleLinear()
        .domain([0, d3.max(healthData, d => d.obesity)])
        .range([height, 0]);

    var yLinearScale3 = d3.scaleLinear()
        .domain([0, d3.max(healthData, d => d.smokes)])
        .range([height, 0]);

    var bottomAxis = d3.axisBottom(xLinearScale1)
    var leftAxis = d3.axisLeft(yLinearScale1)
        
    //Add x-axis
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis)

    //Add y-axis
    chartGroup.append("g")
        .call(leftAxis)


    //Add scatterplot generators
    var circlesGroup = chartGroup.selectAll("circle")
        .data(healthData)
        .enter()
        .append("circle")
        .attr("cx", d  => xLinearScale1(d.poverty))
        .attr("cy", d => yLinearScale1(d.healthcare))
        .attr("r", "10")
        .attr("fill", "lightblue")
        .attr("stroke-width", "1")
        .attr("stroke", "black")
        .attr("opacity", ".5")

    //Append axes titles
    chartGroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top + 20})`)
        .attr("text-anchor", "middle")
        .classed("demographic-text text", true)
        .text("In Poverty (%)");

    chartGroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top + 40})`)
        .attr("text-anchor", "middle")
        .classed("demographic-text text", true)
        .text("Age (Median)");

    chartGroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top + 60})`)
        .attr("text-anchor", "middle")
        .classed("demographic-text text", true)
        .text("Household Income (Median)");

    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 60)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Obese (%)");

    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 40)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Smokes (%)");

    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 80)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Lacks Healthcare (%)");

    // Initialize Tooltip
    var toolTip = d3.tip()
        .attr("class", "d3-tip")
        .offset([80, -60])
        .html(function(d) {
        return (`${d.state}<br> ${d.poverty}<br> ${d.healthcare}`);
        });
    
    // Create the tooltip in chartGroup
    chartGroup.call(toolTip);

    circlesGroup.on("mouseover", function(d) {
        toolTip.show(d);
    })

        .on("mouseout", function(d) {
            toolTip.hide(d)
        });

})