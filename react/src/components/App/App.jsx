import React, { useEffect } from "react";
import "./App.css";
import { Provider } from "react-redux";
import store from "../../store";
import FunctionList from "../FunctionList/FunctionList";

import { getFunctions } from "../../actions/functions";
import { connect } from "react-redux";
import ControlPanel from "../ControlPanel";
import Dashboard from "../Dashboard";

const App = ({ getFunctions }) => {
	useEffect(() => {
		getFunctions();
	}, []);

	return (
		<Provider store={store}>
			<main className="main">
				<ControlPanel />
				<FunctionList />
				<Dashboard />
			</main>
		</Provider>
	);
};

const mapStateToProps = state => ({});

const mapDispatchToProps = {
	getFunctions,
};

export default connect(
	mapStateToProps,
	mapDispatchToProps
)(App);
