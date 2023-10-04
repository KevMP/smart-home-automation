import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


import Dashboard from './pages/Dashboard';
import Admin from './pages/Admin';
import Database from './pages/Database';

import Login from './pages/Login';
import Landing from './pages/Landing';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/database" element={<Database />} />

        <Route path="/login" element={<Login />} />
        <Route path='/' element={<Landing />} />
      </Routes>
    </Router>
  );
}

export default App;
