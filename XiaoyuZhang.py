import streamlit as st
import datetime
import pytz

# Set the timezone to Europe/Berlin
berlin_tz = pytz.timezone('Europe/Berlin')

# Get the current time in Berlin timezone
current_time_berlin = datetime.datetime.now(berlin_tz)

st.markdown(
    """
    <div style='background-color: green; padding: 10px;'>
        <h2 style='color: white; text-align: center; font-size: 20px;'>This is a No-Q verified result</h2>
    </div>
    """,
    unsafe_allow_html=True
)
start_time = berlin_tz.localize(datetime.datetime(2023, 4, 26, 17, 20, 0))
current_time = datetime.datetime.now(berlin_tz)

time_elapsed = current_time - start_time
total_seconds = int(time_elapsed.total_seconds())

hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

time_str = '{:d} h {:02d} min'.format(hours, minutes)

st.write("")

st.write(f"<p style='text-align: center; font-size: 20px; '> TIME SINCE TEST</p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {time_str}</p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {start_time} </p>", unsafe_allow_html=True)

st.write("---")

st.write(f"<p style='text-align: center; font-size: 20px; '> NAME </p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> Xiaoyu Zhang </p>", unsafe_allow_html=True)

st.write("---")

st.write(f"<p style='text-align: center; font-size: 20px; '> RESULT </p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> Negativ </p>", unsafe_allow_html=True)

st.write("---")

st.write(f"<p style='text-align: center; font-size: 20px; '> TEST LOCATION </p>", unsafe_allow_html=True)

st.write(f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> Rathaus-Apotheke </p>", unsafe_allow_html=True)
