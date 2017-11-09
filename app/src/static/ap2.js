var svgContainer = d3.select("body").append("svg")
                                    .attr("width", 200)
                                    .attr("height", 200);

var circles = svgContainer.selectAll("circle")
                          .data(data)
                          .enter()
                          .append("circle");

console.log(d3.select("body").append("svg").attr("width", 200).attr("height", 200).selectAll("circle").data(jsonCircles).enter().append("circle"));     