import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import ViewData from './pages/ViewData'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/view-data" element={<ViewData />} />
      </Routes>
    </Router>
  );
}

export default App;
