import React, { useEffect, useState } from 'react';

export default function Leaderboard() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const endpoint = codespace
      ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
      : `http://localhost:8000/api/leaderboard/`;
    console.log('Leaderboard endpoint:', endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Leaderboard fetched data:', json);
        let data;
        if (Array.isArray(json)) data = json;
        else if (json && json.results) data = json.results;
        else data = [json];
        setItems(data);
      })
      .catch(err => console.error('Error fetching Leaderboard:', err));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {items.map((it, idx) => (
          <li className="list-group-item" key={it.id || idx}>
            {JSON.stringify(it)}
          </li>
        ))}
      </ul>
    </div>
  );
}
