var axios = require('axios');

var SERVER_URL = 'https://127.0.0.1:8000';
var DEPARTMENTS = '/departments/?s='

function getDepartmentsForInput(input) {
	return axios.get(SERVER_URL+DEPARTMENTS+input);
}

var helpers = {
	getDepartmentsForInput: function(input) {
		return axios.get(SERVER_URL+DEPARTMENTS+input);
	}
};

module.exports = helpers;