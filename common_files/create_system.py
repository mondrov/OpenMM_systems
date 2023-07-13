from openmm import app, XmlSerializer
from openmm.unit import kelvin

# Load the Amber file
prmtop = app.AmberPrmtopFile('ntl9.prmtop')

# Create the OpenMM System
system = prmtop.createSystem(nonbondedMethod=app.NoCutoff, constraints=app.HBonds, implicitSolvent=app.HCT)

# Serialize the System to XML
omm_sys_serialized = XmlSerializer.serialize(system)

# Save the serialized System to a file
with open('system.xml', 'wt') as f:
    f.write(omm_sys_serialized)
