# fc_forall_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def test1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        forall6_worked = True
        with engine.lookup('family', 'child_of', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            forall6_worked = False
            if context.lookup_data('mother') == context.lookup_data('mother2'):
              forall6_worked = True
            if not forall6_worked: break
        if forall6_worked:
          forall10_worked = True
          with engine.lookup('family', 'child_of', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              forall10_worked = False
              if context.lookup_data('father') == context.lookup_data('father2'):
                forall10_worked = True
              if not forall10_worked: break
          if forall10_worked:
            print(context.lookup_data('child'), "has no step brothers or sisters")
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_forall')
  
  fc_rule.fc_rule('test1', This_rule_base, test1,
    (('family', 'child_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'child_of',
      (contexts.anonymous('_'),
       contexts.variable('father'),
       contexts.variable('mother2'),),
      True),
     ('family', 'child_of',
      (contexts.anonymous('_'),
       contexts.variable('father2'),
       contexts.variable('mother'),),
      True),),
    ())


Krb_filename = '../fc_forall.krb'
Krb_lineno_map = (
    ((12, 16), (5, 5)),
    ((18, 21), (7, 7)),
    ((23, 23), (9, 9)),
    ((28, 31), (11, 11)),
    ((33, 33), (13, 13)),
    ((37, 37), (15, 15)),
)
