import rhinoscriptsyntax as rs
import random
import itertools

# List of angles for X, Y, Z axes
angles = [0, 45, 90, 135, 180, 225, 270, 315]

# Generate all possible rotations for X, Y, Z
def generate_rotations():
    return list(itertools.product(angles, repeat=3))

# Get random rotations from the generated list
def get_random_rotations(num_rotations):
    all_rotations = generate_rotations()
    return random.sample(all_rotations, num_rotations)

# Remove duplicate rotations based on appearance from all angles
def get_unique_rotations(rotations):
    unique_rotations = []
    seen_rotations = set()
    
    for rotation in rotations:
        # Create a tuple to represent the rotation
        normalized = tuple(rotation)
        if normalized not in seen_rotations:
            unique_rotations.append(rotation)
            seen_rotations.add(normalized)
    
    return unique_rotations

# Place modules in a line
def place_modules_line(rotations):
    module = get_existing_module()
    if not module:
        return

    spacing = 5  # Spacing between each module

    for i, (x_angle, y_angle, z_angle) in enumerate(rotations):
        module_instance = rs.CopyObject(module)
        if not module_instance:
            continue
        
        x = i * spacing
        y = 0
        z = 0

        rs.MoveObject(module_instance, (x, y, z))
        centroid = rs.SurfaceAreaCentroid(module_instance)[0]
        rs.RotateObject(module_instance, centroid, x_angle, axis=(1,0,0))
        rs.RotateObject(module_instance, centroid, y_angle, axis=(0,1,0))
        rs.RotateObject(module_instance, centroid, z_angle, axis=(0,0,1))

# Get existing module from Rhino
def get_existing_module():
    return rs.GetObject("Select the existing module")

# Main code execution
num_random_rotations = 49  # Number of random rotations to select
random_rotations = get_random_rotations(num_random_rotations)

# Remove duplicate rotations
unique_rotations = get_unique_rotations(random_rotations)

# Place unique modules in a line
place_modules_line(unique_rotations)
