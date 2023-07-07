from openmm import XmlSerializer, LangevinMiddleIntegrator
from openmm.app import Simulation, PDBFile, AmberPrmtopFile, AmberInpcrdFile
from openmm.app import HBonds, NoCutoff, HCT
from openmm.unit import kelvin, picosecond
import os

# Load the Amber files
prmtop = AmberPrmtopFile('common_files/chignolin.prmtop')
inpcrd = AmberInpcrdFile('bstates/bstate.rst')

# Create the OpenMM System
system = prmtop.createSystem(nonbondedMethod=NoCutoff, constraints=HBonds, implicitSolvent=HCT)

# Create the OpenMM Simulation with the positions and velocities
integrator = LangevinMiddleIntegrator(275*kelvin,5/picosecond,.002*picosecond)
simulation = Simulation(prmtop.topology,system,integrator)
simulation.context.setPositions(inpcrd.positions)
simulation.context.setVelocities(inpcrd.velocities)

# Get the current state with positions and velocities
state = simulation.context.getState(getPositions=True, getVelocities=True)

# Serialize the State to XML
state_serialized = XmlSerializer.serialize(state)

# Save the serialized State to a file
with open('bstates/bstate.xml', 'w') as f:
    f.write(state_serialized)

