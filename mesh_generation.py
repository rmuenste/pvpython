import vtk

# Define the number of cells in each direction
nx, ny, nz = 4, 4, 4

# Define the cell dimensions
dx, dy, dz = 9/nx, 9/ny, 9/nz

# Create the points for the mesh
points = vtk.vtkPoints()
for k in range(nz + 1):
    for j in range(ny + 1):
        for i in range(nx + 1):
            x = i * dx
            y = j * dy
            z = k * dz
            points.InsertNextPoint(x, y, z)

# Create a cell array for the mesh
cells = vtk.vtkCellArray()
for k in range(nz):
    for j in range(ny):
        for i in range(nx):
            cell = vtk.vtkHexahedron()
            cell.GetPointIds().SetId(0, i + j * (nx + 1) + k * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(1, i + 1 + j * (nx + 1) + k * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(2, i + 1 + (j + 1) * (nx + 1) + k * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(3, i + (j + 1) * (nx + 1) + k * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(4, i + j * (nx + 1) + (k + 1) * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(5, i + 1 + j * (nx + 1) + (k + 1) * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(6, i + 1 + (j + 1) * (nx + 1) + (k + 1) * (nx + 1) * (ny + 1))
            cell.GetPointIds().SetId(7, i + (j + 1) * (nx + 1) + (k + 1) * (nx + 1) * (ny + 1))
            cells.InsertNextCell(cell)

# Create an unstructured grid to store the mesh
mesh = vtk.vtkUnstructuredGrid()
mesh.SetPoints(points)
mesh.SetCells(vtk.VTK_HEXAHEDRON, cells)

# Write the mesh to a VTK file
writer = vtk.vtkUnstructuredGridWriter()
writer.SetFileName("mesh.vtk")
writer.SetInputData(mesh)
writer.Write()