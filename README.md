# A toggle switch widget for Streamlit

## Installation

Currently usable for Streamlit custom components beta testers only.

This will be published to PyPI once Streamlit 0.63.0 is released.

## Usage

```
import streamlit as st
from streamlit_toggle import st_toggleswitch

awesomeness_enabled = st_toggleswitch("Enable awesomeness")
if awesomeness_enabled:
    st.write("Awesomeness has been enabled!")
```