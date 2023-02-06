from stl import mesh

class HalfEdge:
    def __init__(self, start, end, twin=None, next=None):
        self.start = start
        self.end = end
        self.twin = twin
        self.next = next

def parse_stl(filename):
    # Load the STL file into a numpy array
    stl_mesh = mesh.Mesh.from_file(filename)
    # Get the number of faces
    num_faces = stl_mesh.vectors.shape[0]
    # Get the vertices of each face
    vertices = stl_mesh.vectors
    # Create a list to store the half-edges
    halfedges = []
    # Iterate over the faces
    for i in range(num_faces):
        face = vertices[i]
        # Get the start and end vertices of the first half-edge
        start, end = face[0], face[1]
        # Create the first half-edge
        halfedge = HalfEdge(start, end)
        # Set the next half-edge to be the second half-edge
        halfedge.next = HalfEdge(end, face[2], next=halfedge)
        # Set the twin half-edge to be the third half-edge
        halfedge.next.next = HalfEdge(face[2], start, twin=halfedge)
        # Add the first half-edge to the list
        halfedges.append(halfedge)
    return halfedges

if __name__ == '__main__':
    # Example usage
    halfedges = parse_stl('teapot.stl')
    print('Half-edges:')
    count=0
    for halfedge in halfedges:
        print(halfedge.start, halfedge.end)
        count+=1
    print (f"Number of halfedges: {count}")

    '''
OUTPUT:
[96.1704 64.9689 27.5907] [90.5278 64.9689 30.6195]
[90.7468 64.     31.1343] [96.4843 64.     28.0546]
...
...
[84.2628 64.9689 32.528 ] [77.5    64.9689 33.1918]
[77.5    64.     33.7499] [84.3765 64.     33.0749]
Number of halfedges: 2016
'''
