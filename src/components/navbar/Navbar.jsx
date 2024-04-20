import React, { useState } from 'react';
import { RiMenu3Line, RiCloseLine } from 'react-icons/ri';
import logo from '../../assets/veribloc_logo.png';
import './navbar.css';

const Navbar = () => {
  const [toggleMenu, setToggleMenu] = useState(false);

  return (
    <div className="vb__navbar">
      <div className="vb__navbar-links">
        <div className="vb__navbar-links_logo">
          <img src={logo} alt="logo" />
        </div>
        <div className="vb__navbar-links_container">
          <p><a href="#home">About Us</a></p>
          <p><a href="#wvb">Study Listings</a></p>
          <p><a href="#possibility">Pricing</a></p>
          <p><a href="#features">Help & Support</a></p>
        </div>
      </div>
      <div className="vb__navbar-sign">
        <p>Sign in</p>
        <button type="button">Sign up</button>
      </div>
      <div className="vb__navbar-menu">
        {toggleMenu
          ? <RiCloseLine color="#fff" size={27} onClick={() => setToggleMenu(false)} />
          : <RiMenu3Line color="#fff" size={27} onClick={() => setToggleMenu(true)} />}
        {toggleMenu && (
        <div className="vb__navbar-menu_container scale-up-center">
          <div className="vb__navbar-menu_container-links">
            <p><a href="#home">About Us</a></p>
            <p><a href="#wvb">Study Listings</a></p>
            <p><a href="#possibility">Pricing</a></p>
            <p><a href="#features">Help & Support</a></p>
          </div>
          <div className="vb__navbar-menu_container-links-sign">
            <p>Sign in</p>
            <button type="button">Sign up</button>
          </div>
        </div>
        )}
      </div>
    </div>
  );
};

export default Navbar;
