import React from "react";
import "./ControlPanel.scss";
import FileUploader from "../FileUploader/index";

const ControlPanel = () => {
	return (
		<div className="control-panel">
			<div className="btn-group">
				<div className="btn">Config</div>
				<div className="btn">Process</div>
				<div className="btn">Pre-process</div>
				<FileUploader />
			</div>
		</div>
	);
};

export default ControlPanel;
