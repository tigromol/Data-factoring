import React, { useEffect } from "react";
import "./App.css";
import FunctionList from "../FunctionList/FunctionList";

import { getFunctions } from "../../actions/functions";
import { connect } from "react-redux";
import ControlPanel from "../ControlPanel";
import Dashboard from "../Dashboard";
import Popup from "../Popup";

const App = ({ getFunctions, popup }) => {
  useEffect(() => {
    getFunctions();
  }, []);

  console.log(popup);

  return (
    <main className="main">
      <ControlPanel />
      <FunctionList />
      <Dashboard />
      {popup && popup.isOpen && <Popup />}
    </main>
  );
};

const mapStateToProps = state => ({
  popup: state.popup
});

const mapDispatchToProps = {
  getFunctions
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App);
