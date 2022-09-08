import cv2
import streamlit as st

st.title("Real Time - Attendance Register")
st.write("IndabaX - 2022")

start = st.checkbox('Start')

FRAME_WINDOW = st.image([])

cam = cv2.VideoCapture()

while start:
  ret, frame = cam.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  FRAME_WINDOW.image(frame)
else:
  st.write("stopped")
