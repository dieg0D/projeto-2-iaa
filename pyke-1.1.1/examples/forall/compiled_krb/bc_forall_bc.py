# bc_forall_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def test1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'child_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_forall.test1: got unexpected plan from when clause 1"
            forall7_worked = True
            with engine.prove('family', 'child_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_forall.test1: got unexpected plan from when clause 2"
                forall7_worked = False
                if context.lookup_data('mother') == context.lookup_data('mother2'):
                  forall7_worked = True
                if not forall7_worked: break
            if forall7_worked:
              forall11_worked = True
              with engine.prove('family', 'child_of', context,
                                (rule.pattern(3),
                                 rule.pattern(5),
                                 rule.pattern(2),)) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "bc_forall.test1: got unexpected plan from when clause 4"
                  forall11_worked = False
                  if context.lookup_data('father') == context.lookup_data('father2'):
                    forall11_worked = True
                  if not forall11_worked: break
              if forall11_worked:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_forall')
  
  bc_rule.bc_rule('test1', This_rule_base, 'no_step_siblings',
                  test1, None,
                  (contexts.variable('child'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.anonymous('_'),
                   contexts.variable('mother2'),
                   contexts.variable('father2'),))


Krb_filename = '../bc_forall.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 27), (6, 6)),
    ((29, 36), (8, 8)),
    ((38, 38), (10, 10)),
    ((43, 50), (12, 12)),
    ((52, 52), (14, 14)),
)
