import React, { useEffect, useState } from 'react';
import Modal from './Modal';
import { getColumns, formatValue, ensureItems } from './utils';

export default function Workouts() {
  const [items, setItems] = useState([]);
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState(null);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const endpoint = codespace
      ? `https://${codespace}-8000.app.github.dev/api/workouts/`
      : `http://localhost:8000/api/workouts/`;
    console.log('Workouts endpoint:', endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Workouts fetched data:', json);
        setItems(ensureItems(json));
      })
      .catch(err => console.error('Error fetching Workouts:', err));
  }, []);

  const columns = getColumns(items);
  const filtered = items.filter(it => !query || JSON.stringify(it).toLowerCase().includes(query.toLowerCase()));
  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header d-flex align-items-center justify-content-between">
          <h2 className="h5 mb-0">Workouts</h2>
          <div className="d-flex gap-2">
            <input className="form-control form-control-sm" placeholder="Search..." value={query} onChange={e => setQuery(e.target.value)} />
            <button className="btn btn-sm btn-primary" onClick={() => window.location.reload()}>Refresh</button>
          </div>
        </div>
        <div className="card-body p-0">
          {filtered.length === 0 ? (
            <div className="p-3">No workouts found.</div>
          ) : (
            <div className="table-responsive">
              <table className="table table-hover table-striped mb-0">
                <thead>
                  <tr>
                    {columns.map(col => (<th key={col}>{col}</th>))}
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filtered.map((it, idx) => (
                    <tr key={it.id || idx}>
                      {columns.map(col => (<td key={col}>{formatValue(it[col])}</td>))}
                      <td>
                        <button className="btn btn-sm btn-outline-primary" onClick={() => { setSelected(it); setShowModal(true); }}>Details</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
      <Modal title="Workout Details" show={showModal} onClose={() => setShowModal(false)}>
        <pre>{JSON.stringify(selected, null, 2)}</pre>
      </Modal>
    </div>
  );
}
