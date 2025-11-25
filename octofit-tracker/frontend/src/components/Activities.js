import React, { useEffect, useState } from 'react';

export default function Activities() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const endpoint = codespace
      ? `https://${codespace}-8000.app.github.dev/api/activities/`
      : `http://localhost:8000/api/activities/`;
    console.log('Activities endpoint:', endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Activities fetched data:', json);
        let data;
        if (Array.isArray(json)) data = json;
        else if (json && json.results) data = json.results;
        else data = [json];
        setItems(data);
      })
      .catch(err => console.error('Error fetching Activities:', err));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
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
