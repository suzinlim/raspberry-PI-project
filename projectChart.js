// Chart 객체에 넘겨줄 차트에 대한 정보들을 정의한 객체. 명품 html5의 7장 프로토타입 참고
var config = {
	// type은 차트 종류 지정
	type: 'line', /* line 등으로 바꿀 수 있음 */

	// data는 차트에 출력될 전체 데이터 표현
	data: {
		// labels는 배열로 데이터의 레이블들
		labels: [],

		// datasets 배열로 이 차트에 그려질 모든 데이터 셋 표현. 아래는 그래프 1개만 있는 경우
		datasets: [{
			label: '조도',
			backgroundColor: 'green',
			borderColor: 'rgb(255, 99, 132)',
			borderWidth: 2,
			data: [], /* 각 레이블에 해당하는 데이터 */
			fill : false, /* 그래프 아래가 채워진 상태로 그려집니다. 해보세요 */
		}]
	},

	//  차트의 속성 지정
	options: {
		responsive : false, // 크기 조절 금지
		scales: { /* x축과 y축 정보 */
			xAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '시간' },
			}],
			yAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '조도' }
			}]
		}
	}
};


var config1 = {
	// type은 차트 종류 지정
	type: 'line', /* line 등으로 바꿀 수 있음 */

	// data는 차트에 출력될 전체 데이터 표현
	data: {
		// labels는 배열로 데이터의 레이블들
		labels: [],

		// datasets 배열로 이 차트에 그려질 모든 데이터 셋 표현. 아래는 그래프 1개만 있는 경우
		datasets: [{
			label: '온도',
			backgroundColor: 'red',
			borderColor: 'red',
			borderWidth: 2,
			data: [], /* 각 레이블에 해당하는 데이터 */
			fill : false, /* 그래프 아래가 채워진 상태로 그려집니다. 해보세요 */
		},
        {
			label: '습도',
			backgroundColor: 'blue',
			borderColor: 'blue',
			borderWidth: 2,
			data: [], /* 각 레이블에 해당하는 데이터 */
			fill : false, /* 그래프 아래가 채워진 상태로 그려집니다. 해보세요 */
		}]
	},

	//  차트의 속성 지정
	options: {
		responsive : false, // 크기 조절 금지
		scales: { /* x축과 y축 정보 */
			xAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '시간' },
			}],
			yAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '측정값' }
			}]
		}
	}
};

var config2 = {
	// type은 차트 종류 지정
	type: 'line', /* line 등으로 바꿀 수 있음 */

	// data는 차트에 출력될 전체 데이터 표현
	data: {
		// labels는 배열로 데이터의 레이블들
		labels: [],

		// datasets 배열로 이 차트에 그려질 모든 데이터 셋 표현. 아래는 그래프 1개만 있는 경우
		datasets: [{
			label: '무대와 관람객 간 거리',
			backgroundColor: 'yellow',
			borderColor: 'rgb(255, 99, 132)',
			borderWidth: 2,
			data: [], /* 각 레이블에 해당하는 데이터 */
			fill : false, /* 그래프 아래가 채워진 상태로 그려집니다. 해보세요 */
		}]
	},

	//  차트의 속성 지정
	options: {
		responsive : false, // 크기 조절 금지
		scales: { /* x축과 y축 정보 */
			xAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '시간' },
			}],
			yAxes: [{
				display: true,
				scaleLabel: { display: true, labelString: '거리(cm)' }
			}]
		}
	}
};

var ctx = null
var chart = null
var chart1 = null
var chart2 = null
var LABEL_SIZE = 20; // 차트에 그려지는 데이터의 개수 
var tick = 0; // 도착한 데이터의 개수임, tick의 범위는 0에서 99까지만 
function lightDrawChart() {
	ctx = document.getElementById('canvas_light').getContext('2d');
	chart = new Chart(ctx, config);
	init(chart);
} // end of drawChart()

function temnhumDrawChart() {
	ctx = document.getElementById('canvas_temnhum').getContext('2d');
	chart1 = new Chart(ctx, config1);
	init(chart1);
} // end of drawChart()

function distanceDrawChart() {
	ctx = document.getElementById('canvas_distance').getContext('2d');
	chart2 = new Chart(ctx, config2);
	init(chart2);
} // end of drawChart()


// chart의 차트에 labels의 크기를 LABEL_SIZE로 만들고 0~19까지 레이블 붙이기
function init(chart) {
	for(let i=0; i<LABEL_SIZE; i++) {
		chart.data.labels[i] = i;
	}
	chart.update();
}

function addLightChartData(value) {
	tick++; // 도착한 데이터의 개수 증가
	tick %= 100; // tick의 범위는 0에서 99까지만. 100보다 크면 다시 0부터 시작
	let n = chart1.data.datasets[0].data.length; // 현재 데이터의 개수
	if(n < LABEL_SIZE) 
		chart.data.datasets[0].data.push(value);
	else {
		// 새 데이터 value 삽입
		chart.data.datasets[0].data.push(value);
		chart.data.datasets[0].data.shift();

		// 레이블 삽입
		chart.data.labels.push(tick);
		chart.data.labels.shift();
	}
	chart.update();
}

function addTemChartData(value) {
	tick++; // 도착한 데이터의 개수 증가
	tick %= 100; // tick의 범위는 0에서 99까지만. 100보다 크면 다시 0부터 시작
	let n = chart1.data.datasets[0].data.length; // 현재 데이터의 개수
	if(n < LABEL_SIZE) 
		chart1.data.datasets[0].data.push(value);
	else {
		// 새 데이터 value 삽입
		chart1.data.datasets[0].data.push(value);
		chart1.data.datasets[0].data.shift();

		// 레이블 삽입
		chart1.data.labels.push(tick);
		chart1.data.labels.shift();
	}
	chart1.update();
}

function addHumChartData(value) {
	tick++; // 도착한 데이터의 개수 증가
	tick %= 100; // tick의 범위는 0에서 99까지만. 100보다 크면 다시 0부터 시작
	let n = chart1.data.datasets[1].data.length; // 현재 데이터의 개수
	if(n < LABEL_SIZE) 
		chart1.data.datasets[1].data.push(value);
	else {
		// 새 데이터 value 삽입
		chart1.data.datasets[1].data.push(value);
		chart1.data.datasets[1].data.shift();

		// 레이블 삽입
		chart1.data.labels.push(tick);
		chart1.data.labels.shift();
	}
	chart1.update();
}

function adddistanceChartData(value) {
	tick++; // 도착한 데이터의 개수 증가
	tick %= 100; // tick의 범위는 0에서 99까지만. 100보다 크면 다시 0부터 시작
	let n = chart2.data.datasets[0].data.length; // 현재 데이터의 개수 
	if(n < LABEL_SIZE) 
		chart2.data.datasets[0].data.push(value);
	else {
		// 새 데이터 value 삽입
		chart2.data.datasets[0].data.push(value);
		chart2.data.datasets[0].data.shift();

		// 레이블 삽입
		chart2.data.labels.push(tick);
		chart2.data.labels.shift();
	}
	chart2.update();
}

function hideshow(canvas) { // 캔버스 보이기 숨기기 
	if(canvas.style.display == "none")
		canvas.style.display = "block";
	else 
		canvas.style.display = "none"; 
}

window.addEventListener("load", lightDrawChart);
window.addEventListener("load", temnhumDrawChart); // load 이벤트가 발생하면 drawChart() 호출하도록 등록
window.addEventListener("load", distanceDrawChart);