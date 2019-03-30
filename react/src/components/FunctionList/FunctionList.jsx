import React from "react";
import "./FunctionList.css";
import FunctionItem from "../FunctionItem";
import { connect } from "react-redux";

const FunctionList = ({ functions }) => {
	console.log(functions[0]);

	const items = functions.map(({ name, args, ...props }) => (
		<FunctionItem key={name} {...props} />
	));

	return (
		<div className="function-list">
			<h2>Functions</h2>
			{items}
			<div onClick={() => console.log(123)} className="function-add-btn">
				Add new
			</div>
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
