import './App.css';
import React, { useEffect } from "react";
import ParkMap from './ParkMap';

function App() {

  useEffect(() => {
    window.mapComponent.start()
  })

  return (
    <div className="App">
      <div>
      <ParkMap></ParkMap>
      </div>
    </div>
  );
}

export default App;
