import React, { Component } from "react";
import "./ErrorBoundary.scss";

export default class ErrorBoundary extends Component {
	state = { hasError: false };

	componentDidCatch() {
		this.setState({ hasError: true });
	}

	render() {
		const { hasError } = this.state;

		if (hasError) return <div>Error</div>;
		return this.props.children;
	}
}
