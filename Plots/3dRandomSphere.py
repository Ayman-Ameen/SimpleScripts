import numpy as np
from plotly.subplots import make_subplots

import plotly.graph_objects as go

# Generate random sphere data
num_spheres = 100
radii = np.random.uniform(10, 50, num_spheres)
x_max, x_min, y_max, y_min, z_max, z_min = 1, -1, 1, -1, 1, -1
x_coords_start = np.random.uniform(x_min, x_max, num_spheres)
y_coords_start = np.random.uniform(y_min, y_max, num_spheres)
z_coords_start = np.random.uniform(z_min, z_max, num_spheres)
x_coords_end = np.random.uniform(x_min, x_max, num_spheres)
y_coords_end = np.random.uniform(y_min, y_max, num_spheres)
z_coords_end = np.random.uniform(z_min, z_max, num_spheres)

# Generate random colors
colors = np.random.randint(0, 256, (num_spheres, 3))

# Create a figure
fig = go.Figure()

# Add initial scatter plot
fig.add_trace(go.Scatter3d(
    x=x_coords_start,
    y=y_coords_start,
    z=z_coords_start,
    mode='markers',
    marker=dict(
        size=radii,
        color=colors,
        opacity=1
    )
))

# # Add final scatter plot
# fig.add_trace(go.Scatter3d(
#     x=x_coords_end,
#     y=y_coords_end,
#     z=z_coords_end,
#     mode='markers',
#     marker=dict(
#         size=radii,
#         color=colors,
#         opacity=1
#     )
# ))

# Set plot layout
fig.update_layout(
    scene=dict(
        xaxis=dict(title='', showgrid=False, showticklabels=False, visible=False),
        yaxis=dict(title='', showgrid=False, showticklabels=False, visible=False),
        zaxis=dict(title='', showgrid=False, showticklabels=False, visible=False),
        bgcolor='black'
    ),
    title='3D Random Spheres',
    plot_bgcolor='black'
)

# Create animation frames
frames = []
num_frames = 50  # Number of frames in the animation
for i in range(num_frames):
    # Interpolate positions between start and end coordinates
    t = i / (num_frames - 1)
    x_coords_interpolated = (1 - t) * x_coords_start + t * x_coords_end
    y_coords_interpolated = (1 - t) * y_coords_start + t * y_coords_end
    z_coords_interpolated = (1 - t) * z_coords_start + t * z_coords_end
    
    # Add interpolated scatter plot to frames
    frame = go.Frame(data=[go.Scatter3d(
        x=x_coords_interpolated,
        y=y_coords_interpolated,
        z=z_coords_interpolated,
        mode='markers',
        marker=dict(
            size=radii,
            color=colors,
            opacity=1
        )
    )])
    frames.append(frame)

# Add frames to animation
fig.frames = frames

# Set animation settings
animation_settings = dict(
    frame=dict(duration=100, redraw=True),
    fromcurrent=True,
    transition=dict(duration=0),
    mode='immediate'
)

# Add animation buttons
fig.update_layout(updatemenus=[
    dict(
        type='buttons',
        buttons=[
            dict(label='Play',
                 method='animate',
                 args=[None, animation_settings]),
            dict(label='Pause',
                 method='animate',
                 args=[[None], animation_settings])
        ],
        showactive=False,
        x=0.1,
        y=0,
        xanchor='left',
        yanchor='bottom'
    )
])

# Show the plot
fig.show()
