import numpy as np
from scipy.spatial import Delaunay

# Generate random 3D points
points = np.random.rand(10, 3)

# Perform 3D Delaunay triangulation
triangulation = Delaunay(points)

# Write VTK file
with open('delaunay.vtk', 'w') as vtk_file:
    vtk_file.write("# vtk DataFile Version 3.0\n")
    vtk_file.write("Delaunay Triangulation\n")
    vtk_file.write("ASCII\n")
    vtk_file.write("DATASET POLYDATA\n")
    vtk_file.write(f"POINTS {len(points)} float\n")
    
    for point in points:
        vtk_file.write(f"{point[0]} {point[1]} {point[2]}\n")
    
    # Write Delaunay triangulation edges as VTK lines
    edges = []
    for simplex in triangulation.simplices:
        for i in range(len(simplex)):
            for j in range(i+1, len(simplex)):
                edges.append([simplex[i], simplex[j]])
    
    vtk_file.write(f"LINES {len(edges)} {len(edges) * 3}\n")
    
    for line in edges:
        vtk_file.write(f"2 {line[0]} {line[1]}\n")
