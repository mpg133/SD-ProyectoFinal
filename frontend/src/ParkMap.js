
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



      // provisional para mostrar los datos en string.
      /*
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
      //*/
    });
  }

  componentDidMount(){
    this.interval = setInterval(
      () => {this.getData()},
      500
    );
  }

  drawLine(line, row){
    var cols = []

    for(var i = 0; i < line.length; i++){
      if (line[i] != '0'){
        if(parseInt(line[i]) > 0){
          cols.push(<td style={{backgroundColor: "black"}} className="mapDrawing" key={i + 'x' + row + 'y'}>{line[i]}</td>);
        }else{
          cols.push(<td style={{backgroundColor: "green"}} className="mapDrawing" key={i + 'x' + row + 'y'}>{line[i]}</td>);
        }
      }else{
        var bg = "";
        if(row >= 10 && i >= 10){
          bg = "#55554d";
        }else if(row >= 10 && i < 10){
          bg = "#553b55";
        }else if(row < 10 && i < 10){
          bg = "#315555";
        }else if(row < 10 && i >= 10){
          bg = "#313b4d";
        }
        cols.push(<td style={{backgroundColor: bg}} className="mapDrawing" key={i + 'x' + row + 'y'}> </td>);
      }
    }
    return <tr key={row}>{cols}</tr>;
  }

  drawMap(){
    var map = this.state.map
    var rows = []

    for(var i = 0; i < map.length; i++){
      rows.push(this.drawLine(map[i], i));
    }
    return <table className="mapTable"><tbody>{rows}</tbody></table>;
  }



  render(){
    return (<div>
      <div id='mapDiv'></div>
      {this.drawMap()}
    </div>)
  }
}


export default ParkMap;