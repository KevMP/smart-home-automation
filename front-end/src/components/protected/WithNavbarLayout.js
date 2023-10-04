import React from 'react';
import Nav from '../components/common/nav';

function WithNavbarLayout({ children }) {
  return (
    <div>
      <Nav/ >
      <div>{children}</div>
    </div>
  );
}

export default WithNavbarLayout;
