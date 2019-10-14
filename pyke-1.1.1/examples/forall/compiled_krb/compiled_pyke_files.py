# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'fc_forall.krb'):
           [1571056214.9811122, 'fc_forall_fc.py'],
         ('', '', 'bc_forall.krb'):
           [1571056214.987134, 'bc_forall_bc.py'],
         ('', '', 'family.kfb'):
           [1571056214.9914553, 'family.fbc'],
        },
        compiler_version)

