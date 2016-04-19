var axios = require('axios');
var React = require('react');
var ReactRouter = require('react-router');
var Select = require('react-select');
var ApiHelper = require('../utils/apiHelper');

var PromptDepartmentContainer = React.createClass({
  contextTypes: {
    router: React.PropTypes.object.isRequired
  },
  getInitialState: function() {
    return {
      departments: [],
      selectedDepartment: ''
    };
  },
  componentDidMount: function() {
    ApiHelper.getDepartments()
    .then(function(departments) {
      return axios.all(departments.map(function(department) {
        return {
          value: department.num_department,
          label: department.num_department + " - " + department.department + " - " + department.region
        }
      }));
    })
    .then(function(processedDepartments) {
      this.setState({
        departments: processedDepartments
      });
    }.bind(this));
  },
  updateValue: function (newValue) {
    this.setState({
      selectedDepartment: newValue
    });
  },
  handleClick: function(e) {
    e.preventDefault();
    if (this.state.selectedDepartment !== '') {
      this.context.router.push({
        pathname: '/department/' + this.state.selectedDepartment.value + '/polls'
      });
    }
  },
  render: function() {
    return (
        <div className="home">
          <div className="header">
            <h1>Trouvez en un instant les votes de vos représentants à l'assemblée nationale</h1>
          </div>
          <div className="form">
            <Select
              ref="departmentSelect"
              autofocus
              clearable
              ignoreCase
              scrollMenuIntoView={false}
              className="form__prompt"
              name="department-autocomplete"
              placeholder="Trouver votre départment"
              searchingText="Recherche ..."
              searchPromptText="Trouver votre département"
              noResultsText="Aucun département ne correspond à votre recherche"
              options={this.state.departments}
              value={this.state.selectedDepartment}
              onChange={this.updateValue} />
            <button className="form__search" onClick={this.handleClick}>Show me votes</button>
          </div>
      </div>
      );
  }
});

module.exports = PromptDepartmentContainer;
