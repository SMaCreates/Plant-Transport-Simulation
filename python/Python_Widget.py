import streamlit as st
from simulation import water_uptake, phloem_unloading 

soil_moisture = st.slider('Soil Moisture', 0, 100, 50)
st.write('Water Uptake:', water_uptake(soil_moisture)) 

pressure = st.slider('Pressure', 0, 100, 50)
sink_demand = st.slider('Sink Demand', 0, 100, 50)
st.write('Phloem Unloading:', phloem_unloading(pressure, sink_demand))

