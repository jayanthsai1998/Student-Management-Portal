import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class CollegeDetails extends Component
{
    state = {
        collegesdetails : []
    }

    componentDidMount(){
        fetch('http://127.0.0.1:8000/api/colleges/' + this.props.match.params.id + '/students/')
        .then(response => response.json())
        .then(responseJson => this.setState( { collegedetails : responseJson } ) )
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
                            <th>Name</th>
                            <th>E-mail</th>
                            <th>DB Folder</th>
                            <th>Marks</th>
                            </tr>
                        </thead>
                        <tbody>
                        {this.state.collegedetails &&  this.state.collegedetails.map(col_stud =>
                            (
                                <tr key={col_stud.id}>
                                    <td> {col_stud.name}</td>
                                    <td> {col_stud.email}</td>
                                    <td> {col_stud.db_folder}</td>
                                    <td><Link to={'/collge/' + col_stud.college + '/students/' + col_stud.id }> Marks Obtained </Link></td>
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

export default CollegeDetails;