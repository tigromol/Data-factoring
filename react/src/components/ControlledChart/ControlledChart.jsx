import React from "react";
import "./ControlledChart.scss";
import { Chart } from "react-google-charts";
import { connect } from "react-redux";
import Spinner from "../Spinner";

const ControlledChart = props => {
	const { data } = props.file;
	if (!data) return null;

	return (
		<div className="chart">
			<Chart
				width={"100%"}
				height={"100%"}
				chartType="LineChart"
				loader={<Spinner />}
				data={data}
				options={{
					chartArea: { height: "90%", width: "90%" },
					hAxis: { slantedText: false },
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
									chartArea: { width: "90%", height: "30%" },
								},
							},
						},
						controlPosition: "bottom",
					},
				]}
			/>
		</div>
	);
};

const mapStateToProps = state => ({
	file: state.file,
});

const mapDispatchToProps = {};

export default connect(
	mapStateToProps,
	mapDispatchToProps
)(ControlledChart);
