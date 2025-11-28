import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Fetching Activities from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched Activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2>Activities</h2>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.type} - {activity.duration} min on {activity.date}</li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
