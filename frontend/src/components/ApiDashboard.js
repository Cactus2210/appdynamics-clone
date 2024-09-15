import React, { useState, useEffect } from 'react';
import apiService from '../services/apiService';

const ApiDashboard = () => {
  const [apiStatus, setApiStatus] = useState([]);

  useEffect(() => {
    apiService.getApiStatus().then((status) => setApiStatus(status));
  }, []);

  return (
    <div>
      <h1>API Dashboard</h1>
      <ul>
        {apiStatus.map((api, index) => (
          <li key={index}>
            {api.url} - Status: {api.status_code} - Latency: {api.latency}ms
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ApiDashboard;
