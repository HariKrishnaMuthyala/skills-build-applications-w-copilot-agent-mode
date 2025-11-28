import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Fetching Teams from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched Teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {teams.map(team => (
          <li key={team.id}>{team.name} - {team.description}</li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
