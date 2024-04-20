import React from 'react';
import possibilityImage from '../../assets/possibility.png';
import './possibility.css';

const Possibility = () => (
  <div className="vb__possibility section__padding" id="possibility">
    <div className="vb__possibility-image">
      <img src={possibilityImage} alt="possibility" />
    </div>
    <div className="vb__possibility-content">
      <h4>Join Top Research Institutions Today</h4>
      <h1 className="gradient__text">Unlock a world of diverse data <br /> and collaborative potential</h1>
      <p>Discover research opportunities and connect with other researchers worldwide. Explore a curated list of active research studies seeking diverse global contributions, spanning across various fields and cultures.</p>
      <h4>Verify Your Institution Credentials to Get Started!</h4>
    </div>
  </div>
);

export default Possibility;
