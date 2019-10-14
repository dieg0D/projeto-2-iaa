# example_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def son_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def daughter_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brothers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('brother1') != context.lookup_data('brother2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sisters(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('sister1') != context.lookup_data('sister2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brother_and_sister(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'siblings',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            engine.assert_('family', 'siblings',
                           (rule.pattern(1).as_data(context),
                            rule.pattern(0).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def facts_for_bc_rules(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    engine.assert_('family', 'as_au',
                   (rule.pattern(0).as_data(context),
                    rule.pattern(1).as_data(context),)),
    engine.assert_('family', 'as_au',
                   (rule.pattern(2).as_data(context),
                    rule.pattern(3).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(4).as_data(context),
                    rule.pattern(5).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(6).as_data(context),
                    rule.pattern(7).as_data(context),)),
    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('example')
  
  fc_rule.fc_rule('son_of', This_rule_base, son_of,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('son'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('daughter_of', This_rule_base, daughter_of,
    (('family', 'daughter_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('daughter'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('brothers', This_rule_base, brothers,
    (('family', 'son_of',
      (contexts.variable('brother1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother1'),
     contexts.variable('brother2'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('sisters', This_rule_base, sisters,
    (('family', 'daughter_of',
      (contexts.variable('sister1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('sister1'),
     contexts.variable('sister2'),
     pattern.pattern_literal('sister'),))
  
  fc_rule.fc_rule('brother_and_sister', This_rule_base, brother_and_sister,
    (('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother'),
     contexts.variable('sister'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('facts_for_bc_rules', This_rule_base, facts_for_bc_rules,
    (),
    (pattern.pattern_literal('brother'),
     pattern.pattern_literal('uncle'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('aunt'),
     pattern.pattern_literal('son'),
     pattern.pattern_literal('nephew'),
     pattern.pattern_literal('daughter'),
     pattern.pattern_literal('niece'),))


Krb_filename = '../example.krb'
Krb_lineno_map = (
    ((12, 16), (33, 33)),
    ((17, 21), (35, 35)),
    ((22, 26), (36, 36)),
    ((35, 39), (40, 40)),
    ((40, 44), (42, 42)),
    ((45, 49), (43, 43)),
    ((58, 62), (48, 48)),
    ((63, 67), (49, 49)),
    ((68, 68), (50, 50)),
    ((69, 73), (52, 52)),
    ((82, 86), (56, 56)),
    ((87, 91), (57, 57)),
    ((92, 92), (58, 58)),
    ((93, 97), (60, 60)),
    ((106, 110), (64, 64)),
    ((111, 115), (65, 65)),
    ((116, 120), (67, 67)),
    ((121, 125), (68, 68)),
    ((134, 136), (78, 78)),
    ((137, 139), (79, 79)),
    ((140, 142), (80, 80)),
    ((143, 145), (81, 81)),
)
