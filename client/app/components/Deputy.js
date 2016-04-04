var React = require('react');
var PropTypes = React.PropTypes;

var Deputy = function(props) {
  var sexLabel = props.sex ? "Mme" : "Mr.";
  return (
    <div className="deputy-wrapper">
      <h1>{sexLabel} {props.surname} {props.name} ({props.birth_date})</h1>
      <p>Originaire de: {props.birth_town} - {props.birth_department} - {props.birth_country}</p>
      <p>Profession: {props.work_name} ({props.work_familly})</p>
      <p>Groupement politique: {props.group_name} ({props.group_id})</p>
      <hr/>
    </div>
    );
}

Deputy.propTypes = {
  id: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  surname: PropTypes.string.isRequired,
  slug: PropTypes.string.isRequired,
  // sex: PropTypes.bool.isRequired,
  mail: PropTypes.string.isRequired,
  birth_date: PropTypes.string.isRequired,
  birth_town: PropTypes.string.isRequired,
  birth_department: PropTypes.string.isRequired,
  birth_country: PropTypes.string,
  work_name: PropTypes.string,
  work_category: PropTypes.string,
  work_familly: PropTypes.string,
  group: PropTypes.string.isRequired,
  group_id: PropTypes.string.isRequired,
  group_name: PropTypes.string.isRequired,
}

module.exports = Deputy;

/////////////////////////////////
// {
//     "id": "PA607155",
//     "group_id": "PO656002",
//     "group_name": "'Parti socialiste'",
//     "name": "Daniel",
//     "surname": "Yves",
//     "slug": "Daniel-Yves",
//     "sex": "False",
//     "mail": "ydaniel@assemblee-nationale.fr",
//     "birth_date": "1954-07-31",
//     "birth_town": "Mouais",
//     "birth_department": "Loire-Atlantique",
//     "birth_country": "France",
//     "work_name": "Agriculteur-propriétaire exploitant",
//     "work_category": "Agriculteurs-propriétaires exploitants",
//     "work_familly": "Agriculteurs",
//     "group": "PO656002",
//     "substitute": null
// },