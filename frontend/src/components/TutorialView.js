import React from 'react';
import styled from 'styled-components'
import ConsoleSection from "./ConsoleSection"
import TutorialSection from "./TutorialSection"
function TutorialView(props) {
  const Div = styled.div`
    display: flex;
    justify-content: flex-start;
    width: 100%;
    flex-wrap: nowrap;
    flex-direction: row;
    height: calc(100% - 34px);
    overflow: hidden;
  `
  return (
  <Div>
    <TutorialSection />
    <ConsoleSection />
  </Div>

  )
}

export default TutorialView;
