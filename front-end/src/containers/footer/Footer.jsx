import React from 'react';
import logo_light from '../../assets/vb_light.png';
import './footer.css';

const Footer = () => (
  <div className="vb__footer section__padding">
    <div className="vb__footer-heading">
      <h1 className="gradient__text">Ready to Lead the Way in Science?</h1>
    </div>

    <div className="vb__footer-btn">
      <p>Join Now</p>
    </div>

    <div className="vb__footer-links">
      <div className="vb__footer-links_logo">
        <img src={logo_light} alt="logo" />
        <p>116th & Broadway, NY 10027 <br /> All Rights Reserved</p>
      </div>
      <div className="vb__footer-links_div">
        <h4 style={{ fontWeight: 'bold' }}>Links</h4>
        <p>Success Stories</p>
        <p>News & Events</p>
        <p>Contact Us</p>
      </div>
      <div className="vb__footer-links_div">
        <h4 style={{ fontWeight: 'bold' }}>Company</h4>
        <p>Terms & Conditions </p>
        <p>Privacy Policy</p>
        <p>Careers</p>
      </div>
      <div className="vb__footer-links_div">
        <h4 style={{ fontWeight: 'bold' }}>Get in touch</h4>
        <p>116th & Broadway, NY 10027</p>
        <p>012-345-6789</p>
        <p>info@veribloc.com</p>
      </div>
    </div>

    <div className="vb__footer-copyright">
      <p>@2024 VeriBloc. All rights reserved.</p>
    </div>
  </div>
);

export default Footer;
