import mdtraj as md
import numpy as np
import os

def compute_rmsd(traj, ref):
    ca_indices = traj.topology.select('name CA')
    rmsd = md.rmsd(traj, ref, atom_indices=ca_indices)
    return rmsd

if __name__ == "__main__":
    from sys import argv
    outfile = argv[1]
    trajfile = argv[2]
    reffile = os.path.join(os.environ['WORK_SIM_ROOT'],"common_files","reference_chignolin.pdb")
    traj = md.load(trajfile)
    ref = md.load(reffile)
    rmsds = compute_rmsd(traj, ref)
    np.savetxt(outfile, rmsds)



