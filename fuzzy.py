import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# Variáveis de entrada
temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
umidade = ctrl.Antecedent(np.arange(0, 101, 1), 'umidade')
velocidade_ventilador = ctrl.Consequent(np.arange(0, 101, 1),
'velocidade_ventilador')
# Funções de pertinência
temperatura['frio'] = fuzz.trimf(temperatura.universe, [0, 0, 20])
temperatura['médio'] = fuzz.trimf(temperatura.universe, [10, 25, 35])
temperatura['quente'] = fuzz.trimf(temperatura.universe, [30, 40, 40])
umidade['seca'] = fuzz.trimf(umidade.universe, [0, 0, 50])
umidade['úmida'] = fuzz.trimf(umidade.universe, [25, 75, 100])

velocidade_ventilador['baixa'] = fuzz.trimf(velocidade_ventilador.universe, [0, 0, 50])
velocidade_ventilador['alta'] = fuzz.trimf(velocidade_ventilador.universe, [50, 100, 100])
# Regras fuzzy
regra1 = ctrl.Rule(temperatura['frio'] | umidade['seca'],
velocidade_ventilador['baixa'])
regra2 = ctrl.Rule(temperatura['médio'], velocidade_ventilador['alta'])
regra3 = ctrl.Rule(temperatura['quente'] | umidade['úmida'],
velocidade_ventilador['alta'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema_controle)

simulador.input['temperatura'] = 30
simulador.input['umidade'] = 80
# Computação
simulador.compute()
# Saída
print(simulador.output['velocidade_ventilador'])