import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

// import Dashboard from './pages/Dashboard'
// import Developer from './pages/Developer/Developer'
// import Login from './pages/Login'
// import Admin from './pages/Admin'

import Database from './pages/Database/Database'
import AIComponent from './pages/AI/AI'
import ACComponent from './pages/AC/AC'

import Landing from './pages/Landing'

import Nav from './components/common/Nav'
import Footer from './components/common/Footer'

function App () {
  return (
    <Router>
        <Nav />
        <Routes>
            <Route path='/' element={<Landing />} />
            {/* <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/admin" element={<Admin />} />
            <Route path="/developer" element={<Developer />} /> */}
            <Route path="/ai" element={<AIComponent />} />
            <Route path="/database" element={<Database />} />
            <Route path="/ac" element={<ACComponent />} />
        </Routes>
        <Footer />
    </Router>

  )
}

export default App
