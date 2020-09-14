import React from 'react';
import styled from 'styled-components'
import Navbar from "./components/Navbar"
import TutorialView from "./components/TutorialView"



function App() {

  function clicked(e) {
    e.preventDefault();
    e.persist();
    console.log("LINK CLICK");
    console.log(e);
  }
  const navlinks = {
    "Google Site": "http://google.com",
    "Twitter Site": "http://twitter.com",
    "Instagram Site": "http://instagram.com",
    "Clicked" : clicked
  }
  return (
    <>
      <Navbar links={navlinks}/>
      <TutorialView />
    </>
  );
}

export default App;
