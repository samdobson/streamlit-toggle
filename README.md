# A toggle switch widget for Streamlit

![Toggle Switch](screenshot.png?raw=true "Streamlit Toggle Switch")

## Usage

```python
import streamlit as st
from streamlit_toggle import st_toggleswitch

awesomeness_enabled = st_toggleswitch("Enable awesomeness")
if awesomeness_enabled:
    st.write("Awesomeness has been enabled!")
```
