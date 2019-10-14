# fc_forall_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def dengue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('diagnostico', 'diagnostico', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        forall6_worked = True
        with engine.lookup('sintoma', 'sintoma', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            forall6_worked = False
            if context.lookup_data('coceira') == context.lookup_data('c'):
              forall6_worked = True
            if not forall6_worked: break
        if forall6_worked:
          print(context.lookup_data('coceira'), "tá dengoso")
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_forall')
  
  fc_rule.fc_rule('dengue', This_rule_base, dengue,
    (('diagnostico', 'diagnostico',
      (contexts.variable('coceira'),
       contexts.variable('h'),),
      False),
     ('sintoma', 'sintoma',
      (contexts.variable('c'),
       contexts.variable('h'),),
      True),),
    ())


Krb_filename = '../fc_forall.krb'
Krb_lineno_map = (
    ((12, 16), (5, 5)),
    ((18, 21), (7, 7)),
    ((23, 23), (9, 9)),
    ((27, 27), (11, 11)),
)
