import React from 'react';
import styled from 'styled-components'

function TutorialSection(props) {
  var text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sit amet mauris tincidunt, tristique mauris a, interdum enim. Nulla maximus nunc a massa rhoncus, at viverra sem tempor."
  const Div = styled.div`
    flex-grow: 1;
    padding: 8px;
    width: 0%;
  `
  return (
    <Div>
      <p>{text}</p>
    </Div>
  )
}

export default TutorialSection;
