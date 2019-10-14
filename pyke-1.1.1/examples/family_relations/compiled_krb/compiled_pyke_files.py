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
         ('', '', 'bc2_example.krb'):
           [1571077046.6308157, 'bc2_example_bc.py'],
         ('', '', 'bc_example.krb'):
           [1571077046.664321, 'bc_example_bc.py'],
         ('', '', 'family.kfb'):
           [1571077046.7916932, 'family.fbc'],
         ('', '', 'example.krb'):
           [1571077046.856676, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'fc_example.krb'):
           [1571077046.8895907, 'fc_example_fc.py'],
        },
        compiler_version)

