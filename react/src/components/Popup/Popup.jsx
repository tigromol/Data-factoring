import React from "react";
import "./Popup.scss";
import { connect } from "react-redux";
import { popupClose } from "../../actions/popup";
import { email } from "../../data/popupComponents";
import EmailPopup from "../EmailPopup";

const Popup = ({ popupClose, componentId }) => {
  const closePopupButtonHandle = () => {
    popupClose();
  };

  return (
    <div className="pop-up-wrapper">
      <div className="main-popup">
        {componentId === email && <EmailPopup />}
        <div className="close-btns">
          <div className="close-btn btn" onClick={closePopupButtonHandle}>
            Close
          </div>
          <div className="save-btn btn" onClick={closePopupButtonHandle}>
            Save
          </div>
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = state => ({
  componentId: state.popup.componentId
});

const mapDispatchToProps = {
  popupClose
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Popup);
