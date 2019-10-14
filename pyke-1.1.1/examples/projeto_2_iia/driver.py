# driver.py


import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def fc_test():
    consulta()
    engine.reset()
    try:
        engine.activate('fc_forall')
    except:
        krb_traceback.print_exc()
        sys.exit(1)


def consulta():
    print("Seja bem vindo ao sistema especialista em doenças que vem do aedes , responda as perguntas e diremos se você tem dengue, chikungunya ou zika.")
    num = input("Febre:")
    print(num)
    arquivo = open('sintoma.kfb', 'w')
    arquivo.write('nova linha')
    arquivo.close()