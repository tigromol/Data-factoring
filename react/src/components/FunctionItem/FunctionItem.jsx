import React from "react";
import "./FunctionItem.scss";

const FunctionItem = props => {
	const description = props.description || "Function description";
	const display = props.display || "display";
	const args = props.args || [
		{
			description: "string",
			display: "string",
			name: "div",
		},
		{
			description: "string",
			display: "string",
			name: "div",
		},
		{
			description: "string",
			display: "string",
			name: "div",
		},
	];
	const name = props.name;

	return (
		<div className="function-item">
			<div className="function-desc">
				<h3 className="display">{display}</h3>
				<p className="desc">{description}</p>
			</div>
			<div className="function-args">
				{args.map((elem, i) => (
					<ArgumentsItem key={i} {...elem} />
				))}
			</div>
		</div>
	);
};

const ArgumentsItem = ({ display, description, name }) => {
	return (
		<div className="function-arg">
			<div className="arg">{display}</div>
			<div className="arg-description">
				Lorem ipsum dolor sit amet, consectetur adipisicing elit.
			</div>
			<input type="text" placeholder="Arg value" />
		</div>
	);
};

export default FunctionItem;
