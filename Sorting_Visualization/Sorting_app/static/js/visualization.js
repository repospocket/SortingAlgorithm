function renderVisualization(json) {

    console.log(json);
    const data = JSON.parse(json);
    console.log(data);

  const svg = d3.select("#visualize")
  .append("svg");


  function createCircles(parent, node, parentLoc = [200, 50]) {

  

    const circle = parent.append("circle")
      .attr("cx", parentLoc[0] + node.loc[0] * 50)
      .attr("cy", parentLoc[1] + node.loc[1] * 50)
      .attr("r", 20)
      .style("fill", "steelblue");
    
    const text = parent.append("text")
      .attr("x", parentLoc[0] + node.loc[0] * 50)
      .attr("y", parentLoc[1] + node.loc[1] * 50)
      .attr("dy", "0.35em")
      .text(node.data)
      .style("text-anchor", "middle")
      .style("fill", "black");
      

    node.children.forEach(child => {
      createCircles(parent, child, [parentLoc[0] + node.loc[0] * 50, parentLoc[1] + node.loc[1] * 50 + 40]);
    });
  }

  createCircles(svg, data);
}
