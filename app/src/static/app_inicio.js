var datos = [1,2,4,5,7,8,1223,24,64,89,100, 200, 300, 400];

var x = d3.scaleLinear()
			.domain([0, d3.max(datos)])
			.range([0, 510]) // 500 pixeles
		
function graficar(){
	d3.select(".barras")
		.selectAll("div")
		.data(datos)
		.enter().append('div')
		.style("width", function(d){

			return x(d) + "px"
		})
		.text(function(d){
			return d 
		})
		

}

