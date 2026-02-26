import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

x1 = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 17, 20]

x2 = [1, 2, 3, 4, 5]
y2 = [5, 7, 9, 11, 13]

fig.add_trace(
    go.Scatter(x=x1, y=y1, mode='markers', name='Plot 1'),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=x2, y=y2, mode='markers', name='Plot 2'),
    row=1, col=2
)
fig.update_layout(title="Dynamic Subplots")

fig.show()
