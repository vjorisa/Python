 ASCII Galaxy Animation

A simple Python project that renders an animated spiral galaxy directly in the terminal using ASCII characters.

The galaxy is generated mathematically using polar coordinates, spiral arm equations, and brightness calculations to create a rotating galaxy effect.

 Features
Animated spiral galaxy in the terminal.
Two spiral arms generated using mathematical equations.
Realistic brightness distribution with a central galactic bulge.
ASCII characters used to represent different light intensities.
Smooth rotation animation.
Adjustable galaxy parameters.
 Technologies Used
Python
NumPy
ASCII Art
Mathematical calculations (Polar Coordinates, Trigonometry, Exponential Functions)
 Requirements

Make sure you have Python installed.

Install NumPy:

bash
pip install numpy

 How to Run
Clone the repository:
bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Navigate to the project directory:
bash
cd YOUR-REPOSITORY

Run the script:
bash
python galaxy.py


Press CTRL + C to stop the animation.

 Configuration

You can customize the galaxy by modifying these parameters:

Parameter	Description
WIDTH	Terminal width
HEIGHT	Terminal height
R_BULGE	Size of the central bulge
ARMS	Number of spiral arms
PITCH	Spiral arm curvature
OMEGA	Galaxy rotation speed
DENSITY_CHARS	ASCII brightness characters
 How It Works

The animation uses mathematical equations to simulate a spiral galaxy:

Polar Coordinates: Convert terminal coordinates into radius and angle.
Logarithmic Spiral: Generate the spiral structure.
Trigonometry: Calculate the intensity of the spiral arms.
Exponential Decay: Simulate the bright central bulge.
ASCII Rendering: Convert brightness values into different ASCII characters.
 Project Goal

The goal of this project is to explore how mathematics and Python can be combined to create visual simulations directly inside a terminal.

📄 License

This project is open-source. Feel free to explore, modify, and improve it.
