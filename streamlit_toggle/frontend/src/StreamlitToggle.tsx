import React, { ReactNode } from "react"
import { Checkbox, STYLE_TYPE } from 'baseui/checkbox';
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"

interface State {
  value: boolean
}

class StreamlitToggle extends StreamlitComponentBase<State> {
  public state = { value: this.props.args["value"] }

  public render = (): ReactNode => {

    return (
      <div className="Widget row-widget stCheckbox">
      <Checkbox
        checked={this.state.value}
        disabled={this.props.args["disabled"]}
        onChange={this.onChange}
        checkmarkType={STYLE_TYPE.toggle_round}
      >
      </Checkbox>
      {this.props.args["label"]} 
      </div>
    )
  }

private onChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
    const isChecked = e.currentTarget.checked
    this.setState({ value: isChecked }, () => {
      Streamlit.setComponentValue(isChecked)
    })
  }
}

export default withStreamlitConnection(StreamlitToggle)
