import sys, os;
import numpy as np;
from pgmpy.inference import VariableElimination;

dir = os.path.abspath(os.path.dirname(__file__));
filename = dir + '/valve_inst.py';
exec(open(filename, 'r', -1, 'utf-8').read());

inference = VariableElimination(valve_domain_model);
q1 = inference.query(variables = ['state_broken_2']);
q2 = inference.query(variables = ['state_broken_2'], evidence = {'prev_state_observed_broken_3' : 1});
q3 = inference.query(variables = ['state_broken_2'], evidence = {'prev_state_observed_broken_1' : 1, 'prev_state_observed_broken_2' : 0, 'prev_state_observed_broken_3' : 1});
q4 = inference.query(variables = ['state_broken_2'], evidence = {'prev_state_observed_broken_1' : 1, 'prev_state_observed_broken_2' : 1, 'prev_state_observed_broken_3' : 1});
q5 = inference.query(variables = ['prev_state_observed_broken_3'], evidence = {'state_broken_1' : 0});

print("MIE1516 Structured Inference and Learning: Warmup Assignment\n");
print("_0 means normal state/observation, _1 means broken state/observation\n");
print("1. Given no evidence, what is the probability that the valve state is broken at the third time step?");
print(q1['state_broken_2']);
print("2. Given the evidence observed_broken for the sensor at the second time step, what is the probability that the valve state is broken at the third time step?");
print(q2['state_broken_2']);
print("3. Given the sensor observation sequence (observed_broken, observed_normal, observed_broken) as evidence, what is the probability that the valve state is broken at the third time step?");
print(q3['state_broken_2']);
print("4. Given the sensor observation sequence (observed_broken, observed_broken, observed_broken) as evidence, what is the probability that the valve state is broken at the third time step?");
print(q4['state_broken_2']);
print("5. Given the evidence that the valve state at the second time step is normal, what is the probability of observing sensor value observed_normal at the third time step?");
print(q5['prev_state_observed_broken_3']);
