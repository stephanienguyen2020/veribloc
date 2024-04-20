import React from "react";
import { Footer, Possibility, Features, Whatvb, Header } from "./containers";
import Navbar from "./components/navbar/Navbar";
import LoginForm from './components/loginform/LoginForm';
import { CTA, Brand } from "./components";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";

const App = () => (
  <BrowserRouter>
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/signin" element={<LoginForm />} />
      </Routes>
      <div className="gradient__bg">
              <Header />
      </div>
      <Brand />
      <Whatvb />
      <Possibility />
      <Features />
      <CTA />
      <Footer />
    </div>
  </BrowserRouter>
);

export default App;