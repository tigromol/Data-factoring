import React, { Component } from "react";

class Todo extends Component {
  constructor({ content, id }) {
    super();
    this.content = content;
    this.id = id;
    this.checkedStyle = { color: "gray", textDecoration: "line-through" };
    this.state = {
      checked: false
    };
  }

  check = () => {
    this.setState({ checked: !this.state.checked });
  };

  close = () => {
    console.log(this.content);
  };

  render() {
    return (
      <div className="item" style={{ margin: "20px 0" }}>
        <div className="content">
          <div className="header" style={{ padding: "10px 0" }}>
            #{this.id}
            <i
              className="icon close ui right floated"
              style={{ color: "red", cursor: "pointer" }}
              onClick={() => this.close()}
            />
            <i
              className="icon check ui right floated"
              style={{ color: "green", cursor: "pointer" }}
              onClick={() => this.check()}
            />
          </div>
          <span style={this.state.checked ? this.checkedStyle : null}>
            {this.content}
          </span>
        </div>
      </div>
    );
  }
}

export default Todo;
