// require("../assets/sass/style.scss");

var React = require('react');
var ReactDOM = require('react-dom');
var routes = require('./config/routes');
var style = require('../assets/sass/style.scss');

ReactDOM.render(routes, document.getElementById('app'));
