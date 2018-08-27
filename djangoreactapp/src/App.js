import React, { Component } from 'react';

import HeaderPanel from './HeaderPanel';
import CollegeList from './CollegeList';
import CollegeDetails from './CollegeDetails';
import StudentDetails from './StudentDetails';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">

      <Router>
        <div>

            <Route exact path = "/" component = {CollegeList}/>
            <Route exact path = "/college/:id/" component = {CollegeDetails}/>
            <Route exact path = "/college/:id/students/:mid/" component = {StudentDetails}/>
           </div>
        </Router>
      </div>
    );
  }
}

export default App;
