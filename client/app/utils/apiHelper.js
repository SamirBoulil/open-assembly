var axios = require('axios');

var SERVER_URL = 'http://127.0.0.1:8003';
var DEPARTMENTS = '/departments'

var helpers = {
	getDepartments: function() {
		return axios.get(SERVER_URL+DEPARTMENTS);
	}
};

module.exports = helpers;
