import React from 'react';
import styled from 'styled-components'

const Ul = styled.ul`
  list-style-type: none;
  margin: 0;
  padding: 0;
  background-color: #dddddd;
  display: flex;
`

const A = styled.a`
  display: block;
  padding: 0.5em;
  background-color: #dddddd;
`

function Navbar(props) {
  const links = props.links
  const linkListItems = Object.keys(links).map(
    function (key, index) {
      if (typeof links[key] === 'string') {
        return (<li key={index}><A href={links[key]}>{key}</A></li>)
      } else if (typeof links[key] === 'function') {
        return (<li key={index}><A  href="#" onClick={ links[key] }>{key}</A></li>)
      } else {
        throw "Please only pass strings and functions to navbar."
      }
     }
  );
  return (
      <Ul>
        {linkListItems}
      </Ul>
  );
}

export default Navbar;
