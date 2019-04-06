import React from "react";
import "./ControlPanel.scss";
import FileUploader from "../FileUploader/index";
import { connect } from "react-redux";
import { popupOpen } from "../../actions/popup";
import { chartsList, email } from "../../data/popupComponents";

const ControlPanel = ({ popupOpen }) => {
  const chartsListHandle = () => {
    popupOpen(chartsList);
  };

  const emailHandle = () => {
    popupOpen(email);
  };

  return (
    <div className="control-panel">
      <div className="btn-group">
        <div className="btn" onClick={chartsListHandle}>
          Config
        </div>
        <div className="btn" onClick={emailHandle}>
          Process
        </div>
        <div className="btn">Pre-process</div>
        <FileUploader />
      </div>
    </div>
  );
};

const mapStateToProps = state => ({});

const mapDispatchToProps = {
  popupOpen
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ControlPanel);
