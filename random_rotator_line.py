import rhinoscriptsyntax as rs
import random
import itertools

# List of angles
angles = [0, 45, 90, 135, 180, 225, 270, 315]

# Generate rotations
def generate_rotations():
    return list(itertools.product(angles, repeat=3))

# Get random rotations
def get_random_rotations(num_rotations):
    all_rotations = generate_rotations()
    return random.sample(all_rotations, num_rotations)

# Array curve (Option A)
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

# Get rid of duplications
def get_unique_rotations(rotations):
    unique_rotations = []
    seen_rotations = set()
    
    for rotation in rotations:
        normalized = tuple(rotation)  # Normalization may be necessary in some cases
        if normalized not in seen_rotations:
            unique_rotations.append(rotation)
            seen_rotations.add(normalized)
    
    return unique_rotations

# Get existing module
def get_existing_module():
    return rs.GetObject("Select the existing module")

# num_random_rotations = number
num_random_rotations = 49
random_rotations = get_random_rotations(num_random_rotations)

# Square grid
place_modules_grid(random_rotations, grid_size=7)

# Delete duplications
unique_rotations = get_unique_rotations(random_rotations)
