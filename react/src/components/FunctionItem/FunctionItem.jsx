import React from "react";
import "./FunctionItem.scss";

const FunctionItem = ({ description, display, args }) => {
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
			<div className="arg-description">{description}</div>
			<input type="text" placeholder="Arg value" />
		</div>
	);
};

export default FunctionItem;
