import React, { Component } from "react";

export default class ErrorBoundry extends Component {
	state = {
		hasError: false,
	};

	componentDidCatch(err) {
		console.log(err);
		this.setState({ hasError: true });
	}
	render() {
		const { hasError } = this.state;
		if (hasError) return <h1>Something was broken</h1>;
		return this.props.children;
	}
}
