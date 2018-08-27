import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class StudentDetails extends Component
{
    constructor(props)
    {
        super(props);
        console.log("hkjasdfk");
    }

    state = {
        studentdetails : []
    }

    componentDidMount(){
        fetch('http://127.0.0.1:8000/api/colleges/' + this.props.match.params.id + '/students/' + this.props.match.params.mid)
        .then(response => response.json())
        .then(responseJson => {this.setState( { studentdetails : responseJson } );console.log(responseJson); })
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
                            <th>Problem1</th>
                            <th>Problem2</th>
                            <th>Problem3</th>
                            <th>Problem4</th>
                            <th>Total</th>
                            </tr>
                        </thead>
                        <tbody>
                        {this.state.collegedetails &&  this.state.studentdetails.map(col_mark =>
                            (
                                <tr key={col_mark.id}>
                                    <td> {col_mark.problem1}</td>
                                    <td> {col_mark.problem2}</td>
                                    <td> {col_mark.problem3}</td>
                                    <td> {col_mark.problem4}</td>
                                    <td> {col_mark.total}</td>
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

export default StudentDetails;