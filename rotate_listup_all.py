import rhinoscriptsyntax as rs
import itertools

y_angle = [0, 90, 180, 270]
x_angle = [0, 45, 90, 135, 225, 270, 315]

def generate_rotations():
    return list(itertools.product(y_angle, x_angle))

def get_unique_rotations(rotations):
    unique_rotations = []
    seen_rotations = set()
    
    for rotation in rotations:
        normalized = tuple(rotation)
        if normalized not in seen_rotations:
            unique_rotations.append(rotation)
            seen_rotations.add(normalized)
    return unique_rotations

def place_modules_grid(rotations, grid_size):
    module = get_existing_module()
    if not module:
        return
    
    spacing = 5

    for i, (y_angle, x_angle) in enumerate(rotations):
        module_instance = rs.CopyObject(module)
        if not module_instance:
            continue
        
        row = i // grid_size
        col = i % grid_size
        x = col * spacing
        y = row * spacing
        z = 0

        rs.MoveObject(module_instance, (x, y, z))
        centroid = rs.SurfaceAreaCentroid(module_instance)[0]
        rs.RotateObject(module_instance, centroid, y_angle, axis=(0,1,0))
        rs.RotateObject(module_instance, centroid, x_angle, axis=(1,0,0))

def get_existing_module():
    return rs.GetObject("Select the existing module")

rotations = generate_rotations()
unique_rotations = get_unique_rotations(rotations)

grid_size = int(len(unique_rotations) ** 0.5) + 1

place_modules_grid(unique_rotations, grid_size)