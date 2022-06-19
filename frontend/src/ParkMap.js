
import axios from "axios";
import React, { Component } from 'react';

class ParkMap extends Component {

  constructor(props){
    super(props);
    this.state={
      map : [],
      attrs: {},
      visitors: {}
    }
    window.mapComponent = this;
  }

  getData(){
    
    let baseURL = 'http://localhost:5001';
    const headers = {'Content-Type': 'application/json'};
    axios.get(baseURL + '/map', {'headers' : headers}).then((response) => {
      this.setState(() => ({
        map: response.data['mapa'],
        attrs: response.data['attrs'],
        visitors: response.data['visitors']
      }));

      var newString = '';
      for(var i = 0; i < this.state.map.length; i++){
        for(var j = 0; j < this.state.map.length; j++){
          newString += this.state.map[i][j] + '_ ';
        }
        newString += "</br>";
      }

      if (this.state.map != ''){
        document.getElementById('mapDiv').innerHTML = newString;
      }
    });

    
    //document.getElementById('mapDiv').innerHTML = JSON.stringify(this.state.map['2']['id']);
    /*
    if (this.state.map != ''){
      document.getElementById('mapDiv').innerHTML = this.showData();
    }
    */
  }

  componentDidMount(){
    this.interval = setInterval(
      () => {this.getData()},
      500
    );
  }

  start(){
    if (this.state.map != ''){
      document.getElementById('mapDiv').innerHTML = this.state.map;
    }
  }


  render(){
    return (<div>
      <div id='mapDiv'></div>
    </div>)
  }
}


export default ParkMap;