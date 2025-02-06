import numpy as np

def generate_openscad_script(block_width, block_height, spacing, surface_width, surface_height, filename):
    """
    Generate an OpenSCAD script to create an array of square blocks with a 10um x 10um contact area.

    Parameters:
    - block_width: Width of the contact area of each block (in um)
    - block_height: Height of each block (in um)
    - spacing: Spacing between blocks (in um)
    - surface_width: Width of the surface area to cover (in um)
    - surface_height: Height of the surface area to cover (in um)
    - filename: Name of the file to save the OpenSCAD script
    """
    blocks = []
    x_positions = np.arange(0, surface_width, block_width + spacing)
    y_positions = np.arange(0, surface_height, block_width + spacing)

    # Generate block positions
    for x in x_positions:
        for y in y_positions:
            blocks.append((x, y))

    # Create OpenSCAD script
    with open(filename, "w") as file:
        file.write("// OpenSCAD script to generate an array of square blocks\n")
        file.write(f"module block() {{\n  cube([{block_width}, {block_width}, {block_height}], center = true);\n}}\n")

        file.write("translate([0, 0, 0])\n");
        file.write("{\n");
        for x, y in blocks:
            file.write(f"translate([{x}, {y}, {block_height / 2}]) block();\n")
        file.write("}\n")

# Parameters
block_width = 55  # um (contact area width and depth)
block_height = 200  # um
spacing = 400  # um
surface_width = 3000  # um (3 mm)
surface_height = 3000  # um (3 mm)
output_file = "array_of_blocks.scad"

# Generate OpenSCAD script
generate_openscad_script(block_width, block_height, spacing, surface_width, surface_height, output_file)

print(f"OpenSCAD script saved to {output_file}")

