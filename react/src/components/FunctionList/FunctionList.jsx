import React from "react";
import "./FunctionList.scss";
import FunctionItem from "../FunctionItem";
import { connect } from "react-redux";

const FunctionList = ({ functions }) => {
	console.log(functions[0]);

	const items = functions.map(({ name, ...props }) => (
		<FunctionItem key={name} {...props} />
	));

	return (
		<div className="function-list">
			<h2 className="function-title">Functions</h2>
			<div className="function-items">{items}</div>
			<div className="function-add-btn">Add new</div>
		</div>
	);
};

const mapStateToProps = state => ({
	functions: state.functions,
});

const mapDispatchToProps = {};

export default connect(
	mapStateToProps,
	mapDispatchToProps
)(FunctionList);
