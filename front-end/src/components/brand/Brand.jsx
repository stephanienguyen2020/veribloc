import React from 'react';
import { cornell, harvard, mit, yale, cmu } from './imports';
import './brand.css';

const Brand = () => (
  <div className="vb__brand section__padding">
    <div>
      <img src={cornell} />
    </div>
    <div>
      <img src={harvard} />
    </div>
    <div>
      <img src={mit} />
    </div>
    <div>
      <img src={yale} />
    </div>
    <div>
      <img src={cmu} />
    </div>
  </div>
);

export default Brand;
