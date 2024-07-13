import React from 'react';
import './header.css';

// Functional component
//FAUXTIONAL
function Header() {
  return (
    <div className="header">
      <p><em><b>Hardest Impossible Levels List</b></em></p>
      <a href='https://discord.gg/MHx4Nbp'><img  src={require('./ill_logo.png')} alt='Discord'></img></a>
    </div>
  );
}

export default Header;
