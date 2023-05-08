
function parseJSON(jsonString) {
    const json = JSON.parse(jsonString);
  
    function parseNode(node) {
      const parsedNode = {
        data: node.data,
        loc: node.loc,
        children: []
      };
  
      if (node.children && Array.isArray(node.children)) {
        node.children.forEach(child => {
          const parsedChild = parseNode(child);
          parsedNode.children.push(parsedChild);
        });
      }
  
      return parsedNode;
    }
  
    return parseNode(json);
  }
  
  const parsedData = parseJSON(jsonString);
  console.log(parsedData);

     
  const svg = d3.select("#visualize")
  .append("svg");


  const circles = svg.selectAll("circle")
    .data(parsedData)
    .enter()
    .append("circle")
    .attr("cx", d => d['loc'][0] * 50) // Access 'loc' property using d.loc
    .attr("cy", d => d['loc'][1] * 50) // Access 'loc' property using d.loc
    .attr("r", 10)
    .style("fill", "steelblue");

 function createCircles(parent, nodes) {
        const circles = parent.selectAll("circle")
          .data(nodes)
          .enter()
          .append("circle")
          .attr("cx", d => d.loc[0] * 50)
          .attr("cy", d => d.loc[1] * 50)
          .attr("r", 10)
          .style("fill", "steelblue");
          
        const texts = svg.selectAll("text")
          .data(data)
          .enter()
          .append("text")
          .attr("x", d => d.loc[0] * 50)
          .attr("y", d => d.loc[1] * 50)
          .attr("dy", "0.35em")
          .text(d => d.data)
          .style("text-anchor", "middle")
          .style("fill", "white");
    
        nodes.forEach(node => {
          if (node.children.length > 0) {
            createCircles(parent, node.children);
          }
        });
      }
    
      createCircles(svg, data);