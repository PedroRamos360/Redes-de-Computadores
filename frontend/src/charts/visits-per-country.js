// acessos por país de destino

const visitsPerCountry = () => {
	const visits = echarts.init(document.getElementById('visits-per-country'),);

	fetch('http://localhost:8000/reports')
		.then(response => response.json())
		.then(data => {
				const option = {
						title: {
								text: 'Acessos por país de destino'
						},
						tooltip: {},
						xAxis: {
								data: Object.keys(data.destinationCountries)
						},
						yAxis: {},
						series: [
								{
										name: 'Número de acessos',
										type: 'bar',
										data: Object.values(data.destinationCountries)
								}
						]
				};
				visits.setOption(option);
		})
		.catch(error => console.error('Erro ao acessar os dados:', error));
}

export default visitsPerCountry;