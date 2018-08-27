import React, { Component } from 'react'

class HeaderPanel extends Component
{

    state = {
        isLoggedIn : this.props.isLoggedIn
    }

    toggleLoggedIn = () => {
        this.setState(prev => ( { isLoggedIn : !prev.isLoggedIn } ) )
    }

    render(){

            const {title} = this.props;

            const {isLoggedIn}  = this.state;

            return(

                <div className="header">
                    <h2>{title}</h2>
                    <div className = "menu" onClick = {this.toggleLoggedIn}>
                        {
                            isLoggedIn ?
                            <button className= "btn btn=primary" href = "http://127.0.0.1:8000/login/">LOGIN</button>
                            : <button className = "btn btn=primary" href = "">LOGOUT</button>
                        }
                    </div>
                </div>


            )

     }
}

export default HeaderPanel;
