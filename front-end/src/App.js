import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Admin from './pages/Admin';
import MainWindow from './pages/MainWindow';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/admin" element={<Admin />} />
        <Route path='/' element={<MainWindow />} />
      </Routes>
    </Router>
  );
}

export default App;
