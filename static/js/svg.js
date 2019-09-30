function change_color(i, j) {
	var element = document.getElementById(`${i}_${j}`)

	color = '#' + Math.floor(Math.random()*16777215).toString(16);
	element.setAttribute('fill', color);
}

window.addEventListener("load", function() {

	var jsonCircles  = [
		{ "x_axis": 30, "y_axis": 30, "radius": 20, "color" : "green" },
		{ "x_axis": 70, "y_axis": 70, "radius": 20, "color" : "purple"},
		{ "x_axis": 110, "y_axis": 100, "radius": 20, "color" : "red"}
	];

	var svgContainer = d3.select(".container-login100").append("svg").attr("width", 800).attr("height", 800);

	var circles = [];
	var x_coord = 100;
	var y_coord = 100;
	for (var i = 0; i < 4; i++) {
		x_coord = 100
		for (var j = 0; j < 4; j++) {
			color = '#' + Math.floor(Math.random()*16777215).toString(16);
			circles[i * 4 + j] = svgContainer.append("circle")
												.attr("cx", x_coord)
												.attr("cy", y_coord)
												.attr("r", 50)
												.attr('fill', color)
												.attr('id', `${i}_${j}`)
												.attr('onclick', `change_color(${i}, ${j})`);
			x_coord += 200
		}
		y_coord += 200
	}
});