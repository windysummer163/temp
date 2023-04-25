import streamlit as st
import datetime


st.markdown(
    """
    <div style='background-color: green; padding: 10px;'>
        <h2 style='color: white; text-align: center; font-size: 20px;'>This is a No-Q verified result</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Set the target datetime
target_datetime = datetime.datetime(2023, 4, 21, 17, 23, 0)

# Calculate time elapsed
time_elapsed = datetime.datetime.now() - target_datetime
hours, remainder = divmod(time_elapsed.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
# Display time elapsed
# st.markdown("<h1 style='text-align: center;font-size: 20;'>TIME SINCE TEST</h1>", unsafe_allow_html=True)
st.write("")

st.write(f"<p style='text-align: center; font-size: 20px; '> TIME SINCE TEST</p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {hours} h {minutes} min</p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {target_datetime} CET </p>", unsafe_allow_html=True)

st.write("---")

st.write(f"<p style='text-align: center; font-size: 20px; '> NAME </p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> Xiaoyu Zhang </p>", unsafe_allow_html=True)

st.write("---")

st.write(f"<p style='text-align: center; font-size: 20px; '> RESULT </p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> Negativ </p>", unsafe_allow_html=True)

st.write("---")

st.write(f"<p style='text-align: center; font-size: 20px; '> TEST LOCATION </p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> Rathaus-Apotheke </p>", unsafe_allow_html=True)
