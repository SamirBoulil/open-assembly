var axios = require('axios');
var React = require('react');
var Select = require('react-select');
var ApiHelper = require('../utils/apiHelper');

PromptDepartmentContainer = React.createClass({
	getInitialState: function() {
		return {
			"departments": []
		};
	},
	componentDidMount: function() {
		ApiHelper.getDepartments()
			.then(function(json) {
				return axios.all(json.data.map(function(department) {
					return {
						"value": department.num_department,
						"label": department.num_department + " - " + department.department + " - " + department.region
					}
				}));
			})
			.then(function(departments) {
				this.setState({
					departments: departments
				});
			}.bind(this));
	},
	render: function() {
		return (
			<div className="section">
				<div className="container">
					<Select
						clearable
						ignoreCase
						scrollMenuIntoView={false}
						name="department-autocomplete"
						placeholder="Trouver votre départment"
						searchingText="Recherche ..."
						searchPromptText="Trouver votre département"
						noResultsText="Aucun département ne correspond à votre recherche"
						options={this.state.departments}
						onValueClick={undefined} />
				</div>
			</div>
		);
	}
});

module.exports = PromptDepartmentContainer;
