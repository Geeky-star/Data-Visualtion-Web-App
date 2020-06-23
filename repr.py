import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from bokeh.plotting import figure
import pydeck as pdk
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import graphviz as graphviz

st.header("Play with Charts and numbers")
st.subheader("Visualize the data by changing numeric values")

option = st.sidebar.selectbox("Choose Chart", ("Line Chart", "Bar Chart", "Area Chart", "Altair Chart", "Plotly Chart","Bokeh Chart", "Pydeck Chart", "Deck gl Chart","Graphviz Chart","Pyplot", "Map"))
if option == "Altair Chart":
    x = st.sidebar.slider("Set x", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(x,3), columns=['a','b','c'])
    choice = st.sidebar.selectbox("Choose Geometry", ("Circle", "Rectangle", "Triangle"))
    if choice == "Circle":
        c = alt.Chart(df).mark_circle().encode(x = 'a', y='b', size='c', color='c', tooltip = ['a','b','c'])
        st.write(c)

if option == "Bokeh Chart":
    x = [1,2,3,4,5]
    y = [6,7,2,4,5]
    p = figure(title = "simple", x_axis_label = 'x', y_axis_label = 'y')
    p.line(x,y,legend_label = 'Trend', line_width=2)
    st.bokeh_chart(p, use_container_width = True)

if option == "Pydeck Chart":
    x = st.sidebar.slider("Set x", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(x,2)/[50,50]+[37.76, -122.4], columns=['latitude', 'longitude'])
    st.pydeck_chart(pdk.Deck(map_style = 'mapbox://styles/mapbox/light-v9',
                             initial_view_state=pdk.ViewState(latitude=37.76, longitude=-122.4, zoom=11, pitch=50,),
                             layers = [pdk.Layer('Hexagonlayer', data=df, get_position = '[longitude, latitude]',
                                                 radius=200, elevation_scale=4, elevation_range=[0,1000],
                                                 pickable=True, extruded=True,),
                                       pdk.Layer('ScatterplotLayer', data=df,
                                                 get_position= '[longitude, latitude]',
                                                 get_color='[200,30,0,160]', get_radius=200),],))

if option == "Deck gl Chart":
    s = st.sidebar.slider("Set x", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(s,2)/[50,50]+[37.76, -122.4], columns=['latitude', 'longitude'])
    st.deck_gl_chart(viewport = {'latitude': 37.76, 'longitude': -122.4, 'zoom': 11, 'pitch': 50,},
                     layers = [{'type': 'HexagonLayer', 'data': df, 'radius':200, 'elevationScale': 4, 'elevationRange':[0,1000], 'pickable': True, 'extruded': True,},
                               {'type': 'ScatterplotLayer', 'data': df,}])

if option == "Map":
    x = st.sidebar.slider("Set the Density", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(x ,2)/[50,50] + [37.76, - 122.4], columns = ['lat','lon'])
    st.map(df)

if option == "Line Chart":
    p = st.sidebar.slider("Set x", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(p,3), columns = ['a','b','c'])
    st.line_chart(df)

if option == "Area Chart":
    x = st.sidebar.slider("Set x", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(x,3), columns = ['a','b','c'])
    st.area_chart(df)

if option == "Bar Chart":
    l = st.sidebar.slider("Set x", 1, 1000, 1)
    df = pd.DataFrame(np.random.randn(l,3), columns = ['a','b','c'])
    st.bar_chart(df)

if option == "Pyplot":
    array = np.random.normal(1,1, size=100)
    plt.hist(array, bins=20)
    st.pyplot()

if option == "Plotly Chart":
    x1 = np.random.randn(200)-2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200)+2

    hist_data = [x1,x2,x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']

    fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1, .25,.5])
    st.plotly_chart(fig, use_container_width = True)

if option == "Graphviz Chart":
    graph = graphviz.Digraph()
    graph.edge('run', 'intr')
    graph.edge('intr', 'runbl')
    graph.edge('runbl', 'run')
    graph.edge('run', 'kernel')
    graph.edge('kernel', 'zombie')
    graph.edge('kernel', 'sleep')
    graph.edge('kernel', 'runmem')
    graph.edge('sleep', 'swap')
    graph.edge('swap', 'runswap')
    graph.edge('runswap', 'new')
    graph.edge('new', 'runmem')
    graph.edge('sleep', 'runmem')

    st.graphviz_chart(graph)