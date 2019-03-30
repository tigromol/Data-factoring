import React from "react";
import "./ControlledChart.scss";
import { Chart } from "react-google-charts";
import { connect } from "react-redux";
import Spinner from "../Spinner";

const ControlledChart = props => {
	const { charts } = props;
	return (
		<div className="chart">
			<Chart
				width={"100%"}
				height={"100%"}
				chartType="LineChart"
				// loader={<Spinner />}
				data={charts[0].data}
				options={{
					// Use the same chart area width as the control for axis alignment.
					chartArea: { height: "90%", width: "90%" },
					hAxis: { slantedText: false },
					vAxis: { viewWindow: { min: 0, max: 2000 } },
					legend: { position: "none" },
				}}
				rootProps={{ "data-testid": "3" }}
				chartPackages={["corechart", "controls"]}
				controls={[
					{
						controlType: "ChartRangeFilter",
						options: {
							filterColumnIndex: 0,
							ui: {
								chartType: "LineChart",
								chartOptions: {
									chartArea: { width: "90%", height: "50%" },
									hAxis: { baselineColor: "none" },
								},
							},
						},
						controlPosition: "bottom",
						controlWrapperParams: {
							state: {
								range: {
									start: new Date(1997, 1, 9),
									end: new Date(2002, 2, 20),
								},
							},
						},
					},
				]}
			/>
		</div>
	);
};

const mapStateToProps = state => ({
	charts: state.charts,
});

const mapDispatchToProps = {};

export default connect(
	mapStateToProps,
	mapDispatchToProps
)(ControlledChart);
