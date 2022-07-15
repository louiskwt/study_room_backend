const App = () => {
  return <div>Hello Django and React</div>;
};

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);
