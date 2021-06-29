import React, {Component} from 'react';
import axios from 'axios';
import {Redirect} from 'react-router-dom';


class Form extends Component {
    constructor(props) {
        super(props);
        
        this.initialState = {
            name: '',
            redirect: null
        };

        this.state = this.initialState;
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
    }

    onFormSubmit = (event) => {
        event.preventDefault();
    
        this.setState(this.initialState);
        const input = this.state;
        
        axios.post(`http://localhost:8000/data`, input)
        .then(res => {
            console.log("Input wast sent to API");
            console.log(res);
            console.log(res.data);
            console.log(`date is${JSON.stringify(res.data)}`);

            this.setState({name: res.data})
            this.props.handleSubmit(res.data);
            this.setState(this.initialState);
        })
        .catch(err => {
            console.error(err);
        });
    }

    onLogout = () => {
        this.setState({ redirect: "/" });
    }

    render() {
        const { name } = this.state; 

        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />

        }
        return (
            <form onSubmit={this.onFormSubmit}>
                <label for="name" >Event</label>
                <input 
                    type="text" 
                    name="name" 
                    id="name"
                    value={name} 
                    placeholder = "예시: 토요일 오후 3시 미팅"
                    onChange={this.handleChange} />
                <button type="submit">
                    Submit
                </button>
            </form>            

        );
    }
}

export default Form;