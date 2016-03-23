var React = require('react');
var PropTypes = React.PropTypes;
var Select = require('react-select');

function PromptDepartment (props) {
	return (
		<p className="control is-loading">
			<Select.Async
			    name="department"
			    loadOptions={props.getOptions}
			    isLoadingExternally=true
			/>
		</p>
	);
}

PromptDepartment.propTypes = {
	onUpdateDepartement: PropTypes.func.isRequired,
	department: PropTypes.string.isRequired,
	getOptions: PropTypes.func.isRequired,
}

module.exports = PromptDepartment;