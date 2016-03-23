var React = require('react');
var PromptDepartment = require('../components/PromptDepartment');

PromptDepartmentContainer = React.createClass({
	getInitialState: function() {
		return {
			department: ''
		};
	},
	handleUpdateDepartment: function(e) {
		this.setState({
			department: event.target.value
		});
	},
	render: function() {
		return (
			<div>
				<section class="hero">
				  <div class="hero-content">
				    <div class="container">
				      <h1 class="title">
				      	Open Assembly
				      </h1>
				      <h2 class="subtitle">
				      	Democracie colaborative
				      </h2>
				    </div>
				  </div>
				</section>
				<div className="section">
					<div className="container">
						<PromptDepartment 
							department={this.state.department}
							onUpdateDepartement={this.handleUpdateDepartment} />
					</div>
				</div>
				<footer class="footer">
				  <div class="container">
				    <div class="content is-centered">
				      <p>
				        <strong>Bulma</strong> by <a href="http://jgthms.com">Jeremy Thomas</a>. The source code is licensed
				        <a href="http://opensource.org/licenses/mit-license.php">MIT</a>. The website content
				        is licensed <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC ANS 4.0</a>.
				      </p>
				      <p>
				        <a class="icon" href="https://github.com/jgthms/bulma">
				          <i class="fa fa-github"></i>
				        </a>
				      </p>
				    </div>
				  </div>
				</footer>
			</div>
		);
	}
});

module.exports = PromptDepartmentContainer;