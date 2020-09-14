import React, {useState} from 'react';
import styled from 'styled-components'
import ReactConsole from '@webscopeio/react-console'


function ConsoleSection(props) {
  const [history, setHistory] = useState();
  return (
      <ReactConsole
          autoFocus
          welcomeMessage="Initializing..."
          wrapperStyle={
            { flexGrow:"2", alignSelf:"flex-start", height: "100%"}
          }
          commands={{
            history: {
              description: 'History',
              fn: () => new Promise(resolve => {
                 resolve(`${history.join('\r\n')}`)
              })
            }
          }}
          noCommandFound={
            (str) => new Promise(resolve => {
              
              resolve(`${str}`)
            })
          }
        />
  )
}

export default ConsoleSection;
