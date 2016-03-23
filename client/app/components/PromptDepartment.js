var React = require('react');
var PropTypes = React.PropTypes;

function PromptDepartment (props) {
	return (
		<p className="control is-loading">
			<input 
				type='text'
				className='input is-medium' 
				placeholder='Numéro de département'	
				onChange={props.onUpdateDepartement}
				value={props.department} />
		</p>
	);
}

PromptDepartment.propTypes = {
	onUpdateDepartement: PropTypes.func.isRequired,
	department: PropTypes.string.isRequired,
}

module.exports = PromptDepartment;