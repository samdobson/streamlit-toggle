import os
import streamlit.components.v1 as components

_RELEASE = False
if not _RELEASE:
    _component_func = components.declare_component(
        "st_toggleswitch",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_toggleswitch", path=build_dir)

def st_toggleswitch(label, value=True, disabled=False, key=None):
    """Display a toggle switch.

    Parameters
    ----------
    label: str
        A short label explaining to the user what this toggle switch is for.
    value: bool
        Default the toggle switch to activated when it first renders
        (True if not specified).
    disabled: bool
        Disable the widget so that it cannot be changed
        (False if not specified).
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    bool
        Whether or not the toggle switch is activated.
    """
    component_value = _component_func(label=label, value=value, disabled=disabled, key=key, default=value)
    return component_value

if not _RELEASE:
    import streamlit as st

    st.subheader("Toggle Switch Streamlit Component")
    awesomeness_enabled = st_toggleswitch("Enable awesomeness")
    if awesomeness_enabled:
        st.markdown("Awesomeness has been enabled!")