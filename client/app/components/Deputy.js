var React = require('react');
var PropTypes = React.PropTypes;

var Deputy = function(props) {
    return (
        <div className="deputy-wrapper">
            <h1>{this.props.name}</h1>
        </div>
    );
}

module.exports = Deputy;
