var React = require('react');
var PromptDepartment = require('../components/PromptDepartment');
var ApiHelper = require('../utils/apiHelper');

PromptDepartmentContainer = React.createClass({
	getInitialState: function() {
		return {
			department: ''
		};
	},
	handleUpdateDepartment: function(input) {
		ApiHelper.getDepartmentsForInput(input)
			.then(function(json) {
				return {options: json};
			});
	},
	render: function() {
		return (
			<div className="section">
				<div className="container">
					<PromptDepartment
						department={this.state.department}
						onUpdateDepartement={this.handleUpdateDepartment} />
				</div>
			</div>
		);
	}
});

module.exports = PromptDepartmentContainer;