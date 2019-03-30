import React, { Component } from "react";
import "./App.css";
import { Provider } from "react-redux";
import store from "../../store";
import FunctionList from "../FunctionList/FunctionList";
import ControlledChart from "../ControlledChart";
import FileUploader from "../FileUploader/index";

class App extends Component {
	render() {
		return (
			<Provider store={store}>
				<main className="main">
					<FunctionList />
					<ControlledChart />
					<FileUploader />
				</main>
			</Provider>
		);
	}
}

export default App;
