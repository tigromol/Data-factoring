import React, { Component } from "react";
import { createTodo } from "../../actions/todoActions";
import { connect } from "react-redux";

class TodoInput extends Component {
  state = { inputVal: "" };

  inputHandler = e => {
    this.setState({ inputVal: e.target.value });
  };

  addTodo = () => {
    if (this.state.inputVal !== "") {
      console.log("action init");

      this.props.createTodo(this.state.inputVal);

      this.setState({ inputVal: "" });
    }
  };

  render() {
    return (
      <div className="ui action input">
        <input
          type="text"
          placeholder="Add todo..."
          style={{ width: "400px" }}
          value={this.state.inputVal}
          onChange={this.inputHandler}
        />
        <button className="ui button primary" onClick={this.addTodo}>
          Add
        </button>
      </div>
    );
  }
}

export default connect(
  null,
  { createTodo }
)(TodoInput);
