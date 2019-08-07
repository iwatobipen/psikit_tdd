# IPython log file

get_ipython().run_line_magic('logstart', 'fsapthelp.py')
from rdkit import Cehem
from rdkit import Chem
from rdkit.Chem import rdMMPA
mol = Chem.MolFromSmiles('c1ccccc1OC')
rdMMPA.FragmentMol(mol)
frag  = rdMMPA.FragmentMol(mol)
for f in frag:
    print(f)
    
rdMMPA.FragmentMol?    
get_ipython().run_line_magic('pinfo', 'rdMMPA.FragmentMol')
frag  = rdMMPA.FragmentMol(mol, maxCuts=1)
frag
for f in frag:
    print(Chem.MolToSmiles(f[1]))
    
get_ipython().run_line_magic('pinfo', 'rdMMPA.FragmentMol')
get_ipython().run_line_magic('clear', '')
exit()
