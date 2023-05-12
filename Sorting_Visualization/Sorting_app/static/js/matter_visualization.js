var renderContainer = document.getElementById("render-container");
var engine = Matter.Engine.create();
var render = Matter.Render.create({
  element: renderContainer,
  engine: engine,
  options: {
    width: 800,
    height: 600,
    wireframes: false,
    background: 'skyblue',
  }
});

var mouse = Matter.Mouse.create(render.canvas);
var mouseConstraint = Matter.MouseConstraint.create(engine, {
  mouse: mouse,
});

Matter.Runner.run(engine);
Matter.Render.run(render);

function renderArray(arr) {
  var renderedArray = arr.map(function (item) {
      return Array.isArray(item) ? renderArray(item) : item;
  });
  return "[" + renderedArray.join(", ") + "]";
}

function renderTextLabels(render) {
  var ctx = render.context;
  ctx.font = '20px Arial';
  ctx.fillStyle = 'black';

  Matter.Composite.allBodies(render.engine.world).forEach(function (body) {

    if (body.label) {

      var position = body.position;
      var label = body.label;

      // Update the text position relative to the body's position
      var textX = position.x - 3;
      var textY = position.y + 3;

      // Center the text horizontally
      var textWidth = ctx.measureText(label).width;
      textX -= textWidth / 2;

      // Render the text label at the updated position
      ctx.fillText(label, textX, textY);

    }
  });
}

function setupMouseEvents(circle) {

  render.canvas.addEventListener("mousedown", function (event) {
    if (event.target === render.canvas) {
      var mousePosition = mouse.position;
      if (Matter.Bounds.contains(circle.bounds, mousePosition)) {
        mouseConstraint.body = circle;
        Matter.Body.setStatic(circle, true);
      }
    }
  });

  render.canvas.addEventListener("mousemove", function (event) {
    if (mouseConstraint.body === circle) {
      var mousePosition = mouse.position;
      Matter.Body.setPosition(circle, mousePosition);
    }
  });

  render.canvas.addEventListener("mouseup", function (event) {
    mouseConstraint.body = null;
    Matter.Body.setStatic(circle, false);
  });
}

function renderNodes(data) {

  function createCircle(x, y, isStatic) {

    var circle = Matter.Bodies.circle(x, y, radius, { isStatic: isStatic });

    if (!isStatic) {
      Matter.Events.on(render, 'afterRender', function () {
        renderTextLabels(render);
      });
      setupMouseEvents(circle);
      Matter.World.add(engine.world, [circle, mouseConstraint]);
    } else {
      Matter.World.add(engine.world, [circle]);
    }

    return circle;
  }

  var radius = 30;
  var rootX = 400;
  var rootY = 100;
  var rootCircle = null; // Declare rootCircle variable
  rootCircle = createCircle(rootX, rootY, true); // Assign value to rootCircle
  rootCircle.label = '0';

  function createChildCircles(parent, children) {
    var angleStep = Math.PI * 2 / children.length;
    var distance = 100;

    children.forEach(function (child, index) {
      var angle = index * angleStep;
      var childX = parent.position.x + Math.cos(angle) * distance;
      var childY = parent.position.y + Math.sin(angle) * distance;
      var childCircle = createCircle(childX, childY, false);
      childCircle.label = child.digit || "0";

      Matter.World.add(engine.world, [
        Matter.Constraint.create({
          bodyA: parent,
          pointA: { x: 0, y: 0 },
          bodyB: childCircle,
          pointB: { x: 0, y: 0 },
          stiffness: 1,
          length: distance
        })
      ]);

      createChildCircles(childCircle, child.children);
    });
  }

  createChildCircles(rootCircle, data.children);
}
