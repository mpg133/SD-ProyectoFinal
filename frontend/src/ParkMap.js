
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
        visitors: response.data['visitors'],
        regions: ['','','','']
      }));
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

  drawVisitors(){
    var cols = []
    var rows = []
    
    cols.push(<td>ID</td>)
    cols.push(<td>NAME</td>)
    cols.push(<td>STATUS</td>)
    rows.push(<tr>{cols}</tr>)
    cols = []
    for(var i = 0; i < this.state.visitors.length; i++){
      cols.push(<td>{this.state.visitors[i]['id']}</td>)
      cols.push(<td>{this.state.visitors[i]['name']}</td>)
      cols.push(<td>{this.state.visitors[i]['status']}</td>)
      
      rows.push(<tr>{cols}</tr>)
      cols = []
    }
    return <table className="visitorsTable"><tbody>{rows}</tbody></table>
  }

  drawAttracts(){
    var cols = []
    var rows = []
    
    cols.push(<td>ID</td>)
    cols.push(<td>TIME</td>)
    cols.push(<td>REGION</td>)
    cols.push(<td>STATUS</td>)
    rows.push(<tr>{cols}</tr>)
    cols = []
    var keys = Object.keys(this.state.attrs);
    for(var i = 0; i < keys.length; i++){
      cols.push(<td>{keys[i]}</td>)
      cols.push(<td>{this.state.attrs[keys[i]]['time']}</td>)
      cols.push(<td>{this.state.attrs[keys[i]]['region']}</td>)
      if(this.state.attrs[keys[i]]['status'] == 0){
        cols.push(<td>[X]</td>)
      }else{
        cols.push(<td>[O]</td>)
      }
      
      if(this.state.attrs[keys[i]]['status'] == 0){
        rows.push(<tr style={{color:'red', backgroundColor: '#151922'}}>{cols}</tr>)
      }else{
        rows.push(<tr style={{color:'green', backgroundColor: '#151922'}}>{cols}</tr>)
      }
      cols = []
    }
    return <table className="attractionsTable"><tbody>{rows}</tbody></table>

  }



  render(){
    return (<div className="mapVisGroup">
      {this.drawVisitors()}
      {this.drawMap()}
      {this.drawAttracts()}
    </div>)
  }
}


export default ParkMap;