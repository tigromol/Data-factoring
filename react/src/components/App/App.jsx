import React, { Component } from "react";
import "./App.scss";
import { Chart } from "react-google-charts";

const options = {
	title: "Age vs. Weight comparison",
	hAxis: { title: "Age", viewWindow: { min: 0, max: 15 } },
	vAxis: { title: "Weight", viewWindow: { min: 0, max: 15 } },
	legend: "none",
};
const data = [
	["Age", "Weight"],
	[8, 12],
	[4, 5.5],
	[11, 14],
	[4, 5],
	[3, 3.5],
	[6.5, 7],
];

class App extends Component {
	render() {
		return (
			<div className="app">
				<h1>Hi</h1>
				<Chart
					chartType="ScatterChart"
					data={data}
					options={options}
					width="80%"
					height="400px"
					legendToggle
				/>

				<Chart
					width="80%"
					height="500px"
					chartType="AreaChart"
					loader={<div>Loading Chart</div>}
					data={[
						["Year", "Sales", "Expenses"],
						["2013", 1000, 400],
						["2014", 1170, 460],
						["2015", 660, 1120],
						["2016", 1030, 540],
					]}
					options={{
						isStacked: true,
						legend: { position: "top", maxLines: 3 },
						vAxis: { minValue: 0 },
					}}
				/>

				<Chart
					width={"600px"}
					height={"400px"}
					chartType="Line"
					loader={<div>Loading Chart</div>}
					data={[
						[
							"Day",
							"Guardians of the Galaxy",
							"The Avengers",
							"Transformers: Age of Extinction",
						],
						[1, 37.8, 80.8, 41.8],
						[2, 30.9, 69.5, 32.4],
						[3, 25.4, 57, 25.7],
						[4, 11.7, 18.8, 10.5],
						[5, 11.9, 17.6, 10.4],
						[6, 8.8, 13.6, 7.7],
						[7, 7.6, 12.3, 9.6],
						[8, 12.3, 29.2, 10.6],
						[9, 16.9, 42.9, 14.8],
						[10, 12.8, 30.9, 11.6],
						[11, 5.3, 7.9, 4.7],
						[12, 6.6, 8.4, 5.2],
						[13, 4.8, 6.3, 3.6],
						[14, 4.2, 6.2, 3.4],
					]}
					options={{
						chart: {
							title: "123123",
							subtitle: "7657567567",
						},
					}}
					rootProps={{ "data-testid": "3" }}
				/>
			</div>
		);
	}
}

export default App;
