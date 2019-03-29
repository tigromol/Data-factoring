import React from "react";
import "./FunctionList.css";
import FunctionItem from "../FunctionItem";

const funcs = [
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" },
  { name: "123", func: "x^2" }
];

const FunctionList = () => {
  const items = funcs.map(({ name, func }, i) => (
    <FunctionItem key={i} name={name} func={func} />
  ));

  return (
    <div className="function-list">
      <h2>Functions</h2>
      {items}
      <div onClick={123} className="function-add-btn">
        Add new
      </div>
    </div>
  );
};

export default FunctionList;
