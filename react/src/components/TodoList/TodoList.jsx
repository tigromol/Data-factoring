import React, { Component } from "react";
import Todo from "../Todo";
import { connect } from "react-redux";

class TodoList extends Component {
  componentWillReceiveProps(nextProp) {
    const todos = this.props.todos;
    console.log(nextProp);
  }

  render() {
    console.log(this.props);

    return (
      <div className="ui middle aligned divided list">
        <Todo content="Consequatur illum in dignissimos odio aliquid quis.Consequatur illum in dignissimos odio aliquid quis." />
        <Todo content="Quo illum est quo atque." />
        <Todo content="Voluptatem aliquid nisi quia cum velit doloribus impedit quibusdam omnis." />
        <Todo content="Accusantium velit dignissimos in debitis fuga rerum rerum sed voluptates." />
      </div>
    );
  }
}

const mapStateToProps = state => ({});

export default connect(
  mapStateToProps,
  null
)(TodoList);
