import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class CollegeList extends Component
{

    state = {
        collegeslist : []
    }

    componentDidMount(){
        fetch('http://127.0.0.1:8000/api/colleges/')
        .then(response => response.json())
        .then(responseJson => this.setState( { collegeslist : responseJson } ) )
        .catch(e =>  console.log("Error occured") )
    }

    render(){
        return(
            <React.Fragment>
                <div className = "container">
                    <h2>Colleges List</h2>
                     <table className = "table  table-bordered">
                        <thead>
                            <tr>
                            <th>College</th>
                            <th>Location</th>
                            <th>Acronym</th>
                            <th>Contact</th>
                            </tr>
                        </thead>
                        <tbody>
                        {this.state.collegeslist &&  this.state.collegeslist.map(college =>
                            (
                                <tr key={college.id}>
                                    <td > {college.name}</td>
                                    <td> {college.location}</td>
                                    <td><Link to={'/college/' + college.id}> {college.acronym}</Link></td>
                                    <td> {college.contact}</td>
                                </tr>
                            )
                        )}
                        </tbody>
                     </table>
                </div>
              </React.Fragment>
            )
     }
}

export default CollegeList;
