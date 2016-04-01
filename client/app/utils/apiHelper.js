var axios = require('axios');

var SERVER_URL = 'http://127.0.0.1:8003';

var helpers = {
	getDepartments: function() {
		return axios.get(SERVER_URL + '/departments');
	},
    getDeputiesForDepartment: function(department) {
        return axios.get(SERVER_URL + '/departments/' + department + '/deputies');
    },
    getPollsForDepartment: function(departments) {
        return axios.get(SERVER_URL + '/departments/' + department + '/polls');
    }
};

module.exports = helpers;
