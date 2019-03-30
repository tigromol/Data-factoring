import React from "react";
import "./Dashboard.scss";
import FileUploader from "../FileUploader/index";
import ControlledChart from "../ControlledChart/index";

const Dashboard = () => {
	return (
		<div className="dashboard">
			<h2>123</h2>
			<FileUploader />
			<ControlledChart />
			<ControlledChart />
			<ControlledChart />
			<ControlledChart />
		</div>
	);
};

export default Dashboard;
