import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Footer, Possibility, Features, Whatvb, Header } from "./containers";
import { CTA, Brand, Navbar } from "./components";
import LoginForm from "./components/loginform/LoginForm";
import "./App.css";

const App = () => (
  <div className="App">
    <div className="gradient__bg">
      <Navbar />
      <Header />
    </div>
    <Brand />
    <Whatvb />
    <Possibility />
    <Features />
    <CTA />
    <Footer />
  </div>
);

export default App;