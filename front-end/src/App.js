import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Dashboard from './pages/Dashboard';
import Admin from './pages/Admin';
import Database from './pages/Database';

import Login from './pages/Login';
import Landing from './pages/Landing';

import Nav from './components/common/Nav';
import Footer from './components/common/Footer';

function App() {
  return (
    <Router>
        <Nav />
        <Routes>
            <Route path='/' element={<Landing />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/admin" element={<Admin />} />
            <Route path="/database" element={<Database />} />
        </Routes>
        <Footer />
    </Router>

  );
}

export default App;
