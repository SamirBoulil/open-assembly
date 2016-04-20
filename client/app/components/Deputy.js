var React = require('react');
var PropTypes = React.PropTypes;

var Deputy = function(props) {
  var sexLabel = props.sex ? "Mme" : "Mr.";
  props.age = "12";
  return (
    <div className="card">
      <h2 className="card__title">{props.surname} {props.name}</h2>
      <div className="card__pane_1">
        <div>{props.group_name} ({props.group_id})</div>
      </div>
      <div className="card__pane_2">
        <div className="">Profession: {props.work_name} ({props.work_familly})</div>
        <div className="">age: 54 ans</div>
      </div>
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
// <p>Originaire de: {props.birth_town} - {props.birth_department} - {props.birth_country}</p>
