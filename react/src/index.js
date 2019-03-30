import React from "react";
import ReactDOM from "react-dom";

import { BrowserRouter as Router } from "react-router-dom";
import { Provider } from "react-redux";
import store from "./store";
import ErrorBoundary from "./components/ErrorBoundary";
import App from "./components/App";

ReactDOM.render(
  <Provider store={store}>
    {/* <ErrorBoundary> */}
    <Router>
      <App />
    </Router>
    {/* </ErrorBoundary> */}
  </Provider>,
  document.getElementById("root")
);
