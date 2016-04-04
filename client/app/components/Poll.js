var React = require('react');
var PropTypes = React.PropTypes;

var Poll = function(props) {
  var resultLabel = props.is_accepted ? "Accepté" : "Refusé";
  return (
    <div className="poll">
      <h1>{props.poll_date} - {props.title}</h1>
      <p>Resultat: {resultLabel}</p>
      <p>Reference de session: {resultLabel}</p>
      <hr/>
    </div>
  );
}

Poll.propTypes = {
  id: PropTypes.string.isRequired,
  // department_vote_count_ok: 0,
  // department_vote_count_no: 0,
  // department_vote_count_abs: 0,
  // department_vote_count_not_voting: 7,
  title: PropTypes.string.isRequired,
  asked_by: PropTypes.string.isRequired,
  poll_date: PropTypes.string.isRequired, // Convert to date
  session_ref: PropTypes.string.isRequired,
  sceance_ref: PropTypes.string.isRequired,
  is_accepted: PropTypes.bool.isRequired, // convert to bool
  legislature: PropTypes.string.isRequired,
  // number_people_voting: 16,
  // number_votes_made: 14,
  // number_votes_required: 8,
  // number_votes_no: 557,
  // number_votes_yes: 2,
  // number_votes_dk: 12,
  // number_votes_not_voting: 2,
  // is_solemn: false
}

module.exports = Poll;

//////////////////////
// {
//     "id": "VTANR5L14V1244",
//     "department_vote_count_ok": 0,
//     "department_vote_count_no": 0,
//     "department_vote_count_abs": 0,
//     "department_vote_count_not_voting": 7,
//     "title": "l'amendement n° 5 (rect.) de M. Coronado et l'amendement identique n° 414 (rect.) de M. Cavard après l'article 31 du projet de loi renforçant la lutte contre le crime organisé, le terrorisme et leur financement, et améliorant l'efficacité et les garanties de la procédure pénale (première lecture).",
//     "asked_by": "Président du groupe Les Républicains",
//     "poll_date": "2016-03-03",
//     "session_ref": "SCR5A2016O1",
//     "sceance_ref": "",
//     "is_accepted": false,
//     "legislature": "14",
//     "number_people_voting": 16,
//     "number_votes_made": 14,
//     "number_votes_required": 8,
//     "number_votes_no": 557,
//     "number_votes_yes": 2,
//     "number_votes_dk": 12,
//     "number_votes_not_voting": 2,
//     "is_solemn": false
// },
