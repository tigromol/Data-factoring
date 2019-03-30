import React from "react";
import "./FunctionItem.css";

const FunctionItem = ({ name, func }) => {
  const selectHandler = e => {
    console.log(e.target);
  };

  return (
    <div className="function-item" onClick={selectHandler}>
      <h5>{name}</h5>
      <h5>{func}</h5>
    </div>
  );
};

export default FunctionItem;
