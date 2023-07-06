from openmm import app, XmlSerializer
from openmm.unit import kelvin
import os

# Load the Amber files
prmtop = app.AmberPrmtopFile('common_files/chignolin.prmtop')

# Create the OpenMM System
system = prmtop.createSystem(nonbondedMethod=app.NoCutoff, constraints=app.HBonds, implicitSolvent=app.HCT)

# Load the PDB file
pdb = app.PDBFile('bstate_chignolin.pdb')

# Create the OpenMM Simulation with the positions
integrator = LangevinMiddleIntegrator(275*kelvin,5/picosecond,.002*picoseconds)
simulation = Simulation(pdb.topology,system,integrator)
simulation.context.setPositions(pdb.positions)

# Serialize the System to XML
omm_sys_serialized = XmlSerializer.serialize(system)

# Save the serialized System to a file in the bstates directory
with open('bstates/bstate.xml', 'w') as f:
    f.write(omm_sys_serialized)

