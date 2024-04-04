// tráfego gerado por IP de origem

const generatedTrafficPerSource = () => {
	const traffic = echarts.init(document.getElementById('generated-traffic-per-source'),);

	fetch('http://localhost:8000/reports')
		.then(response => response.json())
		.then(data => {
				const option = {
					title: {
						text: 'Tráfego gerado por IP de origem'
					},
					tooltip: {},
						xAxis: {
							data: Object.keys(data.sourceIps)
					},
					yAxis: {},
					series: [
						{
							name: 'Tráfego gerado',
							type: 'bar',
							data: Object.values(data.sourceIps)
						}
					]
				};
				traffic.setOption(option);
		})
		.catch(error => console.error('Erro ao acessar os dados:', error));
}

export default generatedTrafficPerSource;