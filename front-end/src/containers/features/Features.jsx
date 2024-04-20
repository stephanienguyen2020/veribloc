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
    linkedin: "https://www.linkedin.com/in/uyenhoang2903/",
  },
  {
    imgUrl: Stephanie,
    name: "Stephanie Ng",
    position: "PM, Front-end & Blockchain Dev",
    linkedin: "https://www.linkedin.com/in/steph-tien-ng",
  },
  {
    imgUrl: Christopher,
    name: "Christopher Le",
    position: "Backend & AI Dev",
    linkedin: "https://www.linkedin.com/in/chrislevn/",
  },
];

const Features = () => (
  <section className="our__team">
    <div className="container">
      <div className="vb__features-heading">
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
              <a href={item.linkedin} target="_blank" rel="noopener noreferrer">
                <span style={{ color: "#0077B5", fontStyle: "italic" }}>
                  LinkedIn
                </span>
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Features;
