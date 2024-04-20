import React from "react";
import "./features.css";
import Christopher from "../../assets/team/Christopher.jpg";
import Uyen from "../../assets/team/Uyen.jpg";
import Stephanie from "../../assets/team/Stephanie.jpg";

const teamMembers = [
  {
    imgUrl: Uyen,
    name: "Uyen Hoang",
    position: "UI/UX Designer",
  },
  {
    imgUrl: Stephanie,
    name: "Stephanie Ng",
    position: "PM, Front-end & Blockchain Dev",
  },
  {
    imgUrl: Christopher,
    name: "Christopher Le",
    position: "Backend & AI Dev",
  },
];

const Features = () => (
  <section className="our__team">
    <div className="container">
      <div className="team__content">
        <h1 className="gradient__text">Meet the Team</h1>
      </div>
      <div className="team__wrapper">
        {teamMembers.map((item, index) => (
          <div className="team__item" key={index}>
            <div className="team__img">
              <img src={item.imgUrl} alt={item.name} />
            </div>
            <div className="team__details">
              <h4>{item.name}</h4>
              <p className="description">{item.position}</p>
              <div className="team__member-social">
                <span>
                  <i className="ri-linkedin-line"></i>
                </span>
                <span>
                  <i className="ri-twitter-line"></i>
                </span>
                <span>
                  <i className="ri-facebook-line"></i>
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Features;
