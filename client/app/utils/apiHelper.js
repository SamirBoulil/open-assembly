var axios = require('axios');

var SERVER_URL = 'http://127.0.0.1:8003';
var ERROR_MSG = 'Wargning! A server error occured.'

var helpers = {
	getDepartments: function() {
		return axios.get(SERVER_URL + '/departments')
     .then(function(response) {
        return response.data;
    })
     .catch(function(err) {
      console.log(ERROR_MSG);
      console.log(err)
  });
 },
 getDeputiesForDepartment: function(department) {
    return axios.get(SERVER_URL + '/departments/' + department + '/deputies')
    .then(function(response) {
      return response.data;
  })
    .catch(function(err) {
      console.log(ERROR_MSG);
      console.log(err)
  });
},
getPollsForDepartment: function(department) {
    return axios.get(SERVER_URL + '/departments/' + department + '/polls')
    .then(function(response) {
      return response.data.results;
  })
    .catch(function(err) {
      console.log(ERROR_MSG);
      console.log(err)
  });
}
};

module.exports = helpers;
