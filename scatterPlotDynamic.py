import plotly.graph_objects as go

x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 13, 17, 20, 25]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(size=10),
    name='Data Points'
))

fig.update_layout(
    title="Dynamic Scatter Plot",
    xaxis_title="X values",
    yaxis_title="Y values"
)

fig.show()
