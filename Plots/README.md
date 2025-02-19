# 3D Random Spheres Animation

This Python script generates a 3D animation of randomly positioned and sized spheres using the Plotly library. The spheres smoothly transition from a set of initial coordinates to a set of final coordinates.

## Prerequisites

-   Python 3.6 or higher
-   Plotly library
-   Numpy library

You can install the required libraries using pip:

```bash
pip install plotly numpy
```

## How to Run

1.  Save the script as a `.py` file (e.g., `3d_spheres.py`).
2.  Run the script from your terminal:

```bash
python 3d_spheres.py
```

The script will open an interactive plot in your web browser, displaying the animation. You can use the play/pause buttons to control the animation.

## Customization

You can customize the animation by modifying the following parameters in the script:

-   `num_spheres`: Number of spheres in the animation.
-   `radii`: Range of radii for the spheres.
-   `x_max, x_min, y_max, y_min, z_max, z_min`: Boundaries for the initial and final coordinates of the spheres.
-   `colors`: Colors of the spheres.
-   `num_frames`: Number of frames in the animation.
-   `frame_duration`: Duration of each frame in milliseconds.

## Output

The script generates an interactive 3D plot that displays an animation of spheres moving from their initial positions to their final positions.

