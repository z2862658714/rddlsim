from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

model = BayesianModel([('State_0', 'Observed_0'), 
                       ('State_0', 'State_1'), 
                       ('State_1', 'Observed_1'),
                       ('State_1', 'State_2'),
                       ('State_2', 'Observed_2')])

state_0_cpd = TabularCPD('State_0', 2, [[1.0,0.0]])
observ_0_cpd = TabularCPD('Observed_0', 2, [[0.5,0.0],[0.5,1.0]],
                          evidence=['State_0'], evidence_card=[2])

state_1_cpd = TabularCPD('State_1', 2, [[0.8,0.0],[0.2,1.0]],
                         evidence=['State_0'], evidence_card=[2])
observ_1_cpd = TabularCPD('Observed_1', 2, [[0.5,0.0],[0.5,1.0]],
                          evidence=['State_1'], evidence_card=[2])

state_2_cpd = TabularCPD('State_2', 2, [[0.8,0.0],[0.2,1.0]],
                         evidence=['State_1'], evidence_card=[2])
observ_2_cpd = TabularCPD('Observed_2', 2, [[0.5,0.0],[0.5,1.0]],
                          evidence=['State_2'], evidence_card=[2])

model.add_cpds(state_0_cpd, observ_0_cpd, state_1_cpd, observ_1_cpd, state_2_cpd, observ_2_cpd)
