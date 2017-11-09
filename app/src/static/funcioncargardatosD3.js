

function cargarDatos(){

	d3.json("/getMyJson", function(err, data){
		
		if(!err){
			datos = data;
			console.log(datos[0]);	

		}
		else{
			console.error("no cargó :(");d
		}

		graficar();

	})

}