import React, { Component } from 'react';
import Table from './Table';
import Form from './Form';
import {Redirect} from 'react-router-dom';
import 'tui-calendar/dist/tui-calendar.css';
import Basic from './Calendar';


export default class App extends Component {
    state = {
        characters: [],
        redirect: null
    }

    removeCharacter = index => {
        const { characters } = this.state;
    
        this.setState({
            characters: characters.filter((character, i) => { 
                return i !== index;
            })
        });
    }

    handleSubmit = character => {
        this.setState({characters: [...this.state.characters, character]});
    }

    onLogout = (event) => {
        this.setState({redirect: "/login"})
        alert("You have been Logged Out")
        // return <Redirect to='/login' />
    }


    render() {     
        const {characters} = this.state
        if(this.state.redirect) {
            return <Redirect to={this.state.redirect} />
        }
        return (
            <div className="container">
                <h1>Moment Calendar</h1>
                <Basic 
                    characterData={characters}    
                />
                <h2>Add an event to the calendar.</h2>
                <Table
                    characterData={characters}
                    removeCharacter={this.removeCharacter}
                />
                <Form method='POST' action='http://localhost:8000/data' handleSubmit={this.handleSubmit} />
                <button onClick={this.onLogout} style={{float: 'right'}}>Logout?</button>
            </div>
        )
    }

  
}
