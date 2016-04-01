var axios = require('axios');
var React = require('react');
var Select = require('react-select');
var ApiHelper = require('../utils/apiHelper');

var Deputy = require('../components/Deputy');

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
        if (typeof this.props.department !== 'undefined') {
            ApiHelper.getDeputiesForDepartment(this.props.department)
            .then(function(deputiesInfo) {
                this.setState({
                    polls: this.state.polls,
                    deputies: deputiesInfo
                });
            });
            ApiHelper.getPollsForDepartment(this.props.department)
            .then(function(pollsInfo) {
                this.setState({
                    polls: pollsInfo,
                    deputies: this.state.deputies
                });
            });
        }
    },
    render: function() {
        return (
            <div className="poll-container">
                <div className="deputies">
                    <h1>Vos représentants à l'assemblée nationale</h1>
                </div>
                <div className="polls">
                    <h1>Leur votes</h1>
                </div>
            </div>
        );
    }
})

module.exports = PollsContainer;


// {this.state.deputies.map(fuction(deputy) {
//     return (
//         <Deputy ...deputy />
//     );
// })}
