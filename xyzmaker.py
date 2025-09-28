from ase.io import read, write

# Define the list of CIF files to convert
cif_files = ['1569089.cif', '1000017.cif', '1000003.cif']

for cif_file in cif_files:
    # Read the CIF file using ASE
    atoms = read(cif_file)

    # Define the output XYZ file name
    xyz_file = cif_file.replace('.cif', '.xyz')

    # Write the atoms to the output XYZ file using ASE
    write(xyz_file, atoms, format='xyz')