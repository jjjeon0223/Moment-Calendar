import React, {Component} from "react";
import axios from 'axios';
import { Redirect } from "react-router-dom";

class Login extends Component {
    constructor(props) {
        super(props);
        
        this.initialState = {
            ID: '',
            Password: '',
            token: null,
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

    onLogin = (event) => {
        event.preventDefault();
        axios.get(`http://localhost:8000/login`)
        .then(res => {
            console.log("Fetching user data");
            console.log("res.data is: " + JSON.stringify(res.data));
            if (this.state.Password === res.data.Password && this.state.ID === res.data.ID) {
                this.setState({token: "True"});
                this.props.handleLogin(this.state.token);
                console.log("Validation Successful. Token: " + this.state.token);
                alert("Login Successful");
            }
            else{
                console.log(JSON.stringify(res.data))
                console.log(res.body)
                console.log(res)
                console.log("Validation Failed")
                alert("Incorrect Login Attempt. Check ID or Password")
            }
        })
        .catch(err => {
            console.error(err);
        });
    }

    signUp = () => {
        this.setState({ redirect: "/register" });

    }

    render() {
        const { ID, Password } = this.state; 
    
        // if (this.state.token !== null) {
        //     console.log("Redirect form login to app")
        //     return (
        //         <Redirect from='/login' to='/' />
        //     )
        // }
        if (this.state.redirect !== null) {
            return <Redirect to={this.state.redirect} />
        }
        return (
            <div classname="container">
                <h1>Welcome to Moment Calendar</h1>
                <h3>Log in to continue</h3>
                
                <form onSubmit={this.onLogin}>
                    <label for="ID">ID</label>
                    <input 
                        type="text" 
                        name="ID" 
                        id="name"
                        value={ID} 
                        onChange={this.handleChange} />
                    <label for="Password">Password</label>
                    <input 
                        type="password" 
                        name="Password" 
                        id="Password"
                        value={Password} 
                        onChange={this.handleChange} />
                    <button type="submit">
                        Submit
                    </button>
                    <div style = {{float: 'right'}}>
                        <button onClick={this.signUp}>
                            Not registered? Sign Up!
                        </button>
                    </div>
                </form>
            </div>
        );
    }
};

export default Login;