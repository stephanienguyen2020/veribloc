import React, { useState } from 'react';
import { RiMenu3Line, RiCloseLine } from 'react-icons/ri';
import logo from '../../assets/veribloc_logo.png';
import './navbar.css';

import {Link} from 'react-router-dom';

const Navbar = () => {
  const [toggleMenu, setToggleMenu] = useState(false);

  return (
    <div className="vb__navbar">
      <div className="vb__navbar-links">
        <div className="vb__navbar-links_logo">
          <img src={logo} alt="logo" />
        </div>
        <div className="vb__navbar-links_container">
          <p><Link to="/about">About Us</Link></p>
          <p><Link to="/listings">Study Listings</Link></p>
          <p><Link to="/pricing">Pricing</Link></p>
          <p><Link to="/support">Help & Support</Link></p>
        </div>
      </div>
      <div className="vb__navbar-sign">
          <p><Link to="/signin">Sign in</Link></p>
          <button type="button"><Link to="/signup">Sign up</Link></button>
      </div>
      <div className="vb__navbar-menu">
        {toggleMenu
          ? <RiCloseLine color="#fff" size={27} onClick={() => setToggleMenu(false)} />
          : <RiMenu3Line color="#fff" size={27} onClick={() => setToggleMenu(true)} />}
        {toggleMenu && (
        <div className="vb__navbar-menu_container scale-up-center">
          <div className="vb__navbar-menu_container-links">
            <p><Link to="/about">About Us</Link></p>
            <p><Link to="/listings">Study Listings</Link></p>
            <p><Link to="/pricing">Pricing</Link></p>
            <p><Link to="/support">Help & Support</Link></p>
          </div>
          <div className="vb__navbar-menu_container-links-sign">
            <Link to="/signin">Sign in</Link>
            <Link to="/signup"><button type="button">Sign up</button></Link>
          </div>
        </div>
        )}
      </div>
    </div>
  );
};

export default Navbar;
