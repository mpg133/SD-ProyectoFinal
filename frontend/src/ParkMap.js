
import axios from "axios";
import React, { Component } from 'react';

class ParkMap extends Component {

  constructor(props){
    super(props);
    this.state={
      map : ''
    }
    window.mapComponent = this;
  }

  getData(){
    
    let baseURL = 'http://localhost:5001';
    const headers = {'Content-Type': 'application/json'};
    axios.get(baseURL + '/map', {'headers' : headers}).then((response) => {
      this.setState(() => ({
        map:response.data['mapa'][0]
      }));
    });
    
    //document.getElementById('mapDiv').innerHTML = JSON.stringify(this.state.map['2']['id']);
    document.getElementById('mapDiv').innerHTML = this.state.map;
  }

  showData(string){
    newString = '';
    
    for(var i = 0; i<20; i++){
      for(var j = 0; j<20; j++){
        
      }  
    }
  }

  componentDidMount(){
    this.interval = setInterval(
      () => {this.getData()},
      1000
    );
  }


  render(){
    return (<div>
      <div id='mapDiv'></div>
    </div>)
  }
}


export default ParkMap;