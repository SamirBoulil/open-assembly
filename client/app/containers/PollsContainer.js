var axios = require('axios');
var React = require('react');
var Select = require('react-select');
var ApiHelper = require('../utils/apiHelper');

var Deputy = require('../components/Deputy');
var Poll = require('../components/Poll');

var PollsContainer = React.createClass({
    contextTypes: {
        router: React.PropTypes.object.isRequired
    },
    getInitialState: function() {
        return {
            polls: [],
            deputies: []
        };
    },
    componentDidMount: function() {
        var department = this.props.routeParams.department;
        if (typeof department !== 'undefined') {
            ApiHelper.getDeputiesForDepartment(department)
            .then(function(deputiesInfo) {
                this.setState({
                    // polls: this.state.polls,
                    deputies: deputiesInfo
                });
            }.bind(this));
            ApiHelper.getPollsForDepartment(department)
            .then(function(pollsInfo) {
                this.setState({
                    polls: pollsInfo,
                    // deputies: this.state.deputies
                });
            }.bind(this));
        }
    },
    render: function() {
        return (
            <div className="poll-container">
                <div className="deputies">
                    <h1>Vos représentants à l'assemblée nationale</h1>
                    {this.state.deputies.map(function(deputy) {
                        return <Deputy {...deputy}></Deputy>;
                    })}
                </div>
                <div className="polls">
                    <h1>Les votes des députés</h1>
                    {this.state.polls.map(function(poll) {
                        return <Poll {...poll}></Poll>;
                    })}
                </div>
            </div>
        );
    }
})

module.exports = PollsContainer;
