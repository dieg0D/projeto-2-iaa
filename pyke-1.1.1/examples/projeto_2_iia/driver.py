# driver.py
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def fc_test():
    consulta()
    engine.reset()
    try:
        engine.activate('fc_diagnostico')
    except:
        krb_traceback.print_exc()
        sys.exit(1)


def consulta():
    print("Seja bem vindo ao sistema especialista em doenças que vem do Aedes, responda as perguntas e diremos se você tem dengue, chikungunya ou zika.\n")
    p1 = input("Quantos graus de febre você teve?\n")
    p2 = input("Quantos dias durou a febre?\n")
    p3 = input("A partir de que dia surgiram manchas na pele?\n")
    p4 = input("De 1 a 3 qual a frequência da dor muscular que você está sentindo?\n")
    p5 = input("De 1 a 3 qual a frequência da dor nas articulações que você está sentindo?\n")
    p6 = input("Você considera essa dor: leve, moderada ou intensa ? \n")
    p7 = input("Você está com algum edema nas articulações? (sim/nao) \n")
    p8 = input("Qual a intensidade do edema nas articulações? leve, moderada ou intensa \n")
    p9 = input("Você teve conjuntivite ? (sim/nao) \n")
    p10 = input("De 1 a 3 qual a frequência de dor de cabeça?\n")
    p11 = input("Você considera a coceira: leve, moderada ou intensa ? \n")
    p12 = input("Você considera a Hipertrofia ganglionar: leve, moderada ou intensa ?? \n")
    p13 = input("Você considera a discrasia hemorrágica: leve, moderada ou intensa ? \n")
    p14 = input("Você teve acometimento neurológico ? (sim/nao) \n")

    arquivo = open('sintoma.kfb', 'w')
    arquivo.write('sintoma(%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)' % (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14))
    arquivo.close()