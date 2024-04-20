import React from 'react';
import Feature from '../../components/feature/Feature';
import './whatvb.css';

const Whatvb = () => (
  <div className="vb__whatvb section__margin" id="wvb">
    <div className="vb__whatvb-feature">
      <Feature title="What is Veribloc" text="Access a curated list of active research studies seeking diverse global contributions. Our listings are tailored to connect researchers with the ideal participants." />
    </div>
    <div className="vb__whatvb-heading">
      <h1 className="gradient__text">Unlock a world of diverse data and collaborative potential with studies spanning across various fields and cultures.</h1>
      <p>View Studies</p>
    </div>
    <div className="vb__whatvb-container">
      <Feature title="Featured Studies" text="Browse our selected studies showcasing the need for unique data sets from various demographics and regions." />
      <Feature title="Recently Added" text="Check out the newest studies listed on VeriBloc, expanding the horizons of scientific research every day." />
      <Feature title="Top Categories" text="Delve into the most sought-after research categories, from healthcare to environmental science, and contribute to cutting-edge studies." />
    </div>
  </div>
);

export default Whatvb;
