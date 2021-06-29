import React, {useState} from 'react';
import axios from 'axios';
import { Redirect } from 'react-router-dom';

function Register() {
    const [state, setState] = useState({
        username: "",
        password: "",
        confirmPassword: "",
        email: "",
        redirect: null
    })

    const handleChange = (e) => {
        const {id, value} = e.target;
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(state.password)
        console.log(state.confirmPassword)
        if(state.password !== state.confirmPassword){
            alert('Passwords do not match')
        }
        else {
            alert('Form submit successful')
            sendDetailsToServer()
        }
    }

    const sendDetailsToServer = () => {
        const newUser = {
            "ID": state.username,
            "Password": state.password,
            "Email": state.email
        }
        axios.post(`http://localhost:8000/login`, newUser)
        .then(res => {
            console.log("User Info sent to API");
            console.log(res.data);
            setState({redirect: 'True'})
        })
        .catch(err => {
            console.error(err);
        });
    }

    if(state.redirect) return <Redirect to="/"/>

    return(
        <form onSubmit={handleSubmit}>
            <h1>Register!</h1>
            <label>Plase fill out the form below</label>
            <input 
                type="text" 
                id="username"
                value={state.username} 
                placeholder = "Enter Username"
                onChange={handleChange} />
            <input 
                type="Password"  
                id="password"
                value={state.password} 
                placeholder = "Enter Password"
                onChange={handleChange} />
            <input 
                type="Password"  
                id="confirmPassword"
                value={state.confirmPassword} 
                placeholder = "Confirm Password"
                onChange={handleChange} />
            <input 
                type="text" 
                id="email"
                value={state.email} 
                placeholder = "Enter E-mail (Email validation is required)"
                onChange={handleChange} />
            <button type="submit">
                Submit
            </button>
        </form>
    )
}

export default Register;