 // module aliases
var Engine = Matter.Engine,
Render = Matter.Render,
Bodies = Matter.Bodies,
Composite = Matter.Composite;

 // create an engine
var engine = Engine.create();

// create a renderer
var render = Render.create({
    element: document.body,
    engine: engine,
    options: {  
        wireframes: true,
      },
      label: 'dada'
        
    });

Render.run(render);

var ground = Bodies.rectangle(400, 610, 810, 60, {
    isStatic: true,
    render: {
      fillStyle: 'pink',
    }
  });

Composite.add(engine.world, [ground]);

var bodies = [];
var constraints = [];

var radius = 30;
var nodeBody = Bodies.circle(400, 210, radius,
    {isStatic: true
    }
    );
    nodeBody.label = 'root';

Composite.add(engine.world, [nodeBody]);


function renderMatterVisualization(json) {
    const data = JSON.parse(json);
    
    //const rootCircle = createCircle(400, 100, 100, dataStructure.children);

  }

// run the engine
Matter.Runner.run(engine);

function renderTextLabessl(body) {
    var ctx = render.context;  // Get the rendering context
    ctx.font = '12px Arial';   // Set the font style
    ctx.fillStyle = 'black';   // Set the fill color
  
    var position = body.position;
    var label = 'My Circle';  // The text label
  
    // Render the text label at the body's position
    ctx.fillText(label, position.x, position.y);
  }
   
function renderTextLabels() {
    var ctx = render.context;  // Get the rendering context
    ctx.font = '12px Arial';   // Set the font style
    ctx.fillStyle = 'white';   // Set the fill color
  
    // Loop through the bodies and render text labels
    Matter.Composite.allBodies(engine.world).forEach(function(body) {
      var position = body.position;
      var label = body.label;  // The text label
  
      // Render the text label at the body's position
      ctx.fillText(label, position.x -10, position.y);
    });
  }
  

  Matter.Events.on(render, 'afterRender', renderTextLabels);

   // renderTextLabessl(nodeBody);
