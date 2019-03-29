import React from "react";
import "./Spinner.scss";
import SpinnerSVG from "./Spinner.svg";

const Spinner = () => {
	return (
		<div className="spinner-wrapper">
			<img src={SpinnerSVG} alt="spinner" className="spinner" />
		</div>
	);
};

export default Spinner;
