from openmm import app, XmlSerializer
from openmm.unit import kelvin, bar, nanometer
from openmmforcefields.generators import SystemGenerator
from openff.toolkit.topology import Molecule

# Load the PDB file
pdb = app.PDBFile('chignolin.pdb')

# Define the forcefield parameters
forcefield_kwargs = {'constraints': app.HBonds,
                     'removeCMMotion': False}

# Create the GBSAOBCForce
gb_force = openmm.GBSAOBCForce()
gb_force.setNonbondedMethod(openmm.GBSAOBCForce.HCT)
gb_force.setSolventDielectric(1.0)
gb_force.setSoluteDielectric(1.0)

# Create the SystemGenerator
system_generator = SystemGenerator(forcefields=['amber14/protein.ff14SB.xml', 'amber14/tip3p.xml'],
                                   forcefield_kwargs=forcefield_kwargs)

# Create the OpenMM System
system = system_generator.create_system(pdb.topology)

# Add the GBSAOBCForce to the System
system.addForce(gb_force)

# Serialize the System to XML
omm_sys_serialized = XmlSerializer.serialize(system)

# Save the serialized System to a file
with open('system.xml', 'wt') as f:
    f.write(omm_sys_serialized)

