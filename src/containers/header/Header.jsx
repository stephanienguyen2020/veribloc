import React from 'react';
import people from '../../assets/people.png';
import header_logo from '../../assets/header_logo.png';
import './header.css';

const Header = () => (
  <div className="vb__header section__padding" id="home">
    <div className="vb__header-content">
      <h1 className="gradient__text">VeriBloc: Bridging Data, Building Trust</h1>
      <p> Your One-Stop Blockchain-Powered Data Exchange Platform for Research Innovation. Connect with diverse data contributors and researchers seamlessly for trusted insights. </p>

      <div className="vb__header-content__input">
        <input type="email" placeholder="Your Email Address" />
        <button type="button">Get Started</button>
      </div>

      <div className="vb__header-content__people">
        <img src={people} />
        <p>Join 1,600,000+ other contributors from 48+ countries </p>
      </div>
    </div>

    <div className="vb__header-image">
      <img src={header_logo} />
    </div>
  </div>
);

export default Header;
