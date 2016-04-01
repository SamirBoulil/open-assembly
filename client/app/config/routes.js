var React = require('react');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var hashHistory = ReactRouter.hashHistory;
var IndexRoute = ReactRouter.IndexRoute;

var Main = require('../components/Main');
var PromptDepartmentContainer = require('../containers/PromptDepartmentContainer');
var PollsContainer = require('../containers/PollsContainer');
// var DeputyContainer = require('../containers/DeputyContainer');
// <Route path='department/:department/polls' component={PollsContainer} />
// <Route path='deputy/:deputy' component={DeputyContainer} />

var routes = (
	<Router history={hashHistory}>
		<Route path='/' component={Main}>
			<IndexRoute component={PromptDepartmentContainer} />
            <Route path='department/:department/polls' component={PollsContainer} />'
		</Route>
	</Router>
);

module.exports = routes;
