import React, {Component} from 'react';
import { BrowserRouter, Route, Switch} from 'react-router-dom';
import App from './App';
import Login from './Login';
import Register from './Register';

class Routes extends Component {
    state = {
        Token: null
    }

    handleLogin = token => {
        this.setState({Token: token});
        console.log("The value of the token is: " + this.state.Token)
    }

    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route exact path="/login" component={Login}>
                        <Login />
                    </Route>
                    <Route exact path="/register" component={Register}/>
                    <Route exact path="/" component={() => this.state.Token ? <App handleLogin={this.handleLogin}/> : <Login  handleLogin={this.handleLogin}/> } />
            
                </Switch>
            </BrowserRouter>
        )
    }
}

export default Routes;