// acessos por IP de destino

const visitsPerDestination = () => {
	const visits = echarts.init(document.getElementById('visits-per-destination'),);

	fetch('http://localhost:8000/reports')
		.then(response => response.json())
		.then(data => {
				const option = {
						title: {
								text: 'Acessos por IP de destino'
						},
						tooltip: {},
						xAxis: {
								data: Object.keys(data.destinationIps)
						},
						yAxis: {},
						series: [
								{
										name: 'Número de acessos',
										type: 'bar',
										data: Object.values(data.destinationIps)
								}
						]
				};
				visits.setOption(option);
		})
		.catch(error => console.error('Erro ao acessar os dados:', error));
}

export default visitsPerDestination;