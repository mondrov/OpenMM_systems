import mdtraj as md
from sys import argv

def compute_rmsd(traj, ref=None):
    if ref is None:
        ref = traj[0]
    return md.rmsd(traj, ref)

if __name__ == "__main__":
    outfile = argv[1]
    trajfile = argv[2]
    topfile = argv[3] if len(argv) > 3 else None

    if topfile:
        traj = md.load(trajfile, top=topfile)
    else:
        traj = md.load(trajfile)

    rmsds = compute_rmsd(traj)
    np.savetxt(outfile, rmsds)
