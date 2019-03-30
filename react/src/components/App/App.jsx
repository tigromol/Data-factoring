import React, { useEffect } from "react";
import "./App.css";
import { Provider } from "react-redux";
import store from "../../store";
import FunctionList from "../FunctionList/FunctionList";
import ControlledChart from "../ControlledChart";
import FileUploader from "../FileUploader/index";

import { getFunctions } from "../../actions/functions";
import { connect } from "react-redux";

const App = ({ getFunctions }) => {
	useEffect(() => {
		getFunctions();
	}, []);

	return (
		<Provider store={store}>
			<main className="main">
				<FunctionList />
				<ControlledChart />
				<FileUploader />
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
