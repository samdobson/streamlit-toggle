import React from "react"
import ReactDOM from "react-dom"
import StreamlitToggle from "./StreamlitToggle"
import {Client as Styletron} from 'styletron-engine-atomic';
import {Provider as StyletronProvider} from 'styletron-react';
import {ThemeProvider, LightTheme} from 'baseui';

const engine = new Styletron();

ReactDOM.render(
  <React.StrictMode>
    <StyletronProvider value={engine}>
      <ThemeProvider theme={LightTheme}>
        <StreamlitToggle/>
      </ThemeProvider>
    </StyletronProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
