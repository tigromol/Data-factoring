import React from "react";
import "./Spinner.scss";
import SpinnerSvg from "./Spinner.svg";

const Spinner = () => (
	<img src={SpinnerSvg} alt="spinner" className="spinner" />
);

export default Spinner;
