import React from 'react';
import logo from '../../assets/veribloc_logo.png';
import './footer.css';

const Footer = () => (
  <div className="vb__footer section__padding">
    <div className="vb__footer-heading">
      <h1 className="gradient__text">Do you want to step in to the future before others</h1>
    </div>

    <div className="vb__footer-btn">
      <p>Request Early Access</p>
    </div>

    <div className="vb__footer-links">
      <div className="vb__footer-links_logo">
        <img src={logo} alt="logo" />
        <p>Crechterwoord K12 182 DK Alknjkcb, <br /> All Rights Reserved</p>
      </div>
      <div className="vb__footer-links_div">
        <h4>Links</h4>
        <p>Overons</p>
        <p>Social Media</p>
        <p>Counters</p>
        <p>Contact</p>
      </div>
      <div className="vb__footer-links_div">
        <h4>Company</h4>
        <p>Terms & Conditions </p>
        <p>Privacy Policy</p>
        <p>Contact</p>
      </div>
      <div className="vb__footer-links_div">
        <h4>Get in touch</h4>
        <p>Crechterwoord K12 182 DK Alknjkcb</p>
        <p>085-132567</p>
        <p>info@payme.net</p>
      </div>
    </div>

    <div className="vb__footer-copyright">
      <p>@2024 VeriBloc. All rights reserved.</p>
    </div>
  </div>
);

export default Footer;
