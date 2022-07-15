import React from "react";
import { render } from "react-dom";

export default function App() {
  return (
    <div>
      <h1>Hello, React and Django!!</h1>
    </div>
  );
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
