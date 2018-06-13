# Automatically produced by RDDL2Pgmpy
# Pgmpy Bayesian Model for 'ambulance_mdp.ambulance_inst_mdp__0'
# variable_0 => variable = false; variable_1 => variable = true

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD;

ambulance_mdp_model = BayesianModel();

ambulance_mdp_model.add_nodes_from(['person_in_ambulance__a0_0',
                                    'person_in_ambulance__a1_0',
                                    'ambulance_at_node__a0_n0_0',
                                    'ambulance_at_node__a0_n1_0',
                                    'ambulance_at_node__a0_n2_0',
                                    'ambulance_at_node__a0_n3_0',
                                    'ambulance_at_node__a0_n4_0',
                                    'ambulance_at_node__a0_n5_0',
                                    'ambulance_at_node__a0_n6_0',
                                    'ambulance_at_node__a0_n7_0',
                                    'ambulance_at_node__a0_n8_0',
                                    'ambulance_at_node__a1_n0_0',
                                    'ambulance_at_node__a1_n1_0',
                                    'ambulance_at_node__a1_n2_0',
                                    'ambulance_at_node__a1_n3_0',
                                    'ambulance_at_node__a1_n4_0',
                                    'ambulance_at_node__a1_n5_0',
                                    'ambulance_at_node__a1_n6_0',
                                    'ambulance_at_node__a1_n7_0',
                                    'ambulance_at_node__a1_n8_0',
                                    'person_waiting_service__n0_0',
                                    'person_waiting_service__n1_0',
                                    'person_waiting_service__n2_0',
                                    'person_waiting_service__n3_0',
                                    'person_waiting_service__n4_0',
                                    'person_waiting_service__n5_0',
                                    'person_waiting_service__n6_0',
                                    'person_waiting_service__n7_0',
                                    'person_waiting_service__n8_0',
                                    'person_in_ambulance__a0_1',
                                    'person_in_ambulance__a1_1',
                                    'ambulance_at_node__a0_n0_1',
                                    'ambulance_at_node__a0_n1_1',
                                    'ambulance_at_node__a0_n2_1',
                                    'ambulance_at_node__a0_n3_1',
                                    'ambulance_at_node__a0_n4_1',
                                    'ambulance_at_node__a0_n5_1',
                                    'ambulance_at_node__a0_n6_1',
                                    'ambulance_at_node__a0_n7_1',
                                    'ambulance_at_node__a0_n8_1',
                                    'ambulance_at_node__a1_n0_1',
                                    'ambulance_at_node__a1_n1_1',
                                    'ambulance_at_node__a1_n2_1',
                                    'ambulance_at_node__a1_n3_1',
                                    'ambulance_at_node__a1_n4_1',
                                    'ambulance_at_node__a1_n5_1',
                                    'ambulance_at_node__a1_n6_1',
                                    'ambulance_at_node__a1_n7_1',
                                    'ambulance_at_node__a1_n8_1',
                                    'person_waiting_service__n0_1',
                                    'person_waiting_service__n1_1',
                                    'person_waiting_service__n2_1',
                                    'person_waiting_service__n3_1',
                                    'person_waiting_service__n4_1',
                                    'person_waiting_service__n5_1',
                                    'person_waiting_service__n6_1',
                                    'person_waiting_service__n7_1',
                                    'person_waiting_service__n8_1',
                                    'person_in_ambulance__a0_2',
                                    'person_in_ambulance__a1_2',
                                    'ambulance_at_node__a0_n0_2',
                                    'ambulance_at_node__a0_n1_2',
                                    'ambulance_at_node__a0_n2_2',
                                    'ambulance_at_node__a0_n3_2',
                                    'ambulance_at_node__a0_n4_2',
                                    'ambulance_at_node__a0_n5_2',
                                    'ambulance_at_node__a0_n6_2',
                                    'ambulance_at_node__a0_n7_2',
                                    'ambulance_at_node__a0_n8_2',
                                    'ambulance_at_node__a1_n0_2',
                                    'ambulance_at_node__a1_n1_2',
                                    'ambulance_at_node__a1_n2_2',
                                    'ambulance_at_node__a1_n3_2',
                                    'ambulance_at_node__a1_n4_2',
                                    'ambulance_at_node__a1_n5_2',
                                    'ambulance_at_node__a1_n6_2',
                                    'ambulance_at_node__a1_n7_2',
                                    'ambulance_at_node__a1_n8_2',
                                    'person_waiting_service__n0_2',
                                    'person_waiting_service__n1_2',
                                    'person_waiting_service__n2_2',
                                    'person_waiting_service__n3_2',
                                    'person_waiting_service__n4_2',
                                    'person_waiting_service__n5_2',
                                    'person_waiting_service__n6_2',
                                    'person_waiting_service__n7_2',
                                    'person_waiting_service__n8_2',
                                    'person_in_ambulance__a0_3',
                                    'person_in_ambulance__a1_3',
                                    'ambulance_at_node__a0_n0_3',
                                    'ambulance_at_node__a0_n1_3',
                                    'ambulance_at_node__a0_n2_3',
                                    'ambulance_at_node__a0_n3_3',
                                    'ambulance_at_node__a0_n4_3',
                                    'ambulance_at_node__a0_n5_3',
                                    'ambulance_at_node__a0_n6_3',
                                    'ambulance_at_node__a0_n7_3',
                                    'ambulance_at_node__a0_n8_3',
                                    'ambulance_at_node__a1_n0_3',
                                    'ambulance_at_node__a1_n1_3',
                                    'ambulance_at_node__a1_n2_3',
                                    'ambulance_at_node__a1_n3_3',
                                    'ambulance_at_node__a1_n4_3',
                                    'ambulance_at_node__a1_n5_3',
                                    'ambulance_at_node__a1_n6_3',
                                    'ambulance_at_node__a1_n7_3',
                                    'ambulance_at_node__a1_n8_3',
                                    'person_waiting_service__n0_3',
                                    'person_waiting_service__n1_3',
                                    'person_waiting_service__n2_3',
                                    'person_waiting_service__n3_3',
                                    'person_waiting_service__n4_3',
                                    'person_waiting_service__n5_3',
                                    'person_waiting_service__n6_3',
                                    'person_waiting_service__n7_3',
                                    'person_waiting_service__n8_3',
                                    'person_in_ambulance__a0_4',
                                    'person_in_ambulance__a1_4',
                                    'ambulance_at_node__a0_n0_4',
                                    'ambulance_at_node__a0_n1_4',
                                    'ambulance_at_node__a0_n2_4',
                                    'ambulance_at_node__a0_n3_4',
                                    'ambulance_at_node__a0_n4_4',
                                    'ambulance_at_node__a0_n5_4',
                                    'ambulance_at_node__a0_n6_4',
                                    'ambulance_at_node__a0_n7_4',
                                    'ambulance_at_node__a0_n8_4',
                                    'ambulance_at_node__a1_n0_4',
                                    'ambulance_at_node__a1_n1_4',
                                    'ambulance_at_node__a1_n2_4',
                                    'ambulance_at_node__a1_n3_4',
                                    'ambulance_at_node__a1_n4_4',
                                    'ambulance_at_node__a1_n5_4',
                                    'ambulance_at_node__a1_n6_4',
                                    'ambulance_at_node__a1_n7_4',
                                    'ambulance_at_node__a1_n8_4',
                                    'person_waiting_service__n0_4',
                                    'person_waiting_service__n1_4',
                                    'person_waiting_service__n2_4',
                                    'person_waiting_service__n3_4',
                                    'person_waiting_service__n4_4',
                                    'person_waiting_service__n5_4',
                                    'person_waiting_service__n6_4',
                                    'person_waiting_service__n7_4',
                                    'person_waiting_service__n8_4',
                                    'person_in_ambulance__a0_5',
                                    'person_in_ambulance__a1_5',
                                    'ambulance_at_node__a0_n0_5',
                                    'ambulance_at_node__a0_n1_5',
                                    'ambulance_at_node__a0_n2_5',
                                    'ambulance_at_node__a0_n3_5',
                                    'ambulance_at_node__a0_n4_5',
                                    'ambulance_at_node__a0_n5_5',
                                    'ambulance_at_node__a0_n6_5',
                                    'ambulance_at_node__a0_n7_5',
                                    'ambulance_at_node__a0_n8_5',
                                    'ambulance_at_node__a1_n0_5',
                                    'ambulance_at_node__a1_n1_5',
                                    'ambulance_at_node__a1_n2_5',
                                    'ambulance_at_node__a1_n3_5',
                                    'ambulance_at_node__a1_n4_5',
                                    'ambulance_at_node__a1_n5_5',
                                    'ambulance_at_node__a1_n6_5',
                                    'ambulance_at_node__a1_n7_5',
                                    'ambulance_at_node__a1_n8_5',
                                    'person_waiting_service__n0_5',
                                    'person_waiting_service__n1_5',
                                    'person_waiting_service__n2_5',
                                    'person_waiting_service__n3_5',
                                    'person_waiting_service__n4_5',
                                    'person_waiting_service__n5_5',
                                    'person_waiting_service__n6_5',
                                    'person_waiting_service__n7_5',
                                    'person_waiting_service__n8_5',
                                    'person_in_ambulance__a0_6',
                                    'person_in_ambulance__a1_6',
                                    'ambulance_at_node__a0_n0_6',
                                    'ambulance_at_node__a0_n1_6',
                                    'ambulance_at_node__a0_n2_6',
                                    'ambulance_at_node__a0_n3_6',
                                    'ambulance_at_node__a0_n4_6',
                                    'ambulance_at_node__a0_n5_6',
                                    'ambulance_at_node__a0_n6_6',
                                    'ambulance_at_node__a0_n7_6',
                                    'ambulance_at_node__a0_n8_6',
                                    'ambulance_at_node__a1_n0_6',
                                    'ambulance_at_node__a1_n1_6',
                                    'ambulance_at_node__a1_n2_6',
                                    'ambulance_at_node__a1_n3_6',
                                    'ambulance_at_node__a1_n4_6',
                                    'ambulance_at_node__a1_n5_6',
                                    'ambulance_at_node__a1_n6_6',
                                    'ambulance_at_node__a1_n7_6',
                                    'ambulance_at_node__a1_n8_6',
                                    'person_waiting_service__n0_6',
                                    'person_waiting_service__n1_6',
                                    'person_waiting_service__n2_6',
                                    'person_waiting_service__n3_6',
                                    'person_waiting_service__n4_6',
                                    'person_waiting_service__n5_6',
                                    'person_waiting_service__n6_6',
                                    'person_waiting_service__n7_6',
                                    'person_waiting_service__n8_6',
                                    'person_in_ambulance__a0_7',
                                    'person_in_ambulance__a1_7',
                                    'ambulance_at_node__a0_n0_7',
                                    'ambulance_at_node__a0_n1_7',
                                    'ambulance_at_node__a0_n2_7',
                                    'ambulance_at_node__a0_n3_7',
                                    'ambulance_at_node__a0_n4_7',
                                    'ambulance_at_node__a0_n5_7',
                                    'ambulance_at_node__a0_n6_7',
                                    'ambulance_at_node__a0_n7_7',
                                    'ambulance_at_node__a0_n8_7',
                                    'ambulance_at_node__a1_n0_7',
                                    'ambulance_at_node__a1_n1_7',
                                    'ambulance_at_node__a1_n2_7',
                                    'ambulance_at_node__a1_n3_7',
                                    'ambulance_at_node__a1_n4_7',
                                    'ambulance_at_node__a1_n5_7',
                                    'ambulance_at_node__a1_n6_7',
                                    'ambulance_at_node__a1_n7_7',
                                    'ambulance_at_node__a1_n8_7',
                                    'person_waiting_service__n0_7',
                                    'person_waiting_service__n1_7',
                                    'person_waiting_service__n2_7',
                                    'person_waiting_service__n3_7',
                                    'person_waiting_service__n4_7',
                                    'person_waiting_service__n5_7',
                                    'person_waiting_service__n6_7',
                                    'person_waiting_service__n7_7',
                                    'person_waiting_service__n8_7',
                                    'person_in_ambulance__a0_8',
                                    'person_in_ambulance__a1_8',
                                    'ambulance_at_node__a0_n0_8',
                                    'ambulance_at_node__a0_n1_8',
                                    'ambulance_at_node__a0_n2_8',
                                    'ambulance_at_node__a0_n3_8',
                                    'ambulance_at_node__a0_n4_8',
                                    'ambulance_at_node__a0_n5_8',
                                    'ambulance_at_node__a0_n6_8',
                                    'ambulance_at_node__a0_n7_8',
                                    'ambulance_at_node__a0_n8_8',
                                    'ambulance_at_node__a1_n0_8',
                                    'ambulance_at_node__a1_n1_8',
                                    'ambulance_at_node__a1_n2_8',
                                    'ambulance_at_node__a1_n3_8',
                                    'ambulance_at_node__a1_n4_8',
                                    'ambulance_at_node__a1_n5_8',
                                    'ambulance_at_node__a1_n6_8',
                                    'ambulance_at_node__a1_n7_8',
                                    'ambulance_at_node__a1_n8_8',
                                    'person_waiting_service__n0_8',
                                    'person_waiting_service__n1_8',
                                    'person_waiting_service__n2_8',
                                    'person_waiting_service__n3_8',
                                    'person_waiting_service__n4_8',
                                    'person_waiting_service__n5_8',
                                    'person_waiting_service__n6_8',
                                    'person_waiting_service__n7_8',
                                    'person_waiting_service__n8_8',
                                    'person_in_ambulance__a0_9',
                                    'person_in_ambulance__a1_9',
                                    'ambulance_at_node__a0_n0_9',
                                    'ambulance_at_node__a0_n1_9',
                                    'ambulance_at_node__a0_n2_9',
                                    'ambulance_at_node__a0_n3_9',
                                    'ambulance_at_node__a0_n4_9',
                                    'ambulance_at_node__a0_n5_9',
                                    'ambulance_at_node__a0_n6_9',
                                    'ambulance_at_node__a0_n7_9',
                                    'ambulance_at_node__a0_n8_9',
                                    'ambulance_at_node__a1_n0_9',
                                    'ambulance_at_node__a1_n1_9',
                                    'ambulance_at_node__a1_n2_9',
                                    'ambulance_at_node__a1_n3_9',
                                    'ambulance_at_node__a1_n4_9',
                                    'ambulance_at_node__a1_n5_9',
                                    'ambulance_at_node__a1_n6_9',
                                    'ambulance_at_node__a1_n7_9',
                                    'ambulance_at_node__a1_n8_9',
                                    'person_waiting_service__n0_9',
                                    'person_waiting_service__n1_9',
                                    'person_waiting_service__n2_9',
                                    'person_waiting_service__n3_9',
                                    'person_waiting_service__n4_9',
                                    'person_waiting_service__n5_9',
                                    'person_waiting_service__n6_9',
                                    'person_waiting_service__n7_9',
                                    'person_waiting_service__n8_9',
                                    'person_in_ambulance__a0_10',
                                    'person_in_ambulance__a1_10',
                                    'ambulance_at_node__a0_n0_10',
                                    'ambulance_at_node__a0_n1_10',
                                    'ambulance_at_node__a0_n2_10',
                                    'ambulance_at_node__a0_n3_10',
                                    'ambulance_at_node__a0_n4_10',
                                    'ambulance_at_node__a0_n5_10',
                                    'ambulance_at_node__a0_n6_10',
                                    'ambulance_at_node__a0_n7_10',
                                    'ambulance_at_node__a0_n8_10',
                                    'ambulance_at_node__a1_n0_10',
                                    'ambulance_at_node__a1_n1_10',
                                    'ambulance_at_node__a1_n2_10',
                                    'ambulance_at_node__a1_n3_10',
                                    'ambulance_at_node__a1_n4_10',
                                    'ambulance_at_node__a1_n5_10',
                                    'ambulance_at_node__a1_n6_10',
                                    'ambulance_at_node__a1_n7_10',
                                    'ambulance_at_node__a1_n8_10',
                                    'person_waiting_service__n0_10',
                                    'person_waiting_service__n1_10',
                                    'person_waiting_service__n2_10',
                                    'person_waiting_service__n3_10',
                                    'person_waiting_service__n4_10',
                                    'person_waiting_service__n5_10',
                                    'person_waiting_service__n6_10',
                                    'person_waiting_service__n7_10',
                                    'person_waiting_service__n8_10',
                                    'person_in_ambulance__a0_11',
                                    'person_in_ambulance__a1_11',
                                    'ambulance_at_node__a0_n0_11',
                                    'ambulance_at_node__a0_n1_11',
                                    'ambulance_at_node__a0_n2_11',
                                    'ambulance_at_node__a0_n3_11',
                                    'ambulance_at_node__a0_n4_11',
                                    'ambulance_at_node__a0_n5_11',
                                    'ambulance_at_node__a0_n6_11',
                                    'ambulance_at_node__a0_n7_11',
                                    'ambulance_at_node__a0_n8_11',
                                    'ambulance_at_node__a1_n0_11',
                                    'ambulance_at_node__a1_n1_11',
                                    'ambulance_at_node__a1_n2_11',
                                    'ambulance_at_node__a1_n3_11',
                                    'ambulance_at_node__a1_n4_11',
                                    'ambulance_at_node__a1_n5_11',
                                    'ambulance_at_node__a1_n6_11',
                                    'ambulance_at_node__a1_n7_11',
                                    'ambulance_at_node__a1_n8_11',
                                    'person_waiting_service__n0_11',
                                    'person_waiting_service__n1_11',
                                    'person_waiting_service__n2_11',
                                    'person_waiting_service__n3_11',
                                    'person_waiting_service__n4_11',
                                    'person_waiting_service__n5_11',
                                    'person_waiting_service__n6_11',
                                    'person_waiting_service__n7_11',
                                    'person_waiting_service__n8_11',
                                    'person_in_ambulance__a0_12',
                                    'person_in_ambulance__a1_12',
                                    'ambulance_at_node__a0_n0_12',
                                    'ambulance_at_node__a0_n1_12',
                                    'ambulance_at_node__a0_n2_12',
                                    'ambulance_at_node__a0_n3_12',
                                    'ambulance_at_node__a0_n4_12',
                                    'ambulance_at_node__a0_n5_12',
                                    'ambulance_at_node__a0_n6_12',
                                    'ambulance_at_node__a0_n7_12',
                                    'ambulance_at_node__a0_n8_12',
                                    'ambulance_at_node__a1_n0_12',
                                    'ambulance_at_node__a1_n1_12',
                                    'ambulance_at_node__a1_n2_12',
                                    'ambulance_at_node__a1_n3_12',
                                    'ambulance_at_node__a1_n4_12',
                                    'ambulance_at_node__a1_n5_12',
                                    'ambulance_at_node__a1_n6_12',
                                    'ambulance_at_node__a1_n7_12',
                                    'ambulance_at_node__a1_n8_12',
                                    'person_waiting_service__n0_12',
                                    'person_waiting_service__n1_12',
                                    'person_waiting_service__n2_12',
                                    'person_waiting_service__n3_12',
                                    'person_waiting_service__n4_12',
                                    'person_waiting_service__n5_12',
                                    'person_waiting_service__n6_12',
                                    'person_waiting_service__n7_12',
                                    'person_waiting_service__n8_12',
                                    'person_in_ambulance__a0_13',
                                    'person_in_ambulance__a1_13',
                                    'ambulance_at_node__a0_n0_13',
                                    'ambulance_at_node__a0_n1_13',
                                    'ambulance_at_node__a0_n2_13',
                                    'ambulance_at_node__a0_n3_13',
                                    'ambulance_at_node__a0_n4_13',
                                    'ambulance_at_node__a0_n5_13',
                                    'ambulance_at_node__a0_n6_13',
                                    'ambulance_at_node__a0_n7_13',
                                    'ambulance_at_node__a0_n8_13',
                                    'ambulance_at_node__a1_n0_13',
                                    'ambulance_at_node__a1_n1_13',
                                    'ambulance_at_node__a1_n2_13',
                                    'ambulance_at_node__a1_n3_13',
                                    'ambulance_at_node__a1_n4_13',
                                    'ambulance_at_node__a1_n5_13',
                                    'ambulance_at_node__a1_n6_13',
                                    'ambulance_at_node__a1_n7_13',
                                    'ambulance_at_node__a1_n8_13',
                                    'person_waiting_service__n0_13',
                                    'person_waiting_service__n1_13',
                                    'person_waiting_service__n2_13',
                                    'person_waiting_service__n3_13',
                                    'person_waiting_service__n4_13',
                                    'person_waiting_service__n5_13',
                                    'person_waiting_service__n6_13',
                                    'person_waiting_service__n7_13',
                                    'person_waiting_service__n8_13',
                                    'person_in_ambulance__a0_14',
                                    'person_in_ambulance__a1_14',
                                    'ambulance_at_node__a0_n0_14',
                                    'ambulance_at_node__a0_n1_14',
                                    'ambulance_at_node__a0_n2_14',
                                    'ambulance_at_node__a0_n3_14',
                                    'ambulance_at_node__a0_n4_14',
                                    'ambulance_at_node__a0_n5_14',
                                    'ambulance_at_node__a0_n6_14',
                                    'ambulance_at_node__a0_n7_14',
                                    'ambulance_at_node__a0_n8_14',
                                    'ambulance_at_node__a1_n0_14',
                                    'ambulance_at_node__a1_n1_14',
                                    'ambulance_at_node__a1_n2_14',
                                    'ambulance_at_node__a1_n3_14',
                                    'ambulance_at_node__a1_n4_14',
                                    'ambulance_at_node__a1_n5_14',
                                    'ambulance_at_node__a1_n6_14',
                                    'ambulance_at_node__a1_n7_14',
                                    'ambulance_at_node__a1_n8_14',
                                    'person_waiting_service__n0_14',
                                    'person_waiting_service__n1_14',
                                    'person_waiting_service__n2_14',
                                    'person_waiting_service__n3_14',
                                    'person_waiting_service__n4_14',
                                    'person_waiting_service__n5_14',
                                    'person_waiting_service__n6_14',
                                    'person_waiting_service__n7_14',
                                    'person_waiting_service__n8_14',
                                    'person_in_ambulance__a0_15',
                                    'person_in_ambulance__a1_15',
                                    'ambulance_at_node__a0_n0_15',
                                    'ambulance_at_node__a0_n1_15',
                                    'ambulance_at_node__a0_n2_15',
                                    'ambulance_at_node__a0_n3_15',
                                    'ambulance_at_node__a0_n4_15',
                                    'ambulance_at_node__a0_n5_15',
                                    'ambulance_at_node__a0_n6_15',
                                    'ambulance_at_node__a0_n7_15',
                                    'ambulance_at_node__a0_n8_15',
                                    'ambulance_at_node__a1_n0_15',
                                    'ambulance_at_node__a1_n1_15',
                                    'ambulance_at_node__a1_n2_15',
                                    'ambulance_at_node__a1_n3_15',
                                    'ambulance_at_node__a1_n4_15',
                                    'ambulance_at_node__a1_n5_15',
                                    'ambulance_at_node__a1_n6_15',
                                    'ambulance_at_node__a1_n7_15',
                                    'ambulance_at_node__a1_n8_15',
                                    'person_waiting_service__n0_15',
                                    'person_waiting_service__n1_15',
                                    'person_waiting_service__n2_15',
                                    'person_waiting_service__n3_15',
                                    'person_waiting_service__n4_15',
                                    'person_waiting_service__n5_15',
                                    'person_waiting_service__n6_15',
                                    'person_waiting_service__n7_15',
                                    'person_waiting_service__n8_15',
                                    'person_in_ambulance__a0_16',
                                    'person_in_ambulance__a1_16',
                                    'ambulance_at_node__a0_n0_16',
                                    'ambulance_at_node__a0_n1_16',
                                    'ambulance_at_node__a0_n2_16',
                                    'ambulance_at_node__a0_n3_16',
                                    'ambulance_at_node__a0_n4_16',
                                    'ambulance_at_node__a0_n5_16',
                                    'ambulance_at_node__a0_n6_16',
                                    'ambulance_at_node__a0_n7_16',
                                    'ambulance_at_node__a0_n8_16',
                                    'ambulance_at_node__a1_n0_16',
                                    'ambulance_at_node__a1_n1_16',
                                    'ambulance_at_node__a1_n2_16',
                                    'ambulance_at_node__a1_n3_16',
                                    'ambulance_at_node__a1_n4_16',
                                    'ambulance_at_node__a1_n5_16',
                                    'ambulance_at_node__a1_n6_16',
                                    'ambulance_at_node__a1_n7_16',
                                    'ambulance_at_node__a1_n8_16',
                                    'person_waiting_service__n0_16',
                                    'person_waiting_service__n1_16',
                                    'person_waiting_service__n2_16',
                                    'person_waiting_service__n3_16',
                                    'person_waiting_service__n4_16',
                                    'person_waiting_service__n5_16',
                                    'person_waiting_service__n6_16',
                                    'person_waiting_service__n7_16',
                                    'person_waiting_service__n8_16',
                                    'person_in_ambulance__a0_17',
                                    'person_in_ambulance__a1_17',
                                    'ambulance_at_node__a0_n0_17',
                                    'ambulance_at_node__a0_n1_17',
                                    'ambulance_at_node__a0_n2_17',
                                    'ambulance_at_node__a0_n3_17',
                                    'ambulance_at_node__a0_n4_17',
                                    'ambulance_at_node__a0_n5_17',
                                    'ambulance_at_node__a0_n6_17',
                                    'ambulance_at_node__a0_n7_17',
                                    'ambulance_at_node__a0_n8_17',
                                    'ambulance_at_node__a1_n0_17',
                                    'ambulance_at_node__a1_n1_17',
                                    'ambulance_at_node__a1_n2_17',
                                    'ambulance_at_node__a1_n3_17',
                                    'ambulance_at_node__a1_n4_17',
                                    'ambulance_at_node__a1_n5_17',
                                    'ambulance_at_node__a1_n6_17',
                                    'ambulance_at_node__a1_n7_17',
                                    'ambulance_at_node__a1_n8_17',
                                    'person_waiting_service__n0_17',
                                    'person_waiting_service__n1_17',
                                    'person_waiting_service__n2_17',
                                    'person_waiting_service__n3_17',
                                    'person_waiting_service__n4_17',
                                    'person_waiting_service__n5_17',
                                    'person_waiting_service__n6_17',
                                    'person_waiting_service__n7_17',
                                    'person_waiting_service__n8_17',
                                    'person_in_ambulance__a0_18',
                                    'person_in_ambulance__a1_18',
                                    'ambulance_at_node__a0_n0_18',
                                    'ambulance_at_node__a0_n1_18',
                                    'ambulance_at_node__a0_n2_18',
                                    'ambulance_at_node__a0_n3_18',
                                    'ambulance_at_node__a0_n4_18',
                                    'ambulance_at_node__a0_n5_18',
                                    'ambulance_at_node__a0_n6_18',
                                    'ambulance_at_node__a0_n7_18',
                                    'ambulance_at_node__a0_n8_18',
                                    'ambulance_at_node__a1_n0_18',
                                    'ambulance_at_node__a1_n1_18',
                                    'ambulance_at_node__a1_n2_18',
                                    'ambulance_at_node__a1_n3_18',
                                    'ambulance_at_node__a1_n4_18',
                                    'ambulance_at_node__a1_n5_18',
                                    'ambulance_at_node__a1_n6_18',
                                    'ambulance_at_node__a1_n7_18',
                                    'ambulance_at_node__a1_n8_18',
                                    'person_waiting_service__n0_18',
                                    'person_waiting_service__n1_18',
                                    'person_waiting_service__n2_18',
                                    'person_waiting_service__n3_18',
                                    'person_waiting_service__n4_18',
                                    'person_waiting_service__n5_18',
                                    'person_waiting_service__n6_18',
                                    'person_waiting_service__n7_18',
                                    'person_waiting_service__n8_18',
                                    'person_in_ambulance__a0_19',
                                    'person_in_ambulance__a1_19',
                                    'ambulance_at_node__a0_n0_19',
                                    'ambulance_at_node__a0_n1_19',
                                    'ambulance_at_node__a0_n2_19',
                                    'ambulance_at_node__a0_n3_19',
                                    'ambulance_at_node__a0_n4_19',
                                    'ambulance_at_node__a0_n5_19',
                                    'ambulance_at_node__a0_n6_19',
                                    'ambulance_at_node__a0_n7_19',
                                    'ambulance_at_node__a0_n8_19',
                                    'ambulance_at_node__a1_n0_19',
                                    'ambulance_at_node__a1_n1_19',
                                    'ambulance_at_node__a1_n2_19',
                                    'ambulance_at_node__a1_n3_19',
                                    'ambulance_at_node__a1_n4_19',
                                    'ambulance_at_node__a1_n5_19',
                                    'ambulance_at_node__a1_n6_19',
                                    'ambulance_at_node__a1_n7_19',
                                    'ambulance_at_node__a1_n8_19',
                                    'person_waiting_service__n0_19',
                                    'person_waiting_service__n1_19',
                                    'person_waiting_service__n2_19',
                                    'person_waiting_service__n3_19',
                                    'person_waiting_service__n4_19',
                                    'person_waiting_service__n5_19',
                                    'person_waiting_service__n6_19',
                                    'person_waiting_service__n7_19',
                                    'person_waiting_service__n8_19',
                                    'person_in_ambulance__a0_20',
                                    'person_in_ambulance__a1_20',
                                    'ambulance_at_node__a0_n0_20',
                                    'ambulance_at_node__a0_n1_20',
                                    'ambulance_at_node__a0_n2_20',
                                    'ambulance_at_node__a0_n3_20',
                                    'ambulance_at_node__a0_n4_20',
                                    'ambulance_at_node__a0_n5_20',
                                    'ambulance_at_node__a0_n6_20',
                                    'ambulance_at_node__a0_n7_20',
                                    'ambulance_at_node__a0_n8_20',
                                    'ambulance_at_node__a1_n0_20',
                                    'ambulance_at_node__a1_n1_20',
                                    'ambulance_at_node__a1_n2_20',
                                    'ambulance_at_node__a1_n3_20',
                                    'ambulance_at_node__a1_n4_20',
                                    'ambulance_at_node__a1_n5_20',
                                    'ambulance_at_node__a1_n6_20',
                                    'ambulance_at_node__a1_n7_20',
                                    'ambulance_at_node__a1_n8_20',
                                    'person_waiting_service__n0_20',
                                    'person_waiting_service__n1_20',
                                    'person_waiting_service__n2_20',
                                    'person_waiting_service__n3_20',
                                    'person_waiting_service__n4_20',
                                    'person_waiting_service__n5_20',
                                    'person_waiting_service__n6_20',
                                    'person_waiting_service__n7_20',
                                    'person_waiting_service__n8_20',
                                    'person_in_ambulance__a0_21',
                                    'person_in_ambulance__a1_21',
                                    'ambulance_at_node__a0_n0_21',
                                    'ambulance_at_node__a0_n1_21',
                                    'ambulance_at_node__a0_n2_21',
                                    'ambulance_at_node__a0_n3_21',
                                    'ambulance_at_node__a0_n4_21',
                                    'ambulance_at_node__a0_n5_21',
                                    'ambulance_at_node__a0_n6_21',
                                    'ambulance_at_node__a0_n7_21',
                                    'ambulance_at_node__a0_n8_21',
                                    'ambulance_at_node__a1_n0_21',
                                    'ambulance_at_node__a1_n1_21',
                                    'ambulance_at_node__a1_n2_21',
                                    'ambulance_at_node__a1_n3_21',
                                    'ambulance_at_node__a1_n4_21',
                                    'ambulance_at_node__a1_n5_21',
                                    'ambulance_at_node__a1_n6_21',
                                    'ambulance_at_node__a1_n7_21',
                                    'ambulance_at_node__a1_n8_21',
                                    'person_waiting_service__n0_21',
                                    'person_waiting_service__n1_21',
                                    'person_waiting_service__n2_21',
                                    'person_waiting_service__n3_21',
                                    'person_waiting_service__n4_21',
                                    'person_waiting_service__n5_21',
                                    'person_waiting_service__n6_21',
                                    'person_waiting_service__n7_21',
                                    'person_waiting_service__n8_21',
                                    'person_in_ambulance__a0_22',
                                    'person_in_ambulance__a1_22',
                                    'ambulance_at_node__a0_n0_22',
                                    'ambulance_at_node__a0_n1_22',
                                    'ambulance_at_node__a0_n2_22',
                                    'ambulance_at_node__a0_n3_22',
                                    'ambulance_at_node__a0_n4_22',
                                    'ambulance_at_node__a0_n5_22',
                                    'ambulance_at_node__a0_n6_22',
                                    'ambulance_at_node__a0_n7_22',
                                    'ambulance_at_node__a0_n8_22',
                                    'ambulance_at_node__a1_n0_22',
                                    'ambulance_at_node__a1_n1_22',
                                    'ambulance_at_node__a1_n2_22',
                                    'ambulance_at_node__a1_n3_22',
                                    'ambulance_at_node__a1_n4_22',
                                    'ambulance_at_node__a1_n5_22',
                                    'ambulance_at_node__a1_n6_22',
                                    'ambulance_at_node__a1_n7_22',
                                    'ambulance_at_node__a1_n8_22',
                                    'person_waiting_service__n0_22',
                                    'person_waiting_service__n1_22',
                                    'person_waiting_service__n2_22',
                                    'person_waiting_service__n3_22',
                                    'person_waiting_service__n4_22',
                                    'person_waiting_service__n5_22',
                                    'person_waiting_service__n6_22',
                                    'person_waiting_service__n7_22',
                                    'person_waiting_service__n8_22',
                                    'person_in_ambulance__a0_23',
                                    'person_in_ambulance__a1_23',
                                    'ambulance_at_node__a0_n0_23',
                                    'ambulance_at_node__a0_n1_23',
                                    'ambulance_at_node__a0_n2_23',
                                    'ambulance_at_node__a0_n3_23',
                                    'ambulance_at_node__a0_n4_23',
                                    'ambulance_at_node__a0_n5_23',
                                    'ambulance_at_node__a0_n6_23',
                                    'ambulance_at_node__a0_n7_23',
                                    'ambulance_at_node__a0_n8_23',
                                    'ambulance_at_node__a1_n0_23',
                                    'ambulance_at_node__a1_n1_23',
                                    'ambulance_at_node__a1_n2_23',
                                    'ambulance_at_node__a1_n3_23',
                                    'ambulance_at_node__a1_n4_23',
                                    'ambulance_at_node__a1_n5_23',
                                    'ambulance_at_node__a1_n6_23',
                                    'ambulance_at_node__a1_n7_23',
                                    'ambulance_at_node__a1_n8_23',
                                    'person_waiting_service__n0_23',
                                    'person_waiting_service__n1_23',
                                    'person_waiting_service__n2_23',
                                    'person_waiting_service__n3_23',
                                    'person_waiting_service__n4_23',
                                    'person_waiting_service__n5_23',
                                    'person_waiting_service__n6_23',
                                    'person_waiting_service__n7_23',
                                    'person_waiting_service__n8_23',
                                    'person_in_ambulance__a0_24',
                                    'person_in_ambulance__a1_24',
                                    'ambulance_at_node__a0_n0_24',
                                    'ambulance_at_node__a0_n1_24',
                                    'ambulance_at_node__a0_n2_24',
                                    'ambulance_at_node__a0_n3_24',
                                    'ambulance_at_node__a0_n4_24',
                                    'ambulance_at_node__a0_n5_24',
                                    'ambulance_at_node__a0_n6_24',
                                    'ambulance_at_node__a0_n7_24',
                                    'ambulance_at_node__a0_n8_24',
                                    'ambulance_at_node__a1_n0_24',
                                    'ambulance_at_node__a1_n1_24',
                                    'ambulance_at_node__a1_n2_24',
                                    'ambulance_at_node__a1_n3_24',
                                    'ambulance_at_node__a1_n4_24',
                                    'ambulance_at_node__a1_n5_24',
                                    'ambulance_at_node__a1_n6_24',
                                    'ambulance_at_node__a1_n7_24',
                                    'ambulance_at_node__a1_n8_24',
                                    'person_waiting_service__n0_24',
                                    'person_waiting_service__n1_24',
                                    'person_waiting_service__n2_24',
                                    'person_waiting_service__n3_24',
                                    'person_waiting_service__n4_24',
                                    'person_waiting_service__n5_24',
                                    'person_waiting_service__n6_24',
                                    'person_waiting_service__n7_24',
                                    'person_waiting_service__n8_24',
                                    'person_in_ambulance__a0_25',
                                    'person_in_ambulance__a1_25',
                                    'ambulance_at_node__a0_n0_25',
                                    'ambulance_at_node__a0_n1_25',
                                    'ambulance_at_node__a0_n2_25',
                                    'ambulance_at_node__a0_n3_25',
                                    'ambulance_at_node__a0_n4_25',
                                    'ambulance_at_node__a0_n5_25',
                                    'ambulance_at_node__a0_n6_25',
                                    'ambulance_at_node__a0_n7_25',
                                    'ambulance_at_node__a0_n8_25',
                                    'ambulance_at_node__a1_n0_25',
                                    'ambulance_at_node__a1_n1_25',
                                    'ambulance_at_node__a1_n2_25',
                                    'ambulance_at_node__a1_n3_25',
                                    'ambulance_at_node__a1_n4_25',
                                    'ambulance_at_node__a1_n5_25',
                                    'ambulance_at_node__a1_n6_25',
                                    'ambulance_at_node__a1_n7_25',
                                    'ambulance_at_node__a1_n8_25',
                                    'person_waiting_service__n0_25',
                                    'person_waiting_service__n1_25',
                                    'person_waiting_service__n2_25',
                                    'person_waiting_service__n3_25',
                                    'person_waiting_service__n4_25',
                                    'person_waiting_service__n5_25',
                                    'person_waiting_service__n6_25',
                                    'person_waiting_service__n7_25',
                                    'person_waiting_service__n8_25',
                                    'person_in_ambulance__a0_26',
                                    'person_in_ambulance__a1_26',
                                    'ambulance_at_node__a0_n0_26',
                                    'ambulance_at_node__a0_n1_26',
                                    'ambulance_at_node__a0_n2_26',
                                    'ambulance_at_node__a0_n3_26',
                                    'ambulance_at_node__a0_n4_26',
                                    'ambulance_at_node__a0_n5_26',
                                    'ambulance_at_node__a0_n6_26',
                                    'ambulance_at_node__a0_n7_26',
                                    'ambulance_at_node__a0_n8_26',
                                    'ambulance_at_node__a1_n0_26',
                                    'ambulance_at_node__a1_n1_26',
                                    'ambulance_at_node__a1_n2_26',
                                    'ambulance_at_node__a1_n3_26',
                                    'ambulance_at_node__a1_n4_26',
                                    'ambulance_at_node__a1_n5_26',
                                    'ambulance_at_node__a1_n6_26',
                                    'ambulance_at_node__a1_n7_26',
                                    'ambulance_at_node__a1_n8_26',
                                    'person_waiting_service__n0_26',
                                    'person_waiting_service__n1_26',
                                    'person_waiting_service__n2_26',
                                    'person_waiting_service__n3_26',
                                    'person_waiting_service__n4_26',
                                    'person_waiting_service__n5_26',
                                    'person_waiting_service__n6_26',
                                    'person_waiting_service__n7_26',
                                    'person_waiting_service__n8_26',
                                    'person_in_ambulance__a0_27',
                                    'person_in_ambulance__a1_27',
                                    'ambulance_at_node__a0_n0_27',
                                    'ambulance_at_node__a0_n1_27',
                                    'ambulance_at_node__a0_n2_27',
                                    'ambulance_at_node__a0_n3_27',
                                    'ambulance_at_node__a0_n4_27',
                                    'ambulance_at_node__a0_n5_27',
                                    'ambulance_at_node__a0_n6_27',
                                    'ambulance_at_node__a0_n7_27',
                                    'ambulance_at_node__a0_n8_27',
                                    'ambulance_at_node__a1_n0_27',
                                    'ambulance_at_node__a1_n1_27',
                                    'ambulance_at_node__a1_n2_27',
                                    'ambulance_at_node__a1_n3_27',
                                    'ambulance_at_node__a1_n4_27',
                                    'ambulance_at_node__a1_n5_27',
                                    'ambulance_at_node__a1_n6_27',
                                    'ambulance_at_node__a1_n7_27',
                                    'ambulance_at_node__a1_n8_27',
                                    'person_waiting_service__n0_27',
                                    'person_waiting_service__n1_27',
                                    'person_waiting_service__n2_27',
                                    'person_waiting_service__n3_27',
                                    'person_waiting_service__n4_27',
                                    'person_waiting_service__n5_27',
                                    'person_waiting_service__n6_27',
                                    'person_waiting_service__n7_27',
                                    'person_waiting_service__n8_27',
                                    'person_in_ambulance__a0_28',
                                    'person_in_ambulance__a1_28',
                                    'ambulance_at_node__a0_n0_28',
                                    'ambulance_at_node__a0_n1_28',
                                    'ambulance_at_node__a0_n2_28',
                                    'ambulance_at_node__a0_n3_28',
                                    'ambulance_at_node__a0_n4_28',
                                    'ambulance_at_node__a0_n5_28',
                                    'ambulance_at_node__a0_n6_28',
                                    'ambulance_at_node__a0_n7_28',
                                    'ambulance_at_node__a0_n8_28',
                                    'ambulance_at_node__a1_n0_28',
                                    'ambulance_at_node__a1_n1_28',
                                    'ambulance_at_node__a1_n2_28',
                                    'ambulance_at_node__a1_n3_28',
                                    'ambulance_at_node__a1_n4_28',
                                    'ambulance_at_node__a1_n5_28',
                                    'ambulance_at_node__a1_n6_28',
                                    'ambulance_at_node__a1_n7_28',
                                    'ambulance_at_node__a1_n8_28',
                                    'person_waiting_service__n0_28',
                                    'person_waiting_service__n1_28',
                                    'person_waiting_service__n2_28',
                                    'person_waiting_service__n3_28',
                                    'person_waiting_service__n4_28',
                                    'person_waiting_service__n5_28',
                                    'person_waiting_service__n6_28',
                                    'person_waiting_service__n7_28',
                                    'person_waiting_service__n8_28',
                                    'person_in_ambulance__a0_29',
                                    'person_in_ambulance__a1_29',
                                    'ambulance_at_node__a0_n0_29',
                                    'ambulance_at_node__a0_n1_29',
                                    'ambulance_at_node__a0_n2_29',
                                    'ambulance_at_node__a0_n3_29',
                                    'ambulance_at_node__a0_n4_29',
                                    'ambulance_at_node__a0_n5_29',
                                    'ambulance_at_node__a0_n6_29',
                                    'ambulance_at_node__a0_n7_29',
                                    'ambulance_at_node__a0_n8_29',
                                    'ambulance_at_node__a1_n0_29',
                                    'ambulance_at_node__a1_n1_29',
                                    'ambulance_at_node__a1_n2_29',
                                    'ambulance_at_node__a1_n3_29',
                                    'ambulance_at_node__a1_n4_29',
                                    'ambulance_at_node__a1_n5_29',
                                    'ambulance_at_node__a1_n6_29',
                                    'ambulance_at_node__a1_n7_29',
                                    'ambulance_at_node__a1_n8_29',
                                    'person_waiting_service__n0_29',
                                    'person_waiting_service__n1_29',
                                    'person_waiting_service__n2_29',
                                    'person_waiting_service__n3_29',
                                    'person_waiting_service__n4_29',
                                    'person_waiting_service__n5_29',
                                    'person_waiting_service__n6_29',
                                    'person_waiting_service__n7_29',
                                    'person_waiting_service__n8_29',
                                    'person_in_ambulance__a0_30',
                                    'person_in_ambulance__a1_30',
                                    'ambulance_at_node__a0_n0_30',
                                    'ambulance_at_node__a0_n1_30',
                                    'ambulance_at_node__a0_n2_30',
                                    'ambulance_at_node__a0_n3_30',
                                    'ambulance_at_node__a0_n4_30',
                                    'ambulance_at_node__a0_n5_30',
                                    'ambulance_at_node__a0_n6_30',
                                    'ambulance_at_node__a0_n7_30',
                                    'ambulance_at_node__a0_n8_30',
                                    'ambulance_at_node__a1_n0_30',
                                    'ambulance_at_node__a1_n1_30',
                                    'ambulance_at_node__a1_n2_30',
                                    'ambulance_at_node__a1_n3_30',
                                    'ambulance_at_node__a1_n4_30',
                                    'ambulance_at_node__a1_n5_30',
                                    'ambulance_at_node__a1_n6_30',
                                    'ambulance_at_node__a1_n7_30',
                                    'ambulance_at_node__a1_n8_30',
                                    'person_waiting_service__n0_30',
                                    'person_waiting_service__n1_30',
                                    'person_waiting_service__n2_30',
                                    'person_waiting_service__n3_30',
                                    'person_waiting_service__n4_30',
                                    'person_waiting_service__n5_30',
                                    'person_waiting_service__n6_30',
                                    'person_waiting_service__n7_30',
                                    'person_waiting_service__n8_30',
                                    'person_in_ambulance__a0_31',
                                    'person_in_ambulance__a1_31',
                                    'ambulance_at_node__a0_n0_31',
                                    'ambulance_at_node__a0_n1_31',
                                    'ambulance_at_node__a0_n2_31',
                                    'ambulance_at_node__a0_n3_31',
                                    'ambulance_at_node__a0_n4_31',
                                    'ambulance_at_node__a0_n5_31',
                                    'ambulance_at_node__a0_n6_31',
                                    'ambulance_at_node__a0_n7_31',
                                    'ambulance_at_node__a0_n8_31',
                                    'ambulance_at_node__a1_n0_31',
                                    'ambulance_at_node__a1_n1_31',
                                    'ambulance_at_node__a1_n2_31',
                                    'ambulance_at_node__a1_n3_31',
                                    'ambulance_at_node__a1_n4_31',
                                    'ambulance_at_node__a1_n5_31',
                                    'ambulance_at_node__a1_n6_31',
                                    'ambulance_at_node__a1_n7_31',
                                    'ambulance_at_node__a1_n8_31',
                                    'person_waiting_service__n0_31',
                                    'person_waiting_service__n1_31',
                                    'person_waiting_service__n2_31',
                                    'person_waiting_service__n3_31',
                                    'person_waiting_service__n4_31',
                                    'person_waiting_service__n5_31',
                                    'person_waiting_service__n6_31',
                                    'person_waiting_service__n7_31',
                                    'person_waiting_service__n8_31',
                                    'person_in_ambulance__a0_32',
                                    'person_in_ambulance__a1_32',
                                    'ambulance_at_node__a0_n0_32',
                                    'ambulance_at_node__a0_n1_32',
                                    'ambulance_at_node__a0_n2_32',
                                    'ambulance_at_node__a0_n3_32',
                                    'ambulance_at_node__a0_n4_32',
                                    'ambulance_at_node__a0_n5_32',
                                    'ambulance_at_node__a0_n6_32',
                                    'ambulance_at_node__a0_n7_32',
                                    'ambulance_at_node__a0_n8_32',
                                    'ambulance_at_node__a1_n0_32',
                                    'ambulance_at_node__a1_n1_32',
                                    'ambulance_at_node__a1_n2_32',
                                    'ambulance_at_node__a1_n3_32',
                                    'ambulance_at_node__a1_n4_32',
                                    'ambulance_at_node__a1_n5_32',
                                    'ambulance_at_node__a1_n6_32',
                                    'ambulance_at_node__a1_n7_32',
                                    'ambulance_at_node__a1_n8_32',
                                    'person_waiting_service__n0_32',
                                    'person_waiting_service__n1_32',
                                    'person_waiting_service__n2_32',
                                    'person_waiting_service__n3_32',
                                    'person_waiting_service__n4_32',
                                    'person_waiting_service__n5_32',
                                    'person_waiting_service__n6_32',
                                    'person_waiting_service__n7_32',
                                    'person_waiting_service__n8_32',
                                    'person_in_ambulance__a0_33',
                                    'person_in_ambulance__a1_33',
                                    'ambulance_at_node__a0_n0_33',
                                    'ambulance_at_node__a0_n1_33',
                                    'ambulance_at_node__a0_n2_33',
                                    'ambulance_at_node__a0_n3_33',
                                    'ambulance_at_node__a0_n4_33',
                                    'ambulance_at_node__a0_n5_33',
                                    'ambulance_at_node__a0_n6_33',
                                    'ambulance_at_node__a0_n7_33',
                                    'ambulance_at_node__a0_n8_33',
                                    'ambulance_at_node__a1_n0_33',
                                    'ambulance_at_node__a1_n1_33',
                                    'ambulance_at_node__a1_n2_33',
                                    'ambulance_at_node__a1_n3_33',
                                    'ambulance_at_node__a1_n4_33',
                                    'ambulance_at_node__a1_n5_33',
                                    'ambulance_at_node__a1_n6_33',
                                    'ambulance_at_node__a1_n7_33',
                                    'ambulance_at_node__a1_n8_33',
                                    'person_waiting_service__n0_33',
                                    'person_waiting_service__n1_33',
                                    'person_waiting_service__n2_33',
                                    'person_waiting_service__n3_33',
                                    'person_waiting_service__n4_33',
                                    'person_waiting_service__n5_33',
                                    'person_waiting_service__n6_33',
                                    'person_waiting_service__n7_33',
                                    'person_waiting_service__n8_33',
                                    'person_in_ambulance__a0_34',
                                    'person_in_ambulance__a1_34',
                                    'ambulance_at_node__a0_n0_34',
                                    'ambulance_at_node__a0_n1_34',
                                    'ambulance_at_node__a0_n2_34',
                                    'ambulance_at_node__a0_n3_34',
                                    'ambulance_at_node__a0_n4_34',
                                    'ambulance_at_node__a0_n5_34',
                                    'ambulance_at_node__a0_n6_34',
                                    'ambulance_at_node__a0_n7_34',
                                    'ambulance_at_node__a0_n8_34',
                                    'ambulance_at_node__a1_n0_34',
                                    'ambulance_at_node__a1_n1_34',
                                    'ambulance_at_node__a1_n2_34',
                                    'ambulance_at_node__a1_n3_34',
                                    'ambulance_at_node__a1_n4_34',
                                    'ambulance_at_node__a1_n5_34',
                                    'ambulance_at_node__a1_n6_34',
                                    'ambulance_at_node__a1_n7_34',
                                    'ambulance_at_node__a1_n8_34',
                                    'person_waiting_service__n0_34',
                                    'person_waiting_service__n1_34',
                                    'person_waiting_service__n2_34',
                                    'person_waiting_service__n3_34',
                                    'person_waiting_service__n4_34',
                                    'person_waiting_service__n5_34',
                                    'person_waiting_service__n6_34',
                                    'person_waiting_service__n7_34',
                                    'person_waiting_service__n8_34',
                                    'person_in_ambulance__a0_35',
                                    'person_in_ambulance__a1_35',
                                    'ambulance_at_node__a0_n0_35',
                                    'ambulance_at_node__a0_n1_35',
                                    'ambulance_at_node__a0_n2_35',
                                    'ambulance_at_node__a0_n3_35',
                                    'ambulance_at_node__a0_n4_35',
                                    'ambulance_at_node__a0_n5_35',
                                    'ambulance_at_node__a0_n6_35',
                                    'ambulance_at_node__a0_n7_35',
                                    'ambulance_at_node__a0_n8_35',
                                    'ambulance_at_node__a1_n0_35',
                                    'ambulance_at_node__a1_n1_35',
                                    'ambulance_at_node__a1_n2_35',
                                    'ambulance_at_node__a1_n3_35',
                                    'ambulance_at_node__a1_n4_35',
                                    'ambulance_at_node__a1_n5_35',
                                    'ambulance_at_node__a1_n6_35',
                                    'ambulance_at_node__a1_n7_35',
                                    'ambulance_at_node__a1_n8_35',
                                    'person_waiting_service__n0_35',
                                    'person_waiting_service__n1_35',
                                    'person_waiting_service__n2_35',
                                    'person_waiting_service__n3_35',
                                    'person_waiting_service__n4_35',
                                    'person_waiting_service__n5_35',
                                    'person_waiting_service__n6_35',
                                    'person_waiting_service__n7_35',
                                    'person_waiting_service__n8_35',
                                    'person_in_ambulance__a0_36',
                                    'person_in_ambulance__a1_36',
                                    'ambulance_at_node__a0_n0_36',
                                    'ambulance_at_node__a0_n1_36',
                                    'ambulance_at_node__a0_n2_36',
                                    'ambulance_at_node__a0_n3_36',
                                    'ambulance_at_node__a0_n4_36',
                                    'ambulance_at_node__a0_n5_36',
                                    'ambulance_at_node__a0_n6_36',
                                    'ambulance_at_node__a0_n7_36',
                                    'ambulance_at_node__a0_n8_36',
                                    'ambulance_at_node__a1_n0_36',
                                    'ambulance_at_node__a1_n1_36',
                                    'ambulance_at_node__a1_n2_36',
                                    'ambulance_at_node__a1_n3_36',
                                    'ambulance_at_node__a1_n4_36',
                                    'ambulance_at_node__a1_n5_36',
                                    'ambulance_at_node__a1_n6_36',
                                    'ambulance_at_node__a1_n7_36',
                                    'ambulance_at_node__a1_n8_36',
                                    'person_waiting_service__n0_36',
                                    'person_waiting_service__n1_36',
                                    'person_waiting_service__n2_36',
                                    'person_waiting_service__n3_36',
                                    'person_waiting_service__n4_36',
                                    'person_waiting_service__n5_36',
                                    'person_waiting_service__n6_36',
                                    'person_waiting_service__n7_36',
                                    'person_waiting_service__n8_36',
                                    'person_in_ambulance__a0_37',
                                    'person_in_ambulance__a1_37',
                                    'ambulance_at_node__a0_n0_37',
                                    'ambulance_at_node__a0_n1_37',
                                    'ambulance_at_node__a0_n2_37',
                                    'ambulance_at_node__a0_n3_37',
                                    'ambulance_at_node__a0_n4_37',
                                    'ambulance_at_node__a0_n5_37',
                                    'ambulance_at_node__a0_n6_37',
                                    'ambulance_at_node__a0_n7_37',
                                    'ambulance_at_node__a0_n8_37',
                                    'ambulance_at_node__a1_n0_37',
                                    'ambulance_at_node__a1_n1_37',
                                    'ambulance_at_node__a1_n2_37',
                                    'ambulance_at_node__a1_n3_37',
                                    'ambulance_at_node__a1_n4_37',
                                    'ambulance_at_node__a1_n5_37',
                                    'ambulance_at_node__a1_n6_37',
                                    'ambulance_at_node__a1_n7_37',
                                    'ambulance_at_node__a1_n8_37',
                                    'person_waiting_service__n0_37',
                                    'person_waiting_service__n1_37',
                                    'person_waiting_service__n2_37',
                                    'person_waiting_service__n3_37',
                                    'person_waiting_service__n4_37',
                                    'person_waiting_service__n5_37',
                                    'person_waiting_service__n6_37',
                                    'person_waiting_service__n7_37',
                                    'person_waiting_service__n8_37',
                                    'person_in_ambulance__a0_38',
                                    'person_in_ambulance__a1_38',
                                    'ambulance_at_node__a0_n0_38',
                                    'ambulance_at_node__a0_n1_38',
                                    'ambulance_at_node__a0_n2_38',
                                    'ambulance_at_node__a0_n3_38',
                                    'ambulance_at_node__a0_n4_38',
                                    'ambulance_at_node__a0_n5_38',
                                    'ambulance_at_node__a0_n6_38',
                                    'ambulance_at_node__a0_n7_38',
                                    'ambulance_at_node__a0_n8_38',
                                    'ambulance_at_node__a1_n0_38',
                                    'ambulance_at_node__a1_n1_38',
                                    'ambulance_at_node__a1_n2_38',
                                    'ambulance_at_node__a1_n3_38',
                                    'ambulance_at_node__a1_n4_38',
                                    'ambulance_at_node__a1_n5_38',
                                    'ambulance_at_node__a1_n6_38',
                                    'ambulance_at_node__a1_n7_38',
                                    'ambulance_at_node__a1_n8_38',
                                    'person_waiting_service__n0_38',
                                    'person_waiting_service__n1_38',
                                    'person_waiting_service__n2_38',
                                    'person_waiting_service__n3_38',
                                    'person_waiting_service__n4_38',
                                    'person_waiting_service__n5_38',
                                    'person_waiting_service__n6_38',
                                    'person_waiting_service__n7_38',
                                    'person_waiting_service__n8_38',
                                    'person_in_ambulance__a0_39',
                                    'person_in_ambulance__a1_39',
                                    'ambulance_at_node__a0_n0_39',
                                    'ambulance_at_node__a0_n1_39',
                                    'ambulance_at_node__a0_n2_39',
                                    'ambulance_at_node__a0_n3_39',
                                    'ambulance_at_node__a0_n4_39',
                                    'ambulance_at_node__a0_n5_39',
                                    'ambulance_at_node__a0_n6_39',
                                    'ambulance_at_node__a0_n7_39',
                                    'ambulance_at_node__a0_n8_39',
                                    'ambulance_at_node__a1_n0_39',
                                    'ambulance_at_node__a1_n1_39',
                                    'ambulance_at_node__a1_n2_39',
                                    'ambulance_at_node__a1_n3_39',
                                    'ambulance_at_node__a1_n4_39',
                                    'ambulance_at_node__a1_n5_39',
                                    'ambulance_at_node__a1_n6_39',
                                    'ambulance_at_node__a1_n7_39',
                                    'ambulance_at_node__a1_n8_39',
                                    'person_waiting_service__n0_39',
                                    'person_waiting_service__n1_39',
                                    'person_waiting_service__n2_39',
                                    'person_waiting_service__n3_39',
                                    'person_waiting_service__n4_39',
                                    'person_waiting_service__n5_39',
                                    'person_waiting_service__n6_39',
                                    'person_waiting_service__n7_39',
                                    'person_waiting_service__n8_39']);

ambulance_mdp_model.add_edges_from([('person_in_ambulance__a0_0', 'person_in_ambulance__a0_1'),
                                    ('person_in_ambulance__a0_1', 'person_in_ambulance__a0_2'),
                                    ('person_in_ambulance__a0_2', 'person_in_ambulance__a0_3'),
                                    ('person_in_ambulance__a0_3', 'person_in_ambulance__a0_4'),
                                    ('person_in_ambulance__a0_4', 'person_in_ambulance__a0_5'),
                                    ('person_in_ambulance__a0_5', 'person_in_ambulance__a0_6'),
                                    ('person_in_ambulance__a0_6', 'person_in_ambulance__a0_7'),
                                    ('person_in_ambulance__a0_7', 'person_in_ambulance__a0_8'),
                                    ('person_in_ambulance__a0_8', 'person_in_ambulance__a0_9'),
                                    ('person_in_ambulance__a0_9', 'person_in_ambulance__a0_10'),
                                    ('person_in_ambulance__a0_10', 'person_in_ambulance__a0_11'),
                                    ('person_in_ambulance__a0_11', 'person_in_ambulance__a0_12'),
                                    ('person_in_ambulance__a0_12', 'person_in_ambulance__a0_13'),
                                    ('person_in_ambulance__a0_13', 'person_in_ambulance__a0_14'),
                                    ('person_in_ambulance__a0_14', 'person_in_ambulance__a0_15'),
                                    ('person_in_ambulance__a0_15', 'person_in_ambulance__a0_16'),
                                    ('person_in_ambulance__a0_16', 'person_in_ambulance__a0_17'),
                                    ('person_in_ambulance__a0_17', 'person_in_ambulance__a0_18'),
                                    ('person_in_ambulance__a0_18', 'person_in_ambulance__a0_19'),
                                    ('person_in_ambulance__a0_19', 'person_in_ambulance__a0_20'),
                                    ('person_in_ambulance__a0_20', 'person_in_ambulance__a0_21'),
                                    ('person_in_ambulance__a0_21', 'person_in_ambulance__a0_22'),
                                    ('person_in_ambulance__a0_22', 'person_in_ambulance__a0_23'),
                                    ('person_in_ambulance__a0_23', 'person_in_ambulance__a0_24'),
                                    ('person_in_ambulance__a0_24', 'person_in_ambulance__a0_25'),
                                    ('person_in_ambulance__a0_25', 'person_in_ambulance__a0_26'),
                                    ('person_in_ambulance__a0_26', 'person_in_ambulance__a0_27'),
                                    ('person_in_ambulance__a0_27', 'person_in_ambulance__a0_28'),
                                    ('person_in_ambulance__a0_28', 'person_in_ambulance__a0_29'),
                                    ('person_in_ambulance__a0_29', 'person_in_ambulance__a0_30'),
                                    ('person_in_ambulance__a0_30', 'person_in_ambulance__a0_31'),
                                    ('person_in_ambulance__a0_31', 'person_in_ambulance__a0_32'),
                                    ('person_in_ambulance__a0_32', 'person_in_ambulance__a0_33'),
                                    ('person_in_ambulance__a0_33', 'person_in_ambulance__a0_34'),
                                    ('person_in_ambulance__a0_34', 'person_in_ambulance__a0_35'),
                                    ('person_in_ambulance__a0_35', 'person_in_ambulance__a0_36'),
                                    ('person_in_ambulance__a0_36', 'person_in_ambulance__a0_37'),
                                    ('person_in_ambulance__a0_37', 'person_in_ambulance__a0_38'),
                                    ('person_in_ambulance__a0_38', 'person_in_ambulance__a0_39'),
                                    ('person_in_ambulance__a1_0', 'person_in_ambulance__a1_1'),
                                    ('person_in_ambulance__a1_1', 'person_in_ambulance__a1_2'),
                                    ('person_in_ambulance__a1_2', 'person_in_ambulance__a1_3'),
                                    ('person_in_ambulance__a1_3', 'person_in_ambulance__a1_4'),
                                    ('person_in_ambulance__a1_4', 'person_in_ambulance__a1_5'),
                                    ('person_in_ambulance__a1_5', 'person_in_ambulance__a1_6'),
                                    ('person_in_ambulance__a1_6', 'person_in_ambulance__a1_7'),
                                    ('person_in_ambulance__a1_7', 'person_in_ambulance__a1_8'),
                                    ('person_in_ambulance__a1_8', 'person_in_ambulance__a1_9'),
                                    ('person_in_ambulance__a1_9', 'person_in_ambulance__a1_10'),
                                    ('person_in_ambulance__a1_10', 'person_in_ambulance__a1_11'),
                                    ('person_in_ambulance__a1_11', 'person_in_ambulance__a1_12'),
                                    ('person_in_ambulance__a1_12', 'person_in_ambulance__a1_13'),
                                    ('person_in_ambulance__a1_13', 'person_in_ambulance__a1_14'),
                                    ('person_in_ambulance__a1_14', 'person_in_ambulance__a1_15'),
                                    ('person_in_ambulance__a1_15', 'person_in_ambulance__a1_16'),
                                    ('person_in_ambulance__a1_16', 'person_in_ambulance__a1_17'),
                                    ('person_in_ambulance__a1_17', 'person_in_ambulance__a1_18'),
                                    ('person_in_ambulance__a1_18', 'person_in_ambulance__a1_19'),
                                    ('person_in_ambulance__a1_19', 'person_in_ambulance__a1_20'),
                                    ('person_in_ambulance__a1_20', 'person_in_ambulance__a1_21'),
                                    ('person_in_ambulance__a1_21', 'person_in_ambulance__a1_22'),
                                    ('person_in_ambulance__a1_22', 'person_in_ambulance__a1_23'),
                                    ('person_in_ambulance__a1_23', 'person_in_ambulance__a1_24'),
                                    ('person_in_ambulance__a1_24', 'person_in_ambulance__a1_25'),
                                    ('person_in_ambulance__a1_25', 'person_in_ambulance__a1_26'),
                                    ('person_in_ambulance__a1_26', 'person_in_ambulance__a1_27'),
                                    ('person_in_ambulance__a1_27', 'person_in_ambulance__a1_28'),
                                    ('person_in_ambulance__a1_28', 'person_in_ambulance__a1_29'),
                                    ('person_in_ambulance__a1_29', 'person_in_ambulance__a1_30'),
                                    ('person_in_ambulance__a1_30', 'person_in_ambulance__a1_31'),
                                    ('person_in_ambulance__a1_31', 'person_in_ambulance__a1_32'),
                                    ('person_in_ambulance__a1_32', 'person_in_ambulance__a1_33'),
                                    ('person_in_ambulance__a1_33', 'person_in_ambulance__a1_34'),
                                    ('person_in_ambulance__a1_34', 'person_in_ambulance__a1_35'),
                                    ('person_in_ambulance__a1_35', 'person_in_ambulance__a1_36'),
                                    ('person_in_ambulance__a1_36', 'person_in_ambulance__a1_37'),
                                    ('person_in_ambulance__a1_37', 'person_in_ambulance__a1_38'),
                                    ('person_in_ambulance__a1_38', 'person_in_ambulance__a1_39'),
                                    ('ambulance_at_node__a0_n3_0', 'ambulance_at_node__a0_n3_1'),
                                    ('ambulance_at_node__a0_n3_1', 'ambulance_at_node__a0_n3_2'),
                                    ('ambulance_at_node__a0_n3_2', 'ambulance_at_node__a0_n3_3'),
                                    ('ambulance_at_node__a0_n3_3', 'ambulance_at_node__a0_n3_4'),
                                    ('ambulance_at_node__a0_n3_4', 'ambulance_at_node__a0_n3_5'),
                                    ('ambulance_at_node__a0_n3_5', 'ambulance_at_node__a0_n3_6'),
                                    ('ambulance_at_node__a0_n3_6', 'ambulance_at_node__a0_n3_7'),
                                    ('ambulance_at_node__a0_n3_7', 'ambulance_at_node__a0_n3_8'),
                                    ('ambulance_at_node__a0_n3_8', 'ambulance_at_node__a0_n3_9'),
                                    ('ambulance_at_node__a0_n3_9', 'ambulance_at_node__a0_n3_10'),
                                    ('ambulance_at_node__a0_n3_10', 'ambulance_at_node__a0_n3_11'),
                                    ('ambulance_at_node__a0_n3_11', 'ambulance_at_node__a0_n3_12'),
                                    ('ambulance_at_node__a0_n3_12', 'ambulance_at_node__a0_n3_13'),
                                    ('ambulance_at_node__a0_n3_13', 'ambulance_at_node__a0_n3_14'),
                                    ('ambulance_at_node__a0_n3_14', 'ambulance_at_node__a0_n3_15'),
                                    ('ambulance_at_node__a0_n3_15', 'ambulance_at_node__a0_n3_16'),
                                    ('ambulance_at_node__a0_n3_16', 'ambulance_at_node__a0_n3_17'),
                                    ('ambulance_at_node__a0_n3_17', 'ambulance_at_node__a0_n3_18'),
                                    ('ambulance_at_node__a0_n3_18', 'ambulance_at_node__a0_n3_19'),
                                    ('ambulance_at_node__a0_n3_19', 'ambulance_at_node__a0_n3_20'),
                                    ('ambulance_at_node__a0_n3_20', 'ambulance_at_node__a0_n3_21'),
                                    ('ambulance_at_node__a0_n3_21', 'ambulance_at_node__a0_n3_22'),
                                    ('ambulance_at_node__a0_n3_22', 'ambulance_at_node__a0_n3_23'),
                                    ('ambulance_at_node__a0_n3_23', 'ambulance_at_node__a0_n3_24'),
                                    ('ambulance_at_node__a0_n3_24', 'ambulance_at_node__a0_n3_25'),
                                    ('ambulance_at_node__a0_n3_25', 'ambulance_at_node__a0_n3_26'),
                                    ('ambulance_at_node__a0_n3_26', 'ambulance_at_node__a0_n3_27'),
                                    ('ambulance_at_node__a0_n3_27', 'ambulance_at_node__a0_n3_28'),
                                    ('ambulance_at_node__a0_n3_28', 'ambulance_at_node__a0_n3_29'),
                                    ('ambulance_at_node__a0_n3_29', 'ambulance_at_node__a0_n3_30'),
                                    ('ambulance_at_node__a0_n3_30', 'ambulance_at_node__a0_n3_31'),
                                    ('ambulance_at_node__a0_n3_31', 'ambulance_at_node__a0_n3_32'),
                                    ('ambulance_at_node__a0_n3_32', 'ambulance_at_node__a0_n3_33'),
                                    ('ambulance_at_node__a0_n3_33', 'ambulance_at_node__a0_n3_34'),
                                    ('ambulance_at_node__a0_n3_34', 'ambulance_at_node__a0_n3_35'),
                                    ('ambulance_at_node__a0_n3_35', 'ambulance_at_node__a0_n3_36'),
                                    ('ambulance_at_node__a0_n3_36', 'ambulance_at_node__a0_n3_37'),
                                    ('ambulance_at_node__a0_n3_37', 'ambulance_at_node__a0_n3_38'),
                                    ('ambulance_at_node__a0_n3_38', 'ambulance_at_node__a0_n3_39'),
                                    ('ambulance_at_node__a0_n0_0', 'ambulance_at_node__a0_n1_1'),
                                    ('ambulance_at_node__a0_n0_1', 'ambulance_at_node__a0_n1_2'),
                                    ('ambulance_at_node__a0_n0_2', 'ambulance_at_node__a0_n1_3'),
                                    ('ambulance_at_node__a0_n0_3', 'ambulance_at_node__a0_n1_4'),
                                    ('ambulance_at_node__a0_n0_4', 'ambulance_at_node__a0_n1_5'),
                                    ('ambulance_at_node__a0_n0_5', 'ambulance_at_node__a0_n1_6'),
                                    ('ambulance_at_node__a0_n0_6', 'ambulance_at_node__a0_n1_7'),
                                    ('ambulance_at_node__a0_n0_7', 'ambulance_at_node__a0_n1_8'),
                                    ('ambulance_at_node__a0_n0_8', 'ambulance_at_node__a0_n1_9'),
                                    ('ambulance_at_node__a0_n0_9', 'ambulance_at_node__a0_n1_10'),
                                    ('ambulance_at_node__a0_n0_10', 'ambulance_at_node__a0_n1_11'),
                                    ('ambulance_at_node__a0_n0_11', 'ambulance_at_node__a0_n1_12'),
                                    ('ambulance_at_node__a0_n0_12', 'ambulance_at_node__a0_n1_13'),
                                    ('ambulance_at_node__a0_n0_13', 'ambulance_at_node__a0_n1_14'),
                                    ('ambulance_at_node__a0_n0_14', 'ambulance_at_node__a0_n1_15'),
                                    ('ambulance_at_node__a0_n0_15', 'ambulance_at_node__a0_n1_16'),
                                    ('ambulance_at_node__a0_n0_16', 'ambulance_at_node__a0_n1_17'),
                                    ('ambulance_at_node__a0_n0_17', 'ambulance_at_node__a0_n1_18'),
                                    ('ambulance_at_node__a0_n0_18', 'ambulance_at_node__a0_n1_19'),
                                    ('ambulance_at_node__a0_n0_19', 'ambulance_at_node__a0_n1_20'),
                                    ('ambulance_at_node__a0_n0_20', 'ambulance_at_node__a0_n1_21'),
                                    ('ambulance_at_node__a0_n0_21', 'ambulance_at_node__a0_n1_22'),
                                    ('ambulance_at_node__a0_n0_22', 'ambulance_at_node__a0_n1_23'),
                                    ('ambulance_at_node__a0_n0_23', 'ambulance_at_node__a0_n1_24'),
                                    ('ambulance_at_node__a0_n0_24', 'ambulance_at_node__a0_n1_25'),
                                    ('ambulance_at_node__a0_n0_25', 'ambulance_at_node__a0_n1_26'),
                                    ('ambulance_at_node__a0_n0_26', 'ambulance_at_node__a0_n1_27'),
                                    ('ambulance_at_node__a0_n0_27', 'ambulance_at_node__a0_n1_28'),
                                    ('ambulance_at_node__a0_n0_28', 'ambulance_at_node__a0_n1_29'),
                                    ('ambulance_at_node__a0_n0_29', 'ambulance_at_node__a0_n1_30'),
                                    ('ambulance_at_node__a0_n0_30', 'ambulance_at_node__a0_n1_31'),
                                    ('ambulance_at_node__a0_n0_31', 'ambulance_at_node__a0_n1_32'),
                                    ('ambulance_at_node__a0_n0_32', 'ambulance_at_node__a0_n1_33'),
                                    ('ambulance_at_node__a0_n0_33', 'ambulance_at_node__a0_n1_34'),
                                    ('ambulance_at_node__a0_n0_34', 'ambulance_at_node__a0_n1_35'),
                                    ('ambulance_at_node__a0_n0_35', 'ambulance_at_node__a0_n1_36'),
                                    ('ambulance_at_node__a0_n0_36', 'ambulance_at_node__a0_n1_37'),
                                    ('ambulance_at_node__a0_n0_37', 'ambulance_at_node__a0_n1_38'),
                                    ('ambulance_at_node__a0_n0_38', 'ambulance_at_node__a0_n1_39'),
                                    ('ambulance_at_node__a0_n1_0', 'ambulance_at_node__a0_n1_1'),
                                    ('ambulance_at_node__a0_n1_1', 'ambulance_at_node__a0_n1_2'),
                                    ('ambulance_at_node__a0_n1_2', 'ambulance_at_node__a0_n1_3'),
                                    ('ambulance_at_node__a0_n1_3', 'ambulance_at_node__a0_n1_4'),
                                    ('ambulance_at_node__a0_n1_4', 'ambulance_at_node__a0_n1_5'),
                                    ('ambulance_at_node__a0_n1_5', 'ambulance_at_node__a0_n1_6'),
                                    ('ambulance_at_node__a0_n1_6', 'ambulance_at_node__a0_n1_7'),
                                    ('ambulance_at_node__a0_n1_7', 'ambulance_at_node__a0_n1_8'),
                                    ('ambulance_at_node__a0_n1_8', 'ambulance_at_node__a0_n1_9'),
                                    ('ambulance_at_node__a0_n1_9', 'ambulance_at_node__a0_n1_10'),
                                    ('ambulance_at_node__a0_n1_10', 'ambulance_at_node__a0_n1_11'),
                                    ('ambulance_at_node__a0_n1_11', 'ambulance_at_node__a0_n1_12'),
                                    ('ambulance_at_node__a0_n1_12', 'ambulance_at_node__a0_n1_13'),
                                    ('ambulance_at_node__a0_n1_13', 'ambulance_at_node__a0_n1_14'),
                                    ('ambulance_at_node__a0_n1_14', 'ambulance_at_node__a0_n1_15'),
                                    ('ambulance_at_node__a0_n1_15', 'ambulance_at_node__a0_n1_16'),
                                    ('ambulance_at_node__a0_n1_16', 'ambulance_at_node__a0_n1_17'),
                                    ('ambulance_at_node__a0_n1_17', 'ambulance_at_node__a0_n1_18'),
                                    ('ambulance_at_node__a0_n1_18', 'ambulance_at_node__a0_n1_19'),
                                    ('ambulance_at_node__a0_n1_19', 'ambulance_at_node__a0_n1_20'),
                                    ('ambulance_at_node__a0_n1_20', 'ambulance_at_node__a0_n1_21'),
                                    ('ambulance_at_node__a0_n1_21', 'ambulance_at_node__a0_n1_22'),
                                    ('ambulance_at_node__a0_n1_22', 'ambulance_at_node__a0_n1_23'),
                                    ('ambulance_at_node__a0_n1_23', 'ambulance_at_node__a0_n1_24'),
                                    ('ambulance_at_node__a0_n1_24', 'ambulance_at_node__a0_n1_25'),
                                    ('ambulance_at_node__a0_n1_25', 'ambulance_at_node__a0_n1_26'),
                                    ('ambulance_at_node__a0_n1_26', 'ambulance_at_node__a0_n1_27'),
                                    ('ambulance_at_node__a0_n1_27', 'ambulance_at_node__a0_n1_28'),
                                    ('ambulance_at_node__a0_n1_28', 'ambulance_at_node__a0_n1_29'),
                                    ('ambulance_at_node__a0_n1_29', 'ambulance_at_node__a0_n1_30'),
                                    ('ambulance_at_node__a0_n1_30', 'ambulance_at_node__a0_n1_31'),
                                    ('ambulance_at_node__a0_n1_31', 'ambulance_at_node__a0_n1_32'),
                                    ('ambulance_at_node__a0_n1_32', 'ambulance_at_node__a0_n1_33'),
                                    ('ambulance_at_node__a0_n1_33', 'ambulance_at_node__a0_n1_34'),
                                    ('ambulance_at_node__a0_n1_34', 'ambulance_at_node__a0_n1_35'),
                                    ('ambulance_at_node__a0_n1_35', 'ambulance_at_node__a0_n1_36'),
                                    ('ambulance_at_node__a0_n1_36', 'ambulance_at_node__a0_n1_37'),
                                    ('ambulance_at_node__a0_n1_37', 'ambulance_at_node__a0_n1_38'),
                                    ('ambulance_at_node__a0_n1_38', 'ambulance_at_node__a0_n1_39'),
                                    ('ambulance_at_node__a0_n2_0', 'ambulance_at_node__a0_n1_1'),
                                    ('ambulance_at_node__a0_n2_1', 'ambulance_at_node__a0_n1_2'),
                                    ('ambulance_at_node__a0_n2_2', 'ambulance_at_node__a0_n1_3'),
                                    ('ambulance_at_node__a0_n2_3', 'ambulance_at_node__a0_n1_4'),
                                    ('ambulance_at_node__a0_n2_4', 'ambulance_at_node__a0_n1_5'),
                                    ('ambulance_at_node__a0_n2_5', 'ambulance_at_node__a0_n1_6'),
                                    ('ambulance_at_node__a0_n2_6', 'ambulance_at_node__a0_n1_7'),
                                    ('ambulance_at_node__a0_n2_7', 'ambulance_at_node__a0_n1_8'),
                                    ('ambulance_at_node__a0_n2_8', 'ambulance_at_node__a0_n1_9'),
                                    ('ambulance_at_node__a0_n2_9', 'ambulance_at_node__a0_n1_10'),
                                    ('ambulance_at_node__a0_n2_10', 'ambulance_at_node__a0_n1_11'),
                                    ('ambulance_at_node__a0_n2_11', 'ambulance_at_node__a0_n1_12'),
                                    ('ambulance_at_node__a0_n2_12', 'ambulance_at_node__a0_n1_13'),
                                    ('ambulance_at_node__a0_n2_13', 'ambulance_at_node__a0_n1_14'),
                                    ('ambulance_at_node__a0_n2_14', 'ambulance_at_node__a0_n1_15'),
                                    ('ambulance_at_node__a0_n2_15', 'ambulance_at_node__a0_n1_16'),
                                    ('ambulance_at_node__a0_n2_16', 'ambulance_at_node__a0_n1_17'),
                                    ('ambulance_at_node__a0_n2_17', 'ambulance_at_node__a0_n1_18'),
                                    ('ambulance_at_node__a0_n2_18', 'ambulance_at_node__a0_n1_19'),
                                    ('ambulance_at_node__a0_n2_19', 'ambulance_at_node__a0_n1_20'),
                                    ('ambulance_at_node__a0_n2_20', 'ambulance_at_node__a0_n1_21'),
                                    ('ambulance_at_node__a0_n2_21', 'ambulance_at_node__a0_n1_22'),
                                    ('ambulance_at_node__a0_n2_22', 'ambulance_at_node__a0_n1_23'),
                                    ('ambulance_at_node__a0_n2_23', 'ambulance_at_node__a0_n1_24'),
                                    ('ambulance_at_node__a0_n2_24', 'ambulance_at_node__a0_n1_25'),
                                    ('ambulance_at_node__a0_n2_25', 'ambulance_at_node__a0_n1_26'),
                                    ('ambulance_at_node__a0_n2_26', 'ambulance_at_node__a0_n1_27'),
                                    ('ambulance_at_node__a0_n2_27', 'ambulance_at_node__a0_n1_28'),
                                    ('ambulance_at_node__a0_n2_28', 'ambulance_at_node__a0_n1_29'),
                                    ('ambulance_at_node__a0_n2_29', 'ambulance_at_node__a0_n1_30'),
                                    ('ambulance_at_node__a0_n2_30', 'ambulance_at_node__a0_n1_31'),
                                    ('ambulance_at_node__a0_n2_31', 'ambulance_at_node__a0_n1_32'),
                                    ('ambulance_at_node__a0_n2_32', 'ambulance_at_node__a0_n1_33'),
                                    ('ambulance_at_node__a0_n2_33', 'ambulance_at_node__a0_n1_34'),
                                    ('ambulance_at_node__a0_n2_34', 'ambulance_at_node__a0_n1_35'),
                                    ('ambulance_at_node__a0_n2_35', 'ambulance_at_node__a0_n1_36'),
                                    ('ambulance_at_node__a0_n2_36', 'ambulance_at_node__a0_n1_37'),
                                    ('ambulance_at_node__a0_n2_37', 'ambulance_at_node__a0_n1_38'),
                                    ('ambulance_at_node__a0_n2_38', 'ambulance_at_node__a0_n1_39'),
                                    ('ambulance_at_node__a0_n4_0', 'ambulance_at_node__a0_n1_1'),
                                    ('ambulance_at_node__a0_n4_1', 'ambulance_at_node__a0_n1_2'),
                                    ('ambulance_at_node__a0_n4_2', 'ambulance_at_node__a0_n1_3'),
                                    ('ambulance_at_node__a0_n4_3', 'ambulance_at_node__a0_n1_4'),
                                    ('ambulance_at_node__a0_n4_4', 'ambulance_at_node__a0_n1_5'),
                                    ('ambulance_at_node__a0_n4_5', 'ambulance_at_node__a0_n1_6'),
                                    ('ambulance_at_node__a0_n4_6', 'ambulance_at_node__a0_n1_7'),
                                    ('ambulance_at_node__a0_n4_7', 'ambulance_at_node__a0_n1_8'),
                                    ('ambulance_at_node__a0_n4_8', 'ambulance_at_node__a0_n1_9'),
                                    ('ambulance_at_node__a0_n4_9', 'ambulance_at_node__a0_n1_10'),
                                    ('ambulance_at_node__a0_n4_10', 'ambulance_at_node__a0_n1_11'),
                                    ('ambulance_at_node__a0_n4_11', 'ambulance_at_node__a0_n1_12'),
                                    ('ambulance_at_node__a0_n4_12', 'ambulance_at_node__a0_n1_13'),
                                    ('ambulance_at_node__a0_n4_13', 'ambulance_at_node__a0_n1_14'),
                                    ('ambulance_at_node__a0_n4_14', 'ambulance_at_node__a0_n1_15'),
                                    ('ambulance_at_node__a0_n4_15', 'ambulance_at_node__a0_n1_16'),
                                    ('ambulance_at_node__a0_n4_16', 'ambulance_at_node__a0_n1_17'),
                                    ('ambulance_at_node__a0_n4_17', 'ambulance_at_node__a0_n1_18'),
                                    ('ambulance_at_node__a0_n4_18', 'ambulance_at_node__a0_n1_19'),
                                    ('ambulance_at_node__a0_n4_19', 'ambulance_at_node__a0_n1_20'),
                                    ('ambulance_at_node__a0_n4_20', 'ambulance_at_node__a0_n1_21'),
                                    ('ambulance_at_node__a0_n4_21', 'ambulance_at_node__a0_n1_22'),
                                    ('ambulance_at_node__a0_n4_22', 'ambulance_at_node__a0_n1_23'),
                                    ('ambulance_at_node__a0_n4_23', 'ambulance_at_node__a0_n1_24'),
                                    ('ambulance_at_node__a0_n4_24', 'ambulance_at_node__a0_n1_25'),
                                    ('ambulance_at_node__a0_n4_25', 'ambulance_at_node__a0_n1_26'),
                                    ('ambulance_at_node__a0_n4_26', 'ambulance_at_node__a0_n1_27'),
                                    ('ambulance_at_node__a0_n4_27', 'ambulance_at_node__a0_n1_28'),
                                    ('ambulance_at_node__a0_n4_28', 'ambulance_at_node__a0_n1_29'),
                                    ('ambulance_at_node__a0_n4_29', 'ambulance_at_node__a0_n1_30'),
                                    ('ambulance_at_node__a0_n4_30', 'ambulance_at_node__a0_n1_31'),
                                    ('ambulance_at_node__a0_n4_31', 'ambulance_at_node__a0_n1_32'),
                                    ('ambulance_at_node__a0_n4_32', 'ambulance_at_node__a0_n1_33'),
                                    ('ambulance_at_node__a0_n4_33', 'ambulance_at_node__a0_n1_34'),
                                    ('ambulance_at_node__a0_n4_34', 'ambulance_at_node__a0_n1_35'),
                                    ('ambulance_at_node__a0_n4_35', 'ambulance_at_node__a0_n1_36'),
                                    ('ambulance_at_node__a0_n4_36', 'ambulance_at_node__a0_n1_37'),
                                    ('ambulance_at_node__a0_n4_37', 'ambulance_at_node__a0_n1_38'),
                                    ('ambulance_at_node__a0_n4_38', 'ambulance_at_node__a0_n1_39'),
                                    ('ambulance_at_node__a0_n8_0', 'ambulance_at_node__a0_n8_1'),
                                    ('ambulance_at_node__a0_n8_1', 'ambulance_at_node__a0_n8_2'),
                                    ('ambulance_at_node__a0_n8_2', 'ambulance_at_node__a0_n8_3'),
                                    ('ambulance_at_node__a0_n8_3', 'ambulance_at_node__a0_n8_4'),
                                    ('ambulance_at_node__a0_n8_4', 'ambulance_at_node__a0_n8_5'),
                                    ('ambulance_at_node__a0_n8_5', 'ambulance_at_node__a0_n8_6'),
                                    ('ambulance_at_node__a0_n8_6', 'ambulance_at_node__a0_n8_7'),
                                    ('ambulance_at_node__a0_n8_7', 'ambulance_at_node__a0_n8_8'),
                                    ('ambulance_at_node__a0_n8_8', 'ambulance_at_node__a0_n8_9'),
                                    ('ambulance_at_node__a0_n8_9', 'ambulance_at_node__a0_n8_10'),
                                    ('ambulance_at_node__a0_n8_10', 'ambulance_at_node__a0_n8_11'),
                                    ('ambulance_at_node__a0_n8_11', 'ambulance_at_node__a0_n8_12'),
                                    ('ambulance_at_node__a0_n8_12', 'ambulance_at_node__a0_n8_13'),
                                    ('ambulance_at_node__a0_n8_13', 'ambulance_at_node__a0_n8_14'),
                                    ('ambulance_at_node__a0_n8_14', 'ambulance_at_node__a0_n8_15'),
                                    ('ambulance_at_node__a0_n8_15', 'ambulance_at_node__a0_n8_16'),
                                    ('ambulance_at_node__a0_n8_16', 'ambulance_at_node__a0_n8_17'),
                                    ('ambulance_at_node__a0_n8_17', 'ambulance_at_node__a0_n8_18'),
                                    ('ambulance_at_node__a0_n8_18', 'ambulance_at_node__a0_n8_19'),
                                    ('ambulance_at_node__a0_n8_19', 'ambulance_at_node__a0_n8_20'),
                                    ('ambulance_at_node__a0_n8_20', 'ambulance_at_node__a0_n8_21'),
                                    ('ambulance_at_node__a0_n8_21', 'ambulance_at_node__a0_n8_22'),
                                    ('ambulance_at_node__a0_n8_22', 'ambulance_at_node__a0_n8_23'),
                                    ('ambulance_at_node__a0_n8_23', 'ambulance_at_node__a0_n8_24'),
                                    ('ambulance_at_node__a0_n8_24', 'ambulance_at_node__a0_n8_25'),
                                    ('ambulance_at_node__a0_n8_25', 'ambulance_at_node__a0_n8_26'),
                                    ('ambulance_at_node__a0_n8_26', 'ambulance_at_node__a0_n8_27'),
                                    ('ambulance_at_node__a0_n8_27', 'ambulance_at_node__a0_n8_28'),
                                    ('ambulance_at_node__a0_n8_28', 'ambulance_at_node__a0_n8_29'),
                                    ('ambulance_at_node__a0_n8_29', 'ambulance_at_node__a0_n8_30'),
                                    ('ambulance_at_node__a0_n8_30', 'ambulance_at_node__a0_n8_31'),
                                    ('ambulance_at_node__a0_n8_31', 'ambulance_at_node__a0_n8_32'),
                                    ('ambulance_at_node__a0_n8_32', 'ambulance_at_node__a0_n8_33'),
                                    ('ambulance_at_node__a0_n8_33', 'ambulance_at_node__a0_n8_34'),
                                    ('ambulance_at_node__a0_n8_34', 'ambulance_at_node__a0_n8_35'),
                                    ('ambulance_at_node__a0_n8_35', 'ambulance_at_node__a0_n8_36'),
                                    ('ambulance_at_node__a0_n8_36', 'ambulance_at_node__a0_n8_37'),
                                    ('ambulance_at_node__a0_n8_37', 'ambulance_at_node__a0_n8_38'),
                                    ('ambulance_at_node__a0_n8_38', 'ambulance_at_node__a0_n8_39'),
                                    ('ambulance_at_node__a0_n7_0', 'ambulance_at_node__a0_n7_1'),
                                    ('ambulance_at_node__a0_n7_1', 'ambulance_at_node__a0_n7_2'),
                                    ('ambulance_at_node__a0_n7_2', 'ambulance_at_node__a0_n7_3'),
                                    ('ambulance_at_node__a0_n7_3', 'ambulance_at_node__a0_n7_4'),
                                    ('ambulance_at_node__a0_n7_4', 'ambulance_at_node__a0_n7_5'),
                                    ('ambulance_at_node__a0_n7_5', 'ambulance_at_node__a0_n7_6'),
                                    ('ambulance_at_node__a0_n7_6', 'ambulance_at_node__a0_n7_7'),
                                    ('ambulance_at_node__a0_n7_7', 'ambulance_at_node__a0_n7_8'),
                                    ('ambulance_at_node__a0_n7_8', 'ambulance_at_node__a0_n7_9'),
                                    ('ambulance_at_node__a0_n7_9', 'ambulance_at_node__a0_n7_10'),
                                    ('ambulance_at_node__a0_n7_10', 'ambulance_at_node__a0_n7_11'),
                                    ('ambulance_at_node__a0_n7_11', 'ambulance_at_node__a0_n7_12'),
                                    ('ambulance_at_node__a0_n7_12', 'ambulance_at_node__a0_n7_13'),
                                    ('ambulance_at_node__a0_n7_13', 'ambulance_at_node__a0_n7_14'),
                                    ('ambulance_at_node__a0_n7_14', 'ambulance_at_node__a0_n7_15'),
                                    ('ambulance_at_node__a0_n7_15', 'ambulance_at_node__a0_n7_16'),
                                    ('ambulance_at_node__a0_n7_16', 'ambulance_at_node__a0_n7_17'),
                                    ('ambulance_at_node__a0_n7_17', 'ambulance_at_node__a0_n7_18'),
                                    ('ambulance_at_node__a0_n7_18', 'ambulance_at_node__a0_n7_19'),
                                    ('ambulance_at_node__a0_n7_19', 'ambulance_at_node__a0_n7_20'),
                                    ('ambulance_at_node__a0_n7_20', 'ambulance_at_node__a0_n7_21'),
                                    ('ambulance_at_node__a0_n7_21', 'ambulance_at_node__a0_n7_22'),
                                    ('ambulance_at_node__a0_n7_22', 'ambulance_at_node__a0_n7_23'),
                                    ('ambulance_at_node__a0_n7_23', 'ambulance_at_node__a0_n7_24'),
                                    ('ambulance_at_node__a0_n7_24', 'ambulance_at_node__a0_n7_25'),
                                    ('ambulance_at_node__a0_n7_25', 'ambulance_at_node__a0_n7_26'),
                                    ('ambulance_at_node__a0_n7_26', 'ambulance_at_node__a0_n7_27'),
                                    ('ambulance_at_node__a0_n7_27', 'ambulance_at_node__a0_n7_28'),
                                    ('ambulance_at_node__a0_n7_28', 'ambulance_at_node__a0_n7_29'),
                                    ('ambulance_at_node__a0_n7_29', 'ambulance_at_node__a0_n7_30'),
                                    ('ambulance_at_node__a0_n7_30', 'ambulance_at_node__a0_n7_31'),
                                    ('ambulance_at_node__a0_n7_31', 'ambulance_at_node__a0_n7_32'),
                                    ('ambulance_at_node__a0_n7_32', 'ambulance_at_node__a0_n7_33'),
                                    ('ambulance_at_node__a0_n7_33', 'ambulance_at_node__a0_n7_34'),
                                    ('ambulance_at_node__a0_n7_34', 'ambulance_at_node__a0_n7_35'),
                                    ('ambulance_at_node__a0_n7_35', 'ambulance_at_node__a0_n7_36'),
                                    ('ambulance_at_node__a0_n7_36', 'ambulance_at_node__a0_n7_37'),
                                    ('ambulance_at_node__a0_n7_37', 'ambulance_at_node__a0_n7_38'),
                                    ('ambulance_at_node__a0_n7_38', 'ambulance_at_node__a0_n7_39'),
                                    ('ambulance_at_node__a0_n6_0', 'ambulance_at_node__a0_n6_1'),
                                    ('ambulance_at_node__a0_n6_1', 'ambulance_at_node__a0_n6_2'),
                                    ('ambulance_at_node__a0_n6_2', 'ambulance_at_node__a0_n6_3'),
                                    ('ambulance_at_node__a0_n6_3', 'ambulance_at_node__a0_n6_4'),
                                    ('ambulance_at_node__a0_n6_4', 'ambulance_at_node__a0_n6_5'),
                                    ('ambulance_at_node__a0_n6_5', 'ambulance_at_node__a0_n6_6'),
                                    ('ambulance_at_node__a0_n6_6', 'ambulance_at_node__a0_n6_7'),
                                    ('ambulance_at_node__a0_n6_7', 'ambulance_at_node__a0_n6_8'),
                                    ('ambulance_at_node__a0_n6_8', 'ambulance_at_node__a0_n6_9'),
                                    ('ambulance_at_node__a0_n6_9', 'ambulance_at_node__a0_n6_10'),
                                    ('ambulance_at_node__a0_n6_10', 'ambulance_at_node__a0_n6_11'),
                                    ('ambulance_at_node__a0_n6_11', 'ambulance_at_node__a0_n6_12'),
                                    ('ambulance_at_node__a0_n6_12', 'ambulance_at_node__a0_n6_13'),
                                    ('ambulance_at_node__a0_n6_13', 'ambulance_at_node__a0_n6_14'),
                                    ('ambulance_at_node__a0_n6_14', 'ambulance_at_node__a0_n6_15'),
                                    ('ambulance_at_node__a0_n6_15', 'ambulance_at_node__a0_n6_16'),
                                    ('ambulance_at_node__a0_n6_16', 'ambulance_at_node__a0_n6_17'),
                                    ('ambulance_at_node__a0_n6_17', 'ambulance_at_node__a0_n6_18'),
                                    ('ambulance_at_node__a0_n6_18', 'ambulance_at_node__a0_n6_19'),
                                    ('ambulance_at_node__a0_n6_19', 'ambulance_at_node__a0_n6_20'),
                                    ('ambulance_at_node__a0_n6_20', 'ambulance_at_node__a0_n6_21'),
                                    ('ambulance_at_node__a0_n6_21', 'ambulance_at_node__a0_n6_22'),
                                    ('ambulance_at_node__a0_n6_22', 'ambulance_at_node__a0_n6_23'),
                                    ('ambulance_at_node__a0_n6_23', 'ambulance_at_node__a0_n6_24'),
                                    ('ambulance_at_node__a0_n6_24', 'ambulance_at_node__a0_n6_25'),
                                    ('ambulance_at_node__a0_n6_25', 'ambulance_at_node__a0_n6_26'),
                                    ('ambulance_at_node__a0_n6_26', 'ambulance_at_node__a0_n6_27'),
                                    ('ambulance_at_node__a0_n6_27', 'ambulance_at_node__a0_n6_28'),
                                    ('ambulance_at_node__a0_n6_28', 'ambulance_at_node__a0_n6_29'),
                                    ('ambulance_at_node__a0_n6_29', 'ambulance_at_node__a0_n6_30'),
                                    ('ambulance_at_node__a0_n6_30', 'ambulance_at_node__a0_n6_31'),
                                    ('ambulance_at_node__a0_n6_31', 'ambulance_at_node__a0_n6_32'),
                                    ('ambulance_at_node__a0_n6_32', 'ambulance_at_node__a0_n6_33'),
                                    ('ambulance_at_node__a0_n6_33', 'ambulance_at_node__a0_n6_34'),
                                    ('ambulance_at_node__a0_n6_34', 'ambulance_at_node__a0_n6_35'),
                                    ('ambulance_at_node__a0_n6_35', 'ambulance_at_node__a0_n6_36'),
                                    ('ambulance_at_node__a0_n6_36', 'ambulance_at_node__a0_n6_37'),
                                    ('ambulance_at_node__a0_n6_37', 'ambulance_at_node__a0_n6_38'),
                                    ('ambulance_at_node__a0_n6_38', 'ambulance_at_node__a0_n6_39'),
                                    ('ambulance_at_node__a0_n5_0', 'ambulance_at_node__a0_n5_1'),
                                    ('ambulance_at_node__a0_n5_1', 'ambulance_at_node__a0_n5_2'),
                                    ('ambulance_at_node__a0_n5_2', 'ambulance_at_node__a0_n5_3'),
                                    ('ambulance_at_node__a0_n5_3', 'ambulance_at_node__a0_n5_4'),
                                    ('ambulance_at_node__a0_n5_4', 'ambulance_at_node__a0_n5_5'),
                                    ('ambulance_at_node__a0_n5_5', 'ambulance_at_node__a0_n5_6'),
                                    ('ambulance_at_node__a0_n5_6', 'ambulance_at_node__a0_n5_7'),
                                    ('ambulance_at_node__a0_n5_7', 'ambulance_at_node__a0_n5_8'),
                                    ('ambulance_at_node__a0_n5_8', 'ambulance_at_node__a0_n5_9'),
                                    ('ambulance_at_node__a0_n5_9', 'ambulance_at_node__a0_n5_10'),
                                    ('ambulance_at_node__a0_n5_10', 'ambulance_at_node__a0_n5_11'),
                                    ('ambulance_at_node__a0_n5_11', 'ambulance_at_node__a0_n5_12'),
                                    ('ambulance_at_node__a0_n5_12', 'ambulance_at_node__a0_n5_13'),
                                    ('ambulance_at_node__a0_n5_13', 'ambulance_at_node__a0_n5_14'),
                                    ('ambulance_at_node__a0_n5_14', 'ambulance_at_node__a0_n5_15'),
                                    ('ambulance_at_node__a0_n5_15', 'ambulance_at_node__a0_n5_16'),
                                    ('ambulance_at_node__a0_n5_16', 'ambulance_at_node__a0_n5_17'),
                                    ('ambulance_at_node__a0_n5_17', 'ambulance_at_node__a0_n5_18'),
                                    ('ambulance_at_node__a0_n5_18', 'ambulance_at_node__a0_n5_19'),
                                    ('ambulance_at_node__a0_n5_19', 'ambulance_at_node__a0_n5_20'),
                                    ('ambulance_at_node__a0_n5_20', 'ambulance_at_node__a0_n5_21'),
                                    ('ambulance_at_node__a0_n5_21', 'ambulance_at_node__a0_n5_22'),
                                    ('ambulance_at_node__a0_n5_22', 'ambulance_at_node__a0_n5_23'),
                                    ('ambulance_at_node__a0_n5_23', 'ambulance_at_node__a0_n5_24'),
                                    ('ambulance_at_node__a0_n5_24', 'ambulance_at_node__a0_n5_25'),
                                    ('ambulance_at_node__a0_n5_25', 'ambulance_at_node__a0_n5_26'),
                                    ('ambulance_at_node__a0_n5_26', 'ambulance_at_node__a0_n5_27'),
                                    ('ambulance_at_node__a0_n5_27', 'ambulance_at_node__a0_n5_28'),
                                    ('ambulance_at_node__a0_n5_28', 'ambulance_at_node__a0_n5_29'),
                                    ('ambulance_at_node__a0_n5_29', 'ambulance_at_node__a0_n5_30'),
                                    ('ambulance_at_node__a0_n5_30', 'ambulance_at_node__a0_n5_31'),
                                    ('ambulance_at_node__a0_n5_31', 'ambulance_at_node__a0_n5_32'),
                                    ('ambulance_at_node__a0_n5_32', 'ambulance_at_node__a0_n5_33'),
                                    ('ambulance_at_node__a0_n5_33', 'ambulance_at_node__a0_n5_34'),
                                    ('ambulance_at_node__a0_n5_34', 'ambulance_at_node__a0_n5_35'),
                                    ('ambulance_at_node__a0_n5_35', 'ambulance_at_node__a0_n5_36'),
                                    ('ambulance_at_node__a0_n5_36', 'ambulance_at_node__a0_n5_37'),
                                    ('ambulance_at_node__a0_n5_37', 'ambulance_at_node__a0_n5_38'),
                                    ('ambulance_at_node__a0_n5_38', 'ambulance_at_node__a0_n5_39'),
                                    ('person_waiting_service__n0_0', 'person_waiting_service__n0_1'),
                                    ('person_waiting_service__n0_1', 'person_waiting_service__n0_2'),
                                    ('person_waiting_service__n0_2', 'person_waiting_service__n0_3'),
                                    ('person_waiting_service__n0_3', 'person_waiting_service__n0_4'),
                                    ('person_waiting_service__n0_4', 'person_waiting_service__n0_5'),
                                    ('person_waiting_service__n0_5', 'person_waiting_service__n0_6'),
                                    ('person_waiting_service__n0_6', 'person_waiting_service__n0_7'),
                                    ('person_waiting_service__n0_7', 'person_waiting_service__n0_8'),
                                    ('person_waiting_service__n0_8', 'person_waiting_service__n0_9'),
                                    ('person_waiting_service__n0_9', 'person_waiting_service__n0_10'),
                                    ('person_waiting_service__n0_10', 'person_waiting_service__n0_11'),
                                    ('person_waiting_service__n0_11', 'person_waiting_service__n0_12'),
                                    ('person_waiting_service__n0_12', 'person_waiting_service__n0_13'),
                                    ('person_waiting_service__n0_13', 'person_waiting_service__n0_14'),
                                    ('person_waiting_service__n0_14', 'person_waiting_service__n0_15'),
                                    ('person_waiting_service__n0_15', 'person_waiting_service__n0_16'),
                                    ('person_waiting_service__n0_16', 'person_waiting_service__n0_17'),
                                    ('person_waiting_service__n0_17', 'person_waiting_service__n0_18'),
                                    ('person_waiting_service__n0_18', 'person_waiting_service__n0_19'),
                                    ('person_waiting_service__n0_19', 'person_waiting_service__n0_20'),
                                    ('person_waiting_service__n0_20', 'person_waiting_service__n0_21'),
                                    ('person_waiting_service__n0_21', 'person_waiting_service__n0_22'),
                                    ('person_waiting_service__n0_22', 'person_waiting_service__n0_23'),
                                    ('person_waiting_service__n0_23', 'person_waiting_service__n0_24'),
                                    ('person_waiting_service__n0_24', 'person_waiting_service__n0_25'),
                                    ('person_waiting_service__n0_25', 'person_waiting_service__n0_26'),
                                    ('person_waiting_service__n0_26', 'person_waiting_service__n0_27'),
                                    ('person_waiting_service__n0_27', 'person_waiting_service__n0_28'),
                                    ('person_waiting_service__n0_28', 'person_waiting_service__n0_29'),
                                    ('person_waiting_service__n0_29', 'person_waiting_service__n0_30'),
                                    ('person_waiting_service__n0_30', 'person_waiting_service__n0_31'),
                                    ('person_waiting_service__n0_31', 'person_waiting_service__n0_32'),
                                    ('person_waiting_service__n0_32', 'person_waiting_service__n0_33'),
                                    ('person_waiting_service__n0_33', 'person_waiting_service__n0_34'),
                                    ('person_waiting_service__n0_34', 'person_waiting_service__n0_35'),
                                    ('person_waiting_service__n0_35', 'person_waiting_service__n0_36'),
                                    ('person_waiting_service__n0_36', 'person_waiting_service__n0_37'),
                                    ('person_waiting_service__n0_37', 'person_waiting_service__n0_38'),
                                    ('person_waiting_service__n0_38', 'person_waiting_service__n0_39'),
                                    ('person_waiting_service__n3_0', 'person_waiting_service__n3_1'),
                                    ('person_waiting_service__n3_1', 'person_waiting_service__n3_2'),
                                    ('person_waiting_service__n3_2', 'person_waiting_service__n3_3'),
                                    ('person_waiting_service__n3_3', 'person_waiting_service__n3_4'),
                                    ('person_waiting_service__n3_4', 'person_waiting_service__n3_5'),
                                    ('person_waiting_service__n3_5', 'person_waiting_service__n3_6'),
                                    ('person_waiting_service__n3_6', 'person_waiting_service__n3_7'),
                                    ('person_waiting_service__n3_7', 'person_waiting_service__n3_8'),
                                    ('person_waiting_service__n3_8', 'person_waiting_service__n3_9'),
                                    ('person_waiting_service__n3_9', 'person_waiting_service__n3_10'),
                                    ('person_waiting_service__n3_10', 'person_waiting_service__n3_11'),
                                    ('person_waiting_service__n3_11', 'person_waiting_service__n3_12'),
                                    ('person_waiting_service__n3_12', 'person_waiting_service__n3_13'),
                                    ('person_waiting_service__n3_13', 'person_waiting_service__n3_14'),
                                    ('person_waiting_service__n3_14', 'person_waiting_service__n3_15'),
                                    ('person_waiting_service__n3_15', 'person_waiting_service__n3_16'),
                                    ('person_waiting_service__n3_16', 'person_waiting_service__n3_17'),
                                    ('person_waiting_service__n3_17', 'person_waiting_service__n3_18'),
                                    ('person_waiting_service__n3_18', 'person_waiting_service__n3_19'),
                                    ('person_waiting_service__n3_19', 'person_waiting_service__n3_20'),
                                    ('person_waiting_service__n3_20', 'person_waiting_service__n3_21'),
                                    ('person_waiting_service__n3_21', 'person_waiting_service__n3_22'),
                                    ('person_waiting_service__n3_22', 'person_waiting_service__n3_23'),
                                    ('person_waiting_service__n3_23', 'person_waiting_service__n3_24'),
                                    ('person_waiting_service__n3_24', 'person_waiting_service__n3_25'),
                                    ('person_waiting_service__n3_25', 'person_waiting_service__n3_26'),
                                    ('person_waiting_service__n3_26', 'person_waiting_service__n3_27'),
                                    ('person_waiting_service__n3_27', 'person_waiting_service__n3_28'),
                                    ('person_waiting_service__n3_28', 'person_waiting_service__n3_29'),
                                    ('person_waiting_service__n3_29', 'person_waiting_service__n3_30'),
                                    ('person_waiting_service__n3_30', 'person_waiting_service__n3_31'),
                                    ('person_waiting_service__n3_31', 'person_waiting_service__n3_32'),
                                    ('person_waiting_service__n3_32', 'person_waiting_service__n3_33'),
                                    ('person_waiting_service__n3_33', 'person_waiting_service__n3_34'),
                                    ('person_waiting_service__n3_34', 'person_waiting_service__n3_35'),
                                    ('person_waiting_service__n3_35', 'person_waiting_service__n3_36'),
                                    ('person_waiting_service__n3_36', 'person_waiting_service__n3_37'),
                                    ('person_waiting_service__n3_37', 'person_waiting_service__n3_38'),
                                    ('person_waiting_service__n3_38', 'person_waiting_service__n3_39'),
                                    ('person_waiting_service__n4_0', 'person_waiting_service__n4_1'),
                                    ('person_waiting_service__n4_1', 'person_waiting_service__n4_2'),
                                    ('person_waiting_service__n4_2', 'person_waiting_service__n4_3'),
                                    ('person_waiting_service__n4_3', 'person_waiting_service__n4_4'),
                                    ('person_waiting_service__n4_4', 'person_waiting_service__n4_5'),
                                    ('person_waiting_service__n4_5', 'person_waiting_service__n4_6'),
                                    ('person_waiting_service__n4_6', 'person_waiting_service__n4_7'),
                                    ('person_waiting_service__n4_7', 'person_waiting_service__n4_8'),
                                    ('person_waiting_service__n4_8', 'person_waiting_service__n4_9'),
                                    ('person_waiting_service__n4_9', 'person_waiting_service__n4_10'),
                                    ('person_waiting_service__n4_10', 'person_waiting_service__n4_11'),
                                    ('person_waiting_service__n4_11', 'person_waiting_service__n4_12'),
                                    ('person_waiting_service__n4_12', 'person_waiting_service__n4_13'),
                                    ('person_waiting_service__n4_13', 'person_waiting_service__n4_14'),
                                    ('person_waiting_service__n4_14', 'person_waiting_service__n4_15'),
                                    ('person_waiting_service__n4_15', 'person_waiting_service__n4_16'),
                                    ('person_waiting_service__n4_16', 'person_waiting_service__n4_17'),
                                    ('person_waiting_service__n4_17', 'person_waiting_service__n4_18'),
                                    ('person_waiting_service__n4_18', 'person_waiting_service__n4_19'),
                                    ('person_waiting_service__n4_19', 'person_waiting_service__n4_20'),
                                    ('person_waiting_service__n4_20', 'person_waiting_service__n4_21'),
                                    ('person_waiting_service__n4_21', 'person_waiting_service__n4_22'),
                                    ('person_waiting_service__n4_22', 'person_waiting_service__n4_23'),
                                    ('person_waiting_service__n4_23', 'person_waiting_service__n4_24'),
                                    ('person_waiting_service__n4_24', 'person_waiting_service__n4_25'),
                                    ('person_waiting_service__n4_25', 'person_waiting_service__n4_26'),
                                    ('person_waiting_service__n4_26', 'person_waiting_service__n4_27'),
                                    ('person_waiting_service__n4_27', 'person_waiting_service__n4_28'),
                                    ('person_waiting_service__n4_28', 'person_waiting_service__n4_29'),
                                    ('person_waiting_service__n4_29', 'person_waiting_service__n4_30'),
                                    ('person_waiting_service__n4_30', 'person_waiting_service__n4_31'),
                                    ('person_waiting_service__n4_31', 'person_waiting_service__n4_32'),
                                    ('person_waiting_service__n4_32', 'person_waiting_service__n4_33'),
                                    ('person_waiting_service__n4_33', 'person_waiting_service__n4_34'),
                                    ('person_waiting_service__n4_34', 'person_waiting_service__n4_35'),
                                    ('person_waiting_service__n4_35', 'person_waiting_service__n4_36'),
                                    ('person_waiting_service__n4_36', 'person_waiting_service__n4_37'),
                                    ('person_waiting_service__n4_37', 'person_waiting_service__n4_38'),
                                    ('person_waiting_service__n4_38', 'person_waiting_service__n4_39'),
                                    ('person_waiting_service__n1_0', 'person_waiting_service__n1_1'),
                                    ('person_waiting_service__n1_1', 'person_waiting_service__n1_2'),
                                    ('person_waiting_service__n1_2', 'person_waiting_service__n1_3'),
                                    ('person_waiting_service__n1_3', 'person_waiting_service__n1_4'),
                                    ('person_waiting_service__n1_4', 'person_waiting_service__n1_5'),
                                    ('person_waiting_service__n1_5', 'person_waiting_service__n1_6'),
                                    ('person_waiting_service__n1_6', 'person_waiting_service__n1_7'),
                                    ('person_waiting_service__n1_7', 'person_waiting_service__n1_8'),
                                    ('person_waiting_service__n1_8', 'person_waiting_service__n1_9'),
                                    ('person_waiting_service__n1_9', 'person_waiting_service__n1_10'),
                                    ('person_waiting_service__n1_10', 'person_waiting_service__n1_11'),
                                    ('person_waiting_service__n1_11', 'person_waiting_service__n1_12'),
                                    ('person_waiting_service__n1_12', 'person_waiting_service__n1_13'),
                                    ('person_waiting_service__n1_13', 'person_waiting_service__n1_14'),
                                    ('person_waiting_service__n1_14', 'person_waiting_service__n1_15'),
                                    ('person_waiting_service__n1_15', 'person_waiting_service__n1_16'),
                                    ('person_waiting_service__n1_16', 'person_waiting_service__n1_17'),
                                    ('person_waiting_service__n1_17', 'person_waiting_service__n1_18'),
                                    ('person_waiting_service__n1_18', 'person_waiting_service__n1_19'),
                                    ('person_waiting_service__n1_19', 'person_waiting_service__n1_20'),
                                    ('person_waiting_service__n1_20', 'person_waiting_service__n1_21'),
                                    ('person_waiting_service__n1_21', 'person_waiting_service__n1_22'),
                                    ('person_waiting_service__n1_22', 'person_waiting_service__n1_23'),
                                    ('person_waiting_service__n1_23', 'person_waiting_service__n1_24'),
                                    ('person_waiting_service__n1_24', 'person_waiting_service__n1_25'),
                                    ('person_waiting_service__n1_25', 'person_waiting_service__n1_26'),
                                    ('person_waiting_service__n1_26', 'person_waiting_service__n1_27'),
                                    ('person_waiting_service__n1_27', 'person_waiting_service__n1_28'),
                                    ('person_waiting_service__n1_28', 'person_waiting_service__n1_29'),
                                    ('person_waiting_service__n1_29', 'person_waiting_service__n1_30'),
                                    ('person_waiting_service__n1_30', 'person_waiting_service__n1_31'),
                                    ('person_waiting_service__n1_31', 'person_waiting_service__n1_32'),
                                    ('person_waiting_service__n1_32', 'person_waiting_service__n1_33'),
                                    ('person_waiting_service__n1_33', 'person_waiting_service__n1_34'),
                                    ('person_waiting_service__n1_34', 'person_waiting_service__n1_35'),
                                    ('person_waiting_service__n1_35', 'person_waiting_service__n1_36'),
                                    ('person_waiting_service__n1_36', 'person_waiting_service__n1_37'),
                                    ('person_waiting_service__n1_37', 'person_waiting_service__n1_38'),
                                    ('person_waiting_service__n1_38', 'person_waiting_service__n1_39'),
                                    ('person_waiting_service__n2_0', 'person_waiting_service__n2_1'),
                                    ('person_waiting_service__n2_1', 'person_waiting_service__n2_2'),
                                    ('person_waiting_service__n2_2', 'person_waiting_service__n2_3'),
                                    ('person_waiting_service__n2_3', 'person_waiting_service__n2_4'),
                                    ('person_waiting_service__n2_4', 'person_waiting_service__n2_5'),
                                    ('person_waiting_service__n2_5', 'person_waiting_service__n2_6'),
                                    ('person_waiting_service__n2_6', 'person_waiting_service__n2_7'),
                                    ('person_waiting_service__n2_7', 'person_waiting_service__n2_8'),
                                    ('person_waiting_service__n2_8', 'person_waiting_service__n2_9'),
                                    ('person_waiting_service__n2_9', 'person_waiting_service__n2_10'),
                                    ('person_waiting_service__n2_10', 'person_waiting_service__n2_11'),
                                    ('person_waiting_service__n2_11', 'person_waiting_service__n2_12'),
                                    ('person_waiting_service__n2_12', 'person_waiting_service__n2_13'),
                                    ('person_waiting_service__n2_13', 'person_waiting_service__n2_14'),
                                    ('person_waiting_service__n2_14', 'person_waiting_service__n2_15'),
                                    ('person_waiting_service__n2_15', 'person_waiting_service__n2_16'),
                                    ('person_waiting_service__n2_16', 'person_waiting_service__n2_17'),
                                    ('person_waiting_service__n2_17', 'person_waiting_service__n2_18'),
                                    ('person_waiting_service__n2_18', 'person_waiting_service__n2_19'),
                                    ('person_waiting_service__n2_19', 'person_waiting_service__n2_20'),
                                    ('person_waiting_service__n2_20', 'person_waiting_service__n2_21'),
                                    ('person_waiting_service__n2_21', 'person_waiting_service__n2_22'),
                                    ('person_waiting_service__n2_22', 'person_waiting_service__n2_23'),
                                    ('person_waiting_service__n2_23', 'person_waiting_service__n2_24'),
                                    ('person_waiting_service__n2_24', 'person_waiting_service__n2_25'),
                                    ('person_waiting_service__n2_25', 'person_waiting_service__n2_26'),
                                    ('person_waiting_service__n2_26', 'person_waiting_service__n2_27'),
                                    ('person_waiting_service__n2_27', 'person_waiting_service__n2_28'),
                                    ('person_waiting_service__n2_28', 'person_waiting_service__n2_29'),
                                    ('person_waiting_service__n2_29', 'person_waiting_service__n2_30'),
                                    ('person_waiting_service__n2_30', 'person_waiting_service__n2_31'),
                                    ('person_waiting_service__n2_31', 'person_waiting_service__n2_32'),
                                    ('person_waiting_service__n2_32', 'person_waiting_service__n2_33'),
                                    ('person_waiting_service__n2_33', 'person_waiting_service__n2_34'),
                                    ('person_waiting_service__n2_34', 'person_waiting_service__n2_35'),
                                    ('person_waiting_service__n2_35', 'person_waiting_service__n2_36'),
                                    ('person_waiting_service__n2_36', 'person_waiting_service__n2_37'),
                                    ('person_waiting_service__n2_37', 'person_waiting_service__n2_38'),
                                    ('person_waiting_service__n2_38', 'person_waiting_service__n2_39'),
                                    ('person_waiting_service__n7_0', 'person_waiting_service__n7_1'),
                                    ('person_waiting_service__n7_1', 'person_waiting_service__n7_2'),
                                    ('person_waiting_service__n7_2', 'person_waiting_service__n7_3'),
                                    ('person_waiting_service__n7_3', 'person_waiting_service__n7_4'),
                                    ('person_waiting_service__n7_4', 'person_waiting_service__n7_5'),
                                    ('person_waiting_service__n7_5', 'person_waiting_service__n7_6'),
                                    ('person_waiting_service__n7_6', 'person_waiting_service__n7_7'),
                                    ('person_waiting_service__n7_7', 'person_waiting_service__n7_8'),
                                    ('person_waiting_service__n7_8', 'person_waiting_service__n7_9'),
                                    ('person_waiting_service__n7_9', 'person_waiting_service__n7_10'),
                                    ('person_waiting_service__n7_10', 'person_waiting_service__n7_11'),
                                    ('person_waiting_service__n7_11', 'person_waiting_service__n7_12'),
                                    ('person_waiting_service__n7_12', 'person_waiting_service__n7_13'),
                                    ('person_waiting_service__n7_13', 'person_waiting_service__n7_14'),
                                    ('person_waiting_service__n7_14', 'person_waiting_service__n7_15'),
                                    ('person_waiting_service__n7_15', 'person_waiting_service__n7_16'),
                                    ('person_waiting_service__n7_16', 'person_waiting_service__n7_17'),
                                    ('person_waiting_service__n7_17', 'person_waiting_service__n7_18'),
                                    ('person_waiting_service__n7_18', 'person_waiting_service__n7_19'),
                                    ('person_waiting_service__n7_19', 'person_waiting_service__n7_20'),
                                    ('person_waiting_service__n7_20', 'person_waiting_service__n7_21'),
                                    ('person_waiting_service__n7_21', 'person_waiting_service__n7_22'),
                                    ('person_waiting_service__n7_22', 'person_waiting_service__n7_23'),
                                    ('person_waiting_service__n7_23', 'person_waiting_service__n7_24'),
                                    ('person_waiting_service__n7_24', 'person_waiting_service__n7_25'),
                                    ('person_waiting_service__n7_25', 'person_waiting_service__n7_26'),
                                    ('person_waiting_service__n7_26', 'person_waiting_service__n7_27'),
                                    ('person_waiting_service__n7_27', 'person_waiting_service__n7_28'),
                                    ('person_waiting_service__n7_28', 'person_waiting_service__n7_29'),
                                    ('person_waiting_service__n7_29', 'person_waiting_service__n7_30'),
                                    ('person_waiting_service__n7_30', 'person_waiting_service__n7_31'),
                                    ('person_waiting_service__n7_31', 'person_waiting_service__n7_32'),
                                    ('person_waiting_service__n7_32', 'person_waiting_service__n7_33'),
                                    ('person_waiting_service__n7_33', 'person_waiting_service__n7_34'),
                                    ('person_waiting_service__n7_34', 'person_waiting_service__n7_35'),
                                    ('person_waiting_service__n7_35', 'person_waiting_service__n7_36'),
                                    ('person_waiting_service__n7_36', 'person_waiting_service__n7_37'),
                                    ('person_waiting_service__n7_37', 'person_waiting_service__n7_38'),
                                    ('person_waiting_service__n7_38', 'person_waiting_service__n7_39'),
                                    ('person_waiting_service__n8_0', 'person_waiting_service__n8_1'),
                                    ('person_waiting_service__n8_1', 'person_waiting_service__n8_2'),
                                    ('person_waiting_service__n8_2', 'person_waiting_service__n8_3'),
                                    ('person_waiting_service__n8_3', 'person_waiting_service__n8_4'),
                                    ('person_waiting_service__n8_4', 'person_waiting_service__n8_5'),
                                    ('person_waiting_service__n8_5', 'person_waiting_service__n8_6'),
                                    ('person_waiting_service__n8_6', 'person_waiting_service__n8_7'),
                                    ('person_waiting_service__n8_7', 'person_waiting_service__n8_8'),
                                    ('person_waiting_service__n8_8', 'person_waiting_service__n8_9'),
                                    ('person_waiting_service__n8_9', 'person_waiting_service__n8_10'),
                                    ('person_waiting_service__n8_10', 'person_waiting_service__n8_11'),
                                    ('person_waiting_service__n8_11', 'person_waiting_service__n8_12'),
                                    ('person_waiting_service__n8_12', 'person_waiting_service__n8_13'),
                                    ('person_waiting_service__n8_13', 'person_waiting_service__n8_14'),
                                    ('person_waiting_service__n8_14', 'person_waiting_service__n8_15'),
                                    ('person_waiting_service__n8_15', 'person_waiting_service__n8_16'),
                                    ('person_waiting_service__n8_16', 'person_waiting_service__n8_17'),
                                    ('person_waiting_service__n8_17', 'person_waiting_service__n8_18'),
                                    ('person_waiting_service__n8_18', 'person_waiting_service__n8_19'),
                                    ('person_waiting_service__n8_19', 'person_waiting_service__n8_20'),
                                    ('person_waiting_service__n8_20', 'person_waiting_service__n8_21'),
                                    ('person_waiting_service__n8_21', 'person_waiting_service__n8_22'),
                                    ('person_waiting_service__n8_22', 'person_waiting_service__n8_23'),
                                    ('person_waiting_service__n8_23', 'person_waiting_service__n8_24'),
                                    ('person_waiting_service__n8_24', 'person_waiting_service__n8_25'),
                                    ('person_waiting_service__n8_25', 'person_waiting_service__n8_26'),
                                    ('person_waiting_service__n8_26', 'person_waiting_service__n8_27'),
                                    ('person_waiting_service__n8_27', 'person_waiting_service__n8_28'),
                                    ('person_waiting_service__n8_28', 'person_waiting_service__n8_29'),
                                    ('person_waiting_service__n8_29', 'person_waiting_service__n8_30'),
                                    ('person_waiting_service__n8_30', 'person_waiting_service__n8_31'),
                                    ('person_waiting_service__n8_31', 'person_waiting_service__n8_32'),
                                    ('person_waiting_service__n8_32', 'person_waiting_service__n8_33'),
                                    ('person_waiting_service__n8_33', 'person_waiting_service__n8_34'),
                                    ('person_waiting_service__n8_34', 'person_waiting_service__n8_35'),
                                    ('person_waiting_service__n8_35', 'person_waiting_service__n8_36'),
                                    ('person_waiting_service__n8_36', 'person_waiting_service__n8_37'),
                                    ('person_waiting_service__n8_37', 'person_waiting_service__n8_38'),
                                    ('person_waiting_service__n8_38', 'person_waiting_service__n8_39'),
                                    ('person_waiting_service__n5_0', 'person_waiting_service__n5_1'),
                                    ('person_waiting_service__n5_1', 'person_waiting_service__n5_2'),
                                    ('person_waiting_service__n5_2', 'person_waiting_service__n5_3'),
                                    ('person_waiting_service__n5_3', 'person_waiting_service__n5_4'),
                                    ('person_waiting_service__n5_4', 'person_waiting_service__n5_5'),
                                    ('person_waiting_service__n5_5', 'person_waiting_service__n5_6'),
                                    ('person_waiting_service__n5_6', 'person_waiting_service__n5_7'),
                                    ('person_waiting_service__n5_7', 'person_waiting_service__n5_8'),
                                    ('person_waiting_service__n5_8', 'person_waiting_service__n5_9'),
                                    ('person_waiting_service__n5_9', 'person_waiting_service__n5_10'),
                                    ('person_waiting_service__n5_10', 'person_waiting_service__n5_11'),
                                    ('person_waiting_service__n5_11', 'person_waiting_service__n5_12'),
                                    ('person_waiting_service__n5_12', 'person_waiting_service__n5_13'),
                                    ('person_waiting_service__n5_13', 'person_waiting_service__n5_14'),
                                    ('person_waiting_service__n5_14', 'person_waiting_service__n5_15'),
                                    ('person_waiting_service__n5_15', 'person_waiting_service__n5_16'),
                                    ('person_waiting_service__n5_16', 'person_waiting_service__n5_17'),
                                    ('person_waiting_service__n5_17', 'person_waiting_service__n5_18'),
                                    ('person_waiting_service__n5_18', 'person_waiting_service__n5_19'),
                                    ('person_waiting_service__n5_19', 'person_waiting_service__n5_20'),
                                    ('person_waiting_service__n5_20', 'person_waiting_service__n5_21'),
                                    ('person_waiting_service__n5_21', 'person_waiting_service__n5_22'),
                                    ('person_waiting_service__n5_22', 'person_waiting_service__n5_23'),
                                    ('person_waiting_service__n5_23', 'person_waiting_service__n5_24'),
                                    ('person_waiting_service__n5_24', 'person_waiting_service__n5_25'),
                                    ('person_waiting_service__n5_25', 'person_waiting_service__n5_26'),
                                    ('person_waiting_service__n5_26', 'person_waiting_service__n5_27'),
                                    ('person_waiting_service__n5_27', 'person_waiting_service__n5_28'),
                                    ('person_waiting_service__n5_28', 'person_waiting_service__n5_29'),
                                    ('person_waiting_service__n5_29', 'person_waiting_service__n5_30'),
                                    ('person_waiting_service__n5_30', 'person_waiting_service__n5_31'),
                                    ('person_waiting_service__n5_31', 'person_waiting_service__n5_32'),
                                    ('person_waiting_service__n5_32', 'person_waiting_service__n5_33'),
                                    ('person_waiting_service__n5_33', 'person_waiting_service__n5_34'),
                                    ('person_waiting_service__n5_34', 'person_waiting_service__n5_35'),
                                    ('person_waiting_service__n5_35', 'person_waiting_service__n5_36'),
                                    ('person_waiting_service__n5_36', 'person_waiting_service__n5_37'),
                                    ('person_waiting_service__n5_37', 'person_waiting_service__n5_38'),
                                    ('person_waiting_service__n5_38', 'person_waiting_service__n5_39'),
                                    ('person_waiting_service__n6_0', 'person_waiting_service__n6_1'),
                                    ('person_waiting_service__n6_1', 'person_waiting_service__n6_2'),
                                    ('person_waiting_service__n6_2', 'person_waiting_service__n6_3'),
                                    ('person_waiting_service__n6_3', 'person_waiting_service__n6_4'),
                                    ('person_waiting_service__n6_4', 'person_waiting_service__n6_5'),
                                    ('person_waiting_service__n6_5', 'person_waiting_service__n6_6'),
                                    ('person_waiting_service__n6_6', 'person_waiting_service__n6_7'),
                                    ('person_waiting_service__n6_7', 'person_waiting_service__n6_8'),
                                    ('person_waiting_service__n6_8', 'person_waiting_service__n6_9'),
                                    ('person_waiting_service__n6_9', 'person_waiting_service__n6_10'),
                                    ('person_waiting_service__n6_10', 'person_waiting_service__n6_11'),
                                    ('person_waiting_service__n6_11', 'person_waiting_service__n6_12'),
                                    ('person_waiting_service__n6_12', 'person_waiting_service__n6_13'),
                                    ('person_waiting_service__n6_13', 'person_waiting_service__n6_14'),
                                    ('person_waiting_service__n6_14', 'person_waiting_service__n6_15'),
                                    ('person_waiting_service__n6_15', 'person_waiting_service__n6_16'),
                                    ('person_waiting_service__n6_16', 'person_waiting_service__n6_17'),
                                    ('person_waiting_service__n6_17', 'person_waiting_service__n6_18'),
                                    ('person_waiting_service__n6_18', 'person_waiting_service__n6_19'),
                                    ('person_waiting_service__n6_19', 'person_waiting_service__n6_20'),
                                    ('person_waiting_service__n6_20', 'person_waiting_service__n6_21'),
                                    ('person_waiting_service__n6_21', 'person_waiting_service__n6_22'),
                                    ('person_waiting_service__n6_22', 'person_waiting_service__n6_23'),
                                    ('person_waiting_service__n6_23', 'person_waiting_service__n6_24'),
                                    ('person_waiting_service__n6_24', 'person_waiting_service__n6_25'),
                                    ('person_waiting_service__n6_25', 'person_waiting_service__n6_26'),
                                    ('person_waiting_service__n6_26', 'person_waiting_service__n6_27'),
                                    ('person_waiting_service__n6_27', 'person_waiting_service__n6_28'),
                                    ('person_waiting_service__n6_28', 'person_waiting_service__n6_29'),
                                    ('person_waiting_service__n6_29', 'person_waiting_service__n6_30'),
                                    ('person_waiting_service__n6_30', 'person_waiting_service__n6_31'),
                                    ('person_waiting_service__n6_31', 'person_waiting_service__n6_32'),
                                    ('person_waiting_service__n6_32', 'person_waiting_service__n6_33'),
                                    ('person_waiting_service__n6_33', 'person_waiting_service__n6_34'),
                                    ('person_waiting_service__n6_34', 'person_waiting_service__n6_35'),
                                    ('person_waiting_service__n6_35', 'person_waiting_service__n6_36'),
                                    ('person_waiting_service__n6_36', 'person_waiting_service__n6_37'),
                                    ('person_waiting_service__n6_37', 'person_waiting_service__n6_38'),
                                    ('person_waiting_service__n6_38', 'person_waiting_service__n6_39'),
                                    ('ambulance_at_node__a1_n6_0', 'ambulance_at_node__a1_n6_1'),
                                    ('ambulance_at_node__a1_n6_1', 'ambulance_at_node__a1_n6_2'),
                                    ('ambulance_at_node__a1_n6_2', 'ambulance_at_node__a1_n6_3'),
                                    ('ambulance_at_node__a1_n6_3', 'ambulance_at_node__a1_n6_4'),
                                    ('ambulance_at_node__a1_n6_4', 'ambulance_at_node__a1_n6_5'),
                                    ('ambulance_at_node__a1_n6_5', 'ambulance_at_node__a1_n6_6'),
                                    ('ambulance_at_node__a1_n6_6', 'ambulance_at_node__a1_n6_7'),
                                    ('ambulance_at_node__a1_n6_7', 'ambulance_at_node__a1_n6_8'),
                                    ('ambulance_at_node__a1_n6_8', 'ambulance_at_node__a1_n6_9'),
                                    ('ambulance_at_node__a1_n6_9', 'ambulance_at_node__a1_n6_10'),
                                    ('ambulance_at_node__a1_n6_10', 'ambulance_at_node__a1_n6_11'),
                                    ('ambulance_at_node__a1_n6_11', 'ambulance_at_node__a1_n6_12'),
                                    ('ambulance_at_node__a1_n6_12', 'ambulance_at_node__a1_n6_13'),
                                    ('ambulance_at_node__a1_n6_13', 'ambulance_at_node__a1_n6_14'),
                                    ('ambulance_at_node__a1_n6_14', 'ambulance_at_node__a1_n6_15'),
                                    ('ambulance_at_node__a1_n6_15', 'ambulance_at_node__a1_n6_16'),
                                    ('ambulance_at_node__a1_n6_16', 'ambulance_at_node__a1_n6_17'),
                                    ('ambulance_at_node__a1_n6_17', 'ambulance_at_node__a1_n6_18'),
                                    ('ambulance_at_node__a1_n6_18', 'ambulance_at_node__a1_n6_19'),
                                    ('ambulance_at_node__a1_n6_19', 'ambulance_at_node__a1_n6_20'),
                                    ('ambulance_at_node__a1_n6_20', 'ambulance_at_node__a1_n6_21'),
                                    ('ambulance_at_node__a1_n6_21', 'ambulance_at_node__a1_n6_22'),
                                    ('ambulance_at_node__a1_n6_22', 'ambulance_at_node__a1_n6_23'),
                                    ('ambulance_at_node__a1_n6_23', 'ambulance_at_node__a1_n6_24'),
                                    ('ambulance_at_node__a1_n6_24', 'ambulance_at_node__a1_n6_25'),
                                    ('ambulance_at_node__a1_n6_25', 'ambulance_at_node__a1_n6_26'),
                                    ('ambulance_at_node__a1_n6_26', 'ambulance_at_node__a1_n6_27'),
                                    ('ambulance_at_node__a1_n6_27', 'ambulance_at_node__a1_n6_28'),
                                    ('ambulance_at_node__a1_n6_28', 'ambulance_at_node__a1_n6_29'),
                                    ('ambulance_at_node__a1_n6_29', 'ambulance_at_node__a1_n6_30'),
                                    ('ambulance_at_node__a1_n6_30', 'ambulance_at_node__a1_n6_31'),
                                    ('ambulance_at_node__a1_n6_31', 'ambulance_at_node__a1_n6_32'),
                                    ('ambulance_at_node__a1_n6_32', 'ambulance_at_node__a1_n6_33'),
                                    ('ambulance_at_node__a1_n6_33', 'ambulance_at_node__a1_n6_34'),
                                    ('ambulance_at_node__a1_n6_34', 'ambulance_at_node__a1_n6_35'),
                                    ('ambulance_at_node__a1_n6_35', 'ambulance_at_node__a1_n6_36'),
                                    ('ambulance_at_node__a1_n6_36', 'ambulance_at_node__a1_n6_37'),
                                    ('ambulance_at_node__a1_n6_37', 'ambulance_at_node__a1_n6_38'),
                                    ('ambulance_at_node__a1_n6_38', 'ambulance_at_node__a1_n6_39'),
                                    ('ambulance_at_node__a1_n7_0', 'ambulance_at_node__a1_n7_1'),
                                    ('ambulance_at_node__a1_n7_1', 'ambulance_at_node__a1_n7_2'),
                                    ('ambulance_at_node__a1_n7_2', 'ambulance_at_node__a1_n7_3'),
                                    ('ambulance_at_node__a1_n7_3', 'ambulance_at_node__a1_n7_4'),
                                    ('ambulance_at_node__a1_n7_4', 'ambulance_at_node__a1_n7_5'),
                                    ('ambulance_at_node__a1_n7_5', 'ambulance_at_node__a1_n7_6'),
                                    ('ambulance_at_node__a1_n7_6', 'ambulance_at_node__a1_n7_7'),
                                    ('ambulance_at_node__a1_n7_7', 'ambulance_at_node__a1_n7_8'),
                                    ('ambulance_at_node__a1_n7_8', 'ambulance_at_node__a1_n7_9'),
                                    ('ambulance_at_node__a1_n7_9', 'ambulance_at_node__a1_n7_10'),
                                    ('ambulance_at_node__a1_n7_10', 'ambulance_at_node__a1_n7_11'),
                                    ('ambulance_at_node__a1_n7_11', 'ambulance_at_node__a1_n7_12'),
                                    ('ambulance_at_node__a1_n7_12', 'ambulance_at_node__a1_n7_13'),
                                    ('ambulance_at_node__a1_n7_13', 'ambulance_at_node__a1_n7_14'),
                                    ('ambulance_at_node__a1_n7_14', 'ambulance_at_node__a1_n7_15'),
                                    ('ambulance_at_node__a1_n7_15', 'ambulance_at_node__a1_n7_16'),
                                    ('ambulance_at_node__a1_n7_16', 'ambulance_at_node__a1_n7_17'),
                                    ('ambulance_at_node__a1_n7_17', 'ambulance_at_node__a1_n7_18'),
                                    ('ambulance_at_node__a1_n7_18', 'ambulance_at_node__a1_n7_19'),
                                    ('ambulance_at_node__a1_n7_19', 'ambulance_at_node__a1_n7_20'),
                                    ('ambulance_at_node__a1_n7_20', 'ambulance_at_node__a1_n7_21'),
                                    ('ambulance_at_node__a1_n7_21', 'ambulance_at_node__a1_n7_22'),
                                    ('ambulance_at_node__a1_n7_22', 'ambulance_at_node__a1_n7_23'),
                                    ('ambulance_at_node__a1_n7_23', 'ambulance_at_node__a1_n7_24'),
                                    ('ambulance_at_node__a1_n7_24', 'ambulance_at_node__a1_n7_25'),
                                    ('ambulance_at_node__a1_n7_25', 'ambulance_at_node__a1_n7_26'),
                                    ('ambulance_at_node__a1_n7_26', 'ambulance_at_node__a1_n7_27'),
                                    ('ambulance_at_node__a1_n7_27', 'ambulance_at_node__a1_n7_28'),
                                    ('ambulance_at_node__a1_n7_28', 'ambulance_at_node__a1_n7_29'),
                                    ('ambulance_at_node__a1_n7_29', 'ambulance_at_node__a1_n7_30'),
                                    ('ambulance_at_node__a1_n7_30', 'ambulance_at_node__a1_n7_31'),
                                    ('ambulance_at_node__a1_n7_31', 'ambulance_at_node__a1_n7_32'),
                                    ('ambulance_at_node__a1_n7_32', 'ambulance_at_node__a1_n7_33'),
                                    ('ambulance_at_node__a1_n7_33', 'ambulance_at_node__a1_n7_34'),
                                    ('ambulance_at_node__a1_n7_34', 'ambulance_at_node__a1_n7_35'),
                                    ('ambulance_at_node__a1_n7_35', 'ambulance_at_node__a1_n7_36'),
                                    ('ambulance_at_node__a1_n7_36', 'ambulance_at_node__a1_n7_37'),
                                    ('ambulance_at_node__a1_n7_37', 'ambulance_at_node__a1_n7_38'),
                                    ('ambulance_at_node__a1_n7_38', 'ambulance_at_node__a1_n7_39'),
                                    ('ambulance_at_node__a1_n8_0', 'ambulance_at_node__a1_n8_1'),
                                    ('ambulance_at_node__a1_n8_1', 'ambulance_at_node__a1_n8_2'),
                                    ('ambulance_at_node__a1_n8_2', 'ambulance_at_node__a1_n8_3'),
                                    ('ambulance_at_node__a1_n8_3', 'ambulance_at_node__a1_n8_4'),
                                    ('ambulance_at_node__a1_n8_4', 'ambulance_at_node__a1_n8_5'),
                                    ('ambulance_at_node__a1_n8_5', 'ambulance_at_node__a1_n8_6'),
                                    ('ambulance_at_node__a1_n8_6', 'ambulance_at_node__a1_n8_7'),
                                    ('ambulance_at_node__a1_n8_7', 'ambulance_at_node__a1_n8_8'),
                                    ('ambulance_at_node__a1_n8_8', 'ambulance_at_node__a1_n8_9'),
                                    ('ambulance_at_node__a1_n8_9', 'ambulance_at_node__a1_n8_10'),
                                    ('ambulance_at_node__a1_n8_10', 'ambulance_at_node__a1_n8_11'),
                                    ('ambulance_at_node__a1_n8_11', 'ambulance_at_node__a1_n8_12'),
                                    ('ambulance_at_node__a1_n8_12', 'ambulance_at_node__a1_n8_13'),
                                    ('ambulance_at_node__a1_n8_13', 'ambulance_at_node__a1_n8_14'),
                                    ('ambulance_at_node__a1_n8_14', 'ambulance_at_node__a1_n8_15'),
                                    ('ambulance_at_node__a1_n8_15', 'ambulance_at_node__a1_n8_16'),
                                    ('ambulance_at_node__a1_n8_16', 'ambulance_at_node__a1_n8_17'),
                                    ('ambulance_at_node__a1_n8_17', 'ambulance_at_node__a1_n8_18'),
                                    ('ambulance_at_node__a1_n8_18', 'ambulance_at_node__a1_n8_19'),
                                    ('ambulance_at_node__a1_n8_19', 'ambulance_at_node__a1_n8_20'),
                                    ('ambulance_at_node__a1_n8_20', 'ambulance_at_node__a1_n8_21'),
                                    ('ambulance_at_node__a1_n8_21', 'ambulance_at_node__a1_n8_22'),
                                    ('ambulance_at_node__a1_n8_22', 'ambulance_at_node__a1_n8_23'),
                                    ('ambulance_at_node__a1_n8_23', 'ambulance_at_node__a1_n8_24'),
                                    ('ambulance_at_node__a1_n8_24', 'ambulance_at_node__a1_n8_25'),
                                    ('ambulance_at_node__a1_n8_25', 'ambulance_at_node__a1_n8_26'),
                                    ('ambulance_at_node__a1_n8_26', 'ambulance_at_node__a1_n8_27'),
                                    ('ambulance_at_node__a1_n8_27', 'ambulance_at_node__a1_n8_28'),
                                    ('ambulance_at_node__a1_n8_28', 'ambulance_at_node__a1_n8_29'),
                                    ('ambulance_at_node__a1_n8_29', 'ambulance_at_node__a1_n8_30'),
                                    ('ambulance_at_node__a1_n8_30', 'ambulance_at_node__a1_n8_31'),
                                    ('ambulance_at_node__a1_n8_31', 'ambulance_at_node__a1_n8_32'),
                                    ('ambulance_at_node__a1_n8_32', 'ambulance_at_node__a1_n8_33'),
                                    ('ambulance_at_node__a1_n8_33', 'ambulance_at_node__a1_n8_34'),
                                    ('ambulance_at_node__a1_n8_34', 'ambulance_at_node__a1_n8_35'),
                                    ('ambulance_at_node__a1_n8_35', 'ambulance_at_node__a1_n8_36'),
                                    ('ambulance_at_node__a1_n8_36', 'ambulance_at_node__a1_n8_37'),
                                    ('ambulance_at_node__a1_n8_37', 'ambulance_at_node__a1_n8_38'),
                                    ('ambulance_at_node__a1_n8_38', 'ambulance_at_node__a1_n8_39'),
                                    ('ambulance_at_node__a1_n2_0', 'ambulance_at_node__a1_n2_1'),
                                    ('ambulance_at_node__a1_n2_1', 'ambulance_at_node__a1_n2_2'),
                                    ('ambulance_at_node__a1_n2_2', 'ambulance_at_node__a1_n2_3'),
                                    ('ambulance_at_node__a1_n2_3', 'ambulance_at_node__a1_n2_4'),
                                    ('ambulance_at_node__a1_n2_4', 'ambulance_at_node__a1_n2_5'),
                                    ('ambulance_at_node__a1_n2_5', 'ambulance_at_node__a1_n2_6'),
                                    ('ambulance_at_node__a1_n2_6', 'ambulance_at_node__a1_n2_7'),
                                    ('ambulance_at_node__a1_n2_7', 'ambulance_at_node__a1_n2_8'),
                                    ('ambulance_at_node__a1_n2_8', 'ambulance_at_node__a1_n2_9'),
                                    ('ambulance_at_node__a1_n2_9', 'ambulance_at_node__a1_n2_10'),
                                    ('ambulance_at_node__a1_n2_10', 'ambulance_at_node__a1_n2_11'),
                                    ('ambulance_at_node__a1_n2_11', 'ambulance_at_node__a1_n2_12'),
                                    ('ambulance_at_node__a1_n2_12', 'ambulance_at_node__a1_n2_13'),
                                    ('ambulance_at_node__a1_n2_13', 'ambulance_at_node__a1_n2_14'),
                                    ('ambulance_at_node__a1_n2_14', 'ambulance_at_node__a1_n2_15'),
                                    ('ambulance_at_node__a1_n2_15', 'ambulance_at_node__a1_n2_16'),
                                    ('ambulance_at_node__a1_n2_16', 'ambulance_at_node__a1_n2_17'),
                                    ('ambulance_at_node__a1_n2_17', 'ambulance_at_node__a1_n2_18'),
                                    ('ambulance_at_node__a1_n2_18', 'ambulance_at_node__a1_n2_19'),
                                    ('ambulance_at_node__a1_n2_19', 'ambulance_at_node__a1_n2_20'),
                                    ('ambulance_at_node__a1_n2_20', 'ambulance_at_node__a1_n2_21'),
                                    ('ambulance_at_node__a1_n2_21', 'ambulance_at_node__a1_n2_22'),
                                    ('ambulance_at_node__a1_n2_22', 'ambulance_at_node__a1_n2_23'),
                                    ('ambulance_at_node__a1_n2_23', 'ambulance_at_node__a1_n2_24'),
                                    ('ambulance_at_node__a1_n2_24', 'ambulance_at_node__a1_n2_25'),
                                    ('ambulance_at_node__a1_n2_25', 'ambulance_at_node__a1_n2_26'),
                                    ('ambulance_at_node__a1_n2_26', 'ambulance_at_node__a1_n2_27'),
                                    ('ambulance_at_node__a1_n2_27', 'ambulance_at_node__a1_n2_28'),
                                    ('ambulance_at_node__a1_n2_28', 'ambulance_at_node__a1_n2_29'),
                                    ('ambulance_at_node__a1_n2_29', 'ambulance_at_node__a1_n2_30'),
                                    ('ambulance_at_node__a1_n2_30', 'ambulance_at_node__a1_n2_31'),
                                    ('ambulance_at_node__a1_n2_31', 'ambulance_at_node__a1_n2_32'),
                                    ('ambulance_at_node__a1_n2_32', 'ambulance_at_node__a1_n2_33'),
                                    ('ambulance_at_node__a1_n2_33', 'ambulance_at_node__a1_n2_34'),
                                    ('ambulance_at_node__a1_n2_34', 'ambulance_at_node__a1_n2_35'),
                                    ('ambulance_at_node__a1_n2_35', 'ambulance_at_node__a1_n2_36'),
                                    ('ambulance_at_node__a1_n2_36', 'ambulance_at_node__a1_n2_37'),
                                    ('ambulance_at_node__a1_n2_37', 'ambulance_at_node__a1_n2_38'),
                                    ('ambulance_at_node__a1_n2_38', 'ambulance_at_node__a1_n2_39'),
                                    ('ambulance_at_node__a1_n3_0', 'ambulance_at_node__a1_n3_1'),
                                    ('ambulance_at_node__a1_n3_1', 'ambulance_at_node__a1_n3_2'),
                                    ('ambulance_at_node__a1_n3_2', 'ambulance_at_node__a1_n3_3'),
                                    ('ambulance_at_node__a1_n3_3', 'ambulance_at_node__a1_n3_4'),
                                    ('ambulance_at_node__a1_n3_4', 'ambulance_at_node__a1_n3_5'),
                                    ('ambulance_at_node__a1_n3_5', 'ambulance_at_node__a1_n3_6'),
                                    ('ambulance_at_node__a1_n3_6', 'ambulance_at_node__a1_n3_7'),
                                    ('ambulance_at_node__a1_n3_7', 'ambulance_at_node__a1_n3_8'),
                                    ('ambulance_at_node__a1_n3_8', 'ambulance_at_node__a1_n3_9'),
                                    ('ambulance_at_node__a1_n3_9', 'ambulance_at_node__a1_n3_10'),
                                    ('ambulance_at_node__a1_n3_10', 'ambulance_at_node__a1_n3_11'),
                                    ('ambulance_at_node__a1_n3_11', 'ambulance_at_node__a1_n3_12'),
                                    ('ambulance_at_node__a1_n3_12', 'ambulance_at_node__a1_n3_13'),
                                    ('ambulance_at_node__a1_n3_13', 'ambulance_at_node__a1_n3_14'),
                                    ('ambulance_at_node__a1_n3_14', 'ambulance_at_node__a1_n3_15'),
                                    ('ambulance_at_node__a1_n3_15', 'ambulance_at_node__a1_n3_16'),
                                    ('ambulance_at_node__a1_n3_16', 'ambulance_at_node__a1_n3_17'),
                                    ('ambulance_at_node__a1_n3_17', 'ambulance_at_node__a1_n3_18'),
                                    ('ambulance_at_node__a1_n3_18', 'ambulance_at_node__a1_n3_19'),
                                    ('ambulance_at_node__a1_n3_19', 'ambulance_at_node__a1_n3_20'),
                                    ('ambulance_at_node__a1_n3_20', 'ambulance_at_node__a1_n3_21'),
                                    ('ambulance_at_node__a1_n3_21', 'ambulance_at_node__a1_n3_22'),
                                    ('ambulance_at_node__a1_n3_22', 'ambulance_at_node__a1_n3_23'),
                                    ('ambulance_at_node__a1_n3_23', 'ambulance_at_node__a1_n3_24'),
                                    ('ambulance_at_node__a1_n3_24', 'ambulance_at_node__a1_n3_25'),
                                    ('ambulance_at_node__a1_n3_25', 'ambulance_at_node__a1_n3_26'),
                                    ('ambulance_at_node__a1_n3_26', 'ambulance_at_node__a1_n3_27'),
                                    ('ambulance_at_node__a1_n3_27', 'ambulance_at_node__a1_n3_28'),
                                    ('ambulance_at_node__a1_n3_28', 'ambulance_at_node__a1_n3_29'),
                                    ('ambulance_at_node__a1_n3_29', 'ambulance_at_node__a1_n3_30'),
                                    ('ambulance_at_node__a1_n3_30', 'ambulance_at_node__a1_n3_31'),
                                    ('ambulance_at_node__a1_n3_31', 'ambulance_at_node__a1_n3_32'),
                                    ('ambulance_at_node__a1_n3_32', 'ambulance_at_node__a1_n3_33'),
                                    ('ambulance_at_node__a1_n3_33', 'ambulance_at_node__a1_n3_34'),
                                    ('ambulance_at_node__a1_n3_34', 'ambulance_at_node__a1_n3_35'),
                                    ('ambulance_at_node__a1_n3_35', 'ambulance_at_node__a1_n3_36'),
                                    ('ambulance_at_node__a1_n3_36', 'ambulance_at_node__a1_n3_37'),
                                    ('ambulance_at_node__a1_n3_37', 'ambulance_at_node__a1_n3_38'),
                                    ('ambulance_at_node__a1_n3_38', 'ambulance_at_node__a1_n3_39'),
                                    ('ambulance_at_node__a1_n4_0', 'ambulance_at_node__a1_n4_1'),
                                    ('ambulance_at_node__a1_n4_1', 'ambulance_at_node__a1_n4_2'),
                                    ('ambulance_at_node__a1_n4_2', 'ambulance_at_node__a1_n4_3'),
                                    ('ambulance_at_node__a1_n4_3', 'ambulance_at_node__a1_n4_4'),
                                    ('ambulance_at_node__a1_n4_4', 'ambulance_at_node__a1_n4_5'),
                                    ('ambulance_at_node__a1_n4_5', 'ambulance_at_node__a1_n4_6'),
                                    ('ambulance_at_node__a1_n4_6', 'ambulance_at_node__a1_n4_7'),
                                    ('ambulance_at_node__a1_n4_7', 'ambulance_at_node__a1_n4_8'),
                                    ('ambulance_at_node__a1_n4_8', 'ambulance_at_node__a1_n4_9'),
                                    ('ambulance_at_node__a1_n4_9', 'ambulance_at_node__a1_n4_10'),
                                    ('ambulance_at_node__a1_n4_10', 'ambulance_at_node__a1_n4_11'),
                                    ('ambulance_at_node__a1_n4_11', 'ambulance_at_node__a1_n4_12'),
                                    ('ambulance_at_node__a1_n4_12', 'ambulance_at_node__a1_n4_13'),
                                    ('ambulance_at_node__a1_n4_13', 'ambulance_at_node__a1_n4_14'),
                                    ('ambulance_at_node__a1_n4_14', 'ambulance_at_node__a1_n4_15'),
                                    ('ambulance_at_node__a1_n4_15', 'ambulance_at_node__a1_n4_16'),
                                    ('ambulance_at_node__a1_n4_16', 'ambulance_at_node__a1_n4_17'),
                                    ('ambulance_at_node__a1_n4_17', 'ambulance_at_node__a1_n4_18'),
                                    ('ambulance_at_node__a1_n4_18', 'ambulance_at_node__a1_n4_19'),
                                    ('ambulance_at_node__a1_n4_19', 'ambulance_at_node__a1_n4_20'),
                                    ('ambulance_at_node__a1_n4_20', 'ambulance_at_node__a1_n4_21'),
                                    ('ambulance_at_node__a1_n4_21', 'ambulance_at_node__a1_n4_22'),
                                    ('ambulance_at_node__a1_n4_22', 'ambulance_at_node__a1_n4_23'),
                                    ('ambulance_at_node__a1_n4_23', 'ambulance_at_node__a1_n4_24'),
                                    ('ambulance_at_node__a1_n4_24', 'ambulance_at_node__a1_n4_25'),
                                    ('ambulance_at_node__a1_n4_25', 'ambulance_at_node__a1_n4_26'),
                                    ('ambulance_at_node__a1_n4_26', 'ambulance_at_node__a1_n4_27'),
                                    ('ambulance_at_node__a1_n4_27', 'ambulance_at_node__a1_n4_28'),
                                    ('ambulance_at_node__a1_n4_28', 'ambulance_at_node__a1_n4_29'),
                                    ('ambulance_at_node__a1_n4_29', 'ambulance_at_node__a1_n4_30'),
                                    ('ambulance_at_node__a1_n4_30', 'ambulance_at_node__a1_n4_31'),
                                    ('ambulance_at_node__a1_n4_31', 'ambulance_at_node__a1_n4_32'),
                                    ('ambulance_at_node__a1_n4_32', 'ambulance_at_node__a1_n4_33'),
                                    ('ambulance_at_node__a1_n4_33', 'ambulance_at_node__a1_n4_34'),
                                    ('ambulance_at_node__a1_n4_34', 'ambulance_at_node__a1_n4_35'),
                                    ('ambulance_at_node__a1_n4_35', 'ambulance_at_node__a1_n4_36'),
                                    ('ambulance_at_node__a1_n4_36', 'ambulance_at_node__a1_n4_37'),
                                    ('ambulance_at_node__a1_n4_37', 'ambulance_at_node__a1_n4_38'),
                                    ('ambulance_at_node__a1_n4_38', 'ambulance_at_node__a1_n4_39'),
                                    ('ambulance_at_node__a1_n5_0', 'ambulance_at_node__a1_n5_1'),
                                    ('ambulance_at_node__a1_n5_1', 'ambulance_at_node__a1_n5_2'),
                                    ('ambulance_at_node__a1_n5_2', 'ambulance_at_node__a1_n5_3'),
                                    ('ambulance_at_node__a1_n5_3', 'ambulance_at_node__a1_n5_4'),
                                    ('ambulance_at_node__a1_n5_4', 'ambulance_at_node__a1_n5_5'),
                                    ('ambulance_at_node__a1_n5_5', 'ambulance_at_node__a1_n5_6'),
                                    ('ambulance_at_node__a1_n5_6', 'ambulance_at_node__a1_n5_7'),
                                    ('ambulance_at_node__a1_n5_7', 'ambulance_at_node__a1_n5_8'),
                                    ('ambulance_at_node__a1_n5_8', 'ambulance_at_node__a1_n5_9'),
                                    ('ambulance_at_node__a1_n5_9', 'ambulance_at_node__a1_n5_10'),
                                    ('ambulance_at_node__a1_n5_10', 'ambulance_at_node__a1_n5_11'),
                                    ('ambulance_at_node__a1_n5_11', 'ambulance_at_node__a1_n5_12'),
                                    ('ambulance_at_node__a1_n5_12', 'ambulance_at_node__a1_n5_13'),
                                    ('ambulance_at_node__a1_n5_13', 'ambulance_at_node__a1_n5_14'),
                                    ('ambulance_at_node__a1_n5_14', 'ambulance_at_node__a1_n5_15'),
                                    ('ambulance_at_node__a1_n5_15', 'ambulance_at_node__a1_n5_16'),
                                    ('ambulance_at_node__a1_n5_16', 'ambulance_at_node__a1_n5_17'),
                                    ('ambulance_at_node__a1_n5_17', 'ambulance_at_node__a1_n5_18'),
                                    ('ambulance_at_node__a1_n5_18', 'ambulance_at_node__a1_n5_19'),
                                    ('ambulance_at_node__a1_n5_19', 'ambulance_at_node__a1_n5_20'),
                                    ('ambulance_at_node__a1_n5_20', 'ambulance_at_node__a1_n5_21'),
                                    ('ambulance_at_node__a1_n5_21', 'ambulance_at_node__a1_n5_22'),
                                    ('ambulance_at_node__a1_n5_22', 'ambulance_at_node__a1_n5_23'),
                                    ('ambulance_at_node__a1_n5_23', 'ambulance_at_node__a1_n5_24'),
                                    ('ambulance_at_node__a1_n5_24', 'ambulance_at_node__a1_n5_25'),
                                    ('ambulance_at_node__a1_n5_25', 'ambulance_at_node__a1_n5_26'),
                                    ('ambulance_at_node__a1_n5_26', 'ambulance_at_node__a1_n5_27'),
                                    ('ambulance_at_node__a1_n5_27', 'ambulance_at_node__a1_n5_28'),
                                    ('ambulance_at_node__a1_n5_28', 'ambulance_at_node__a1_n5_29'),
                                    ('ambulance_at_node__a1_n5_29', 'ambulance_at_node__a1_n5_30'),
                                    ('ambulance_at_node__a1_n5_30', 'ambulance_at_node__a1_n5_31'),
                                    ('ambulance_at_node__a1_n5_31', 'ambulance_at_node__a1_n5_32'),
                                    ('ambulance_at_node__a1_n5_32', 'ambulance_at_node__a1_n5_33'),
                                    ('ambulance_at_node__a1_n5_33', 'ambulance_at_node__a1_n5_34'),
                                    ('ambulance_at_node__a1_n5_34', 'ambulance_at_node__a1_n5_35'),
                                    ('ambulance_at_node__a1_n5_35', 'ambulance_at_node__a1_n5_36'),
                                    ('ambulance_at_node__a1_n5_36', 'ambulance_at_node__a1_n5_37'),
                                    ('ambulance_at_node__a1_n5_37', 'ambulance_at_node__a1_n5_38'),
                                    ('ambulance_at_node__a1_n5_38', 'ambulance_at_node__a1_n5_39'),
                                    ('ambulance_at_node__a1_n0_0', 'ambulance_at_node__a1_n0_1'),
                                    ('ambulance_at_node__a1_n0_1', 'ambulance_at_node__a1_n0_2'),
                                    ('ambulance_at_node__a1_n0_2', 'ambulance_at_node__a1_n0_3'),
                                    ('ambulance_at_node__a1_n0_3', 'ambulance_at_node__a1_n0_4'),
                                    ('ambulance_at_node__a1_n0_4', 'ambulance_at_node__a1_n0_5'),
                                    ('ambulance_at_node__a1_n0_5', 'ambulance_at_node__a1_n0_6'),
                                    ('ambulance_at_node__a1_n0_6', 'ambulance_at_node__a1_n0_7'),
                                    ('ambulance_at_node__a1_n0_7', 'ambulance_at_node__a1_n0_8'),
                                    ('ambulance_at_node__a1_n0_8', 'ambulance_at_node__a1_n0_9'),
                                    ('ambulance_at_node__a1_n0_9', 'ambulance_at_node__a1_n0_10'),
                                    ('ambulance_at_node__a1_n0_10', 'ambulance_at_node__a1_n0_11'),
                                    ('ambulance_at_node__a1_n0_11', 'ambulance_at_node__a1_n0_12'),
                                    ('ambulance_at_node__a1_n0_12', 'ambulance_at_node__a1_n0_13'),
                                    ('ambulance_at_node__a1_n0_13', 'ambulance_at_node__a1_n0_14'),
                                    ('ambulance_at_node__a1_n0_14', 'ambulance_at_node__a1_n0_15'),
                                    ('ambulance_at_node__a1_n0_15', 'ambulance_at_node__a1_n0_16'),
                                    ('ambulance_at_node__a1_n0_16', 'ambulance_at_node__a1_n0_17'),
                                    ('ambulance_at_node__a1_n0_17', 'ambulance_at_node__a1_n0_18'),
                                    ('ambulance_at_node__a1_n0_18', 'ambulance_at_node__a1_n0_19'),
                                    ('ambulance_at_node__a1_n0_19', 'ambulance_at_node__a1_n0_20'),
                                    ('ambulance_at_node__a1_n0_20', 'ambulance_at_node__a1_n0_21'),
                                    ('ambulance_at_node__a1_n0_21', 'ambulance_at_node__a1_n0_22'),
                                    ('ambulance_at_node__a1_n0_22', 'ambulance_at_node__a1_n0_23'),
                                    ('ambulance_at_node__a1_n0_23', 'ambulance_at_node__a1_n0_24'),
                                    ('ambulance_at_node__a1_n0_24', 'ambulance_at_node__a1_n0_25'),
                                    ('ambulance_at_node__a1_n0_25', 'ambulance_at_node__a1_n0_26'),
                                    ('ambulance_at_node__a1_n0_26', 'ambulance_at_node__a1_n0_27'),
                                    ('ambulance_at_node__a1_n0_27', 'ambulance_at_node__a1_n0_28'),
                                    ('ambulance_at_node__a1_n0_28', 'ambulance_at_node__a1_n0_29'),
                                    ('ambulance_at_node__a1_n0_29', 'ambulance_at_node__a1_n0_30'),
                                    ('ambulance_at_node__a1_n0_30', 'ambulance_at_node__a1_n0_31'),
                                    ('ambulance_at_node__a1_n0_31', 'ambulance_at_node__a1_n0_32'),
                                    ('ambulance_at_node__a1_n0_32', 'ambulance_at_node__a1_n0_33'),
                                    ('ambulance_at_node__a1_n0_33', 'ambulance_at_node__a1_n0_34'),
                                    ('ambulance_at_node__a1_n0_34', 'ambulance_at_node__a1_n0_35'),
                                    ('ambulance_at_node__a1_n0_35', 'ambulance_at_node__a1_n0_36'),
                                    ('ambulance_at_node__a1_n0_36', 'ambulance_at_node__a1_n0_37'),
                                    ('ambulance_at_node__a1_n0_37', 'ambulance_at_node__a1_n0_38'),
                                    ('ambulance_at_node__a1_n0_38', 'ambulance_at_node__a1_n0_39'),
                                    ('ambulance_at_node__a1_n1_0', 'ambulance_at_node__a1_n1_1'),
                                    ('ambulance_at_node__a1_n1_1', 'ambulance_at_node__a1_n1_2'),
                                    ('ambulance_at_node__a1_n1_2', 'ambulance_at_node__a1_n1_3'),
                                    ('ambulance_at_node__a1_n1_3', 'ambulance_at_node__a1_n1_4'),
                                    ('ambulance_at_node__a1_n1_4', 'ambulance_at_node__a1_n1_5'),
                                    ('ambulance_at_node__a1_n1_5', 'ambulance_at_node__a1_n1_6'),
                                    ('ambulance_at_node__a1_n1_6', 'ambulance_at_node__a1_n1_7'),
                                    ('ambulance_at_node__a1_n1_7', 'ambulance_at_node__a1_n1_8'),
                                    ('ambulance_at_node__a1_n1_8', 'ambulance_at_node__a1_n1_9'),
                                    ('ambulance_at_node__a1_n1_9', 'ambulance_at_node__a1_n1_10'),
                                    ('ambulance_at_node__a1_n1_10', 'ambulance_at_node__a1_n1_11'),
                                    ('ambulance_at_node__a1_n1_11', 'ambulance_at_node__a1_n1_12'),
                                    ('ambulance_at_node__a1_n1_12', 'ambulance_at_node__a1_n1_13'),
                                    ('ambulance_at_node__a1_n1_13', 'ambulance_at_node__a1_n1_14'),
                                    ('ambulance_at_node__a1_n1_14', 'ambulance_at_node__a1_n1_15'),
                                    ('ambulance_at_node__a1_n1_15', 'ambulance_at_node__a1_n1_16'),
                                    ('ambulance_at_node__a1_n1_16', 'ambulance_at_node__a1_n1_17'),
                                    ('ambulance_at_node__a1_n1_17', 'ambulance_at_node__a1_n1_18'),
                                    ('ambulance_at_node__a1_n1_18', 'ambulance_at_node__a1_n1_19'),
                                    ('ambulance_at_node__a1_n1_19', 'ambulance_at_node__a1_n1_20'),
                                    ('ambulance_at_node__a1_n1_20', 'ambulance_at_node__a1_n1_21'),
                                    ('ambulance_at_node__a1_n1_21', 'ambulance_at_node__a1_n1_22'),
                                    ('ambulance_at_node__a1_n1_22', 'ambulance_at_node__a1_n1_23'),
                                    ('ambulance_at_node__a1_n1_23', 'ambulance_at_node__a1_n1_24'),
                                    ('ambulance_at_node__a1_n1_24', 'ambulance_at_node__a1_n1_25'),
                                    ('ambulance_at_node__a1_n1_25', 'ambulance_at_node__a1_n1_26'),
                                    ('ambulance_at_node__a1_n1_26', 'ambulance_at_node__a1_n1_27'),
                                    ('ambulance_at_node__a1_n1_27', 'ambulance_at_node__a1_n1_28'),
                                    ('ambulance_at_node__a1_n1_28', 'ambulance_at_node__a1_n1_29'),
                                    ('ambulance_at_node__a1_n1_29', 'ambulance_at_node__a1_n1_30'),
                                    ('ambulance_at_node__a1_n1_30', 'ambulance_at_node__a1_n1_31'),
                                    ('ambulance_at_node__a1_n1_31', 'ambulance_at_node__a1_n1_32'),
                                    ('ambulance_at_node__a1_n1_32', 'ambulance_at_node__a1_n1_33'),
                                    ('ambulance_at_node__a1_n1_33', 'ambulance_at_node__a1_n1_34'),
                                    ('ambulance_at_node__a1_n1_34', 'ambulance_at_node__a1_n1_35'),
                                    ('ambulance_at_node__a1_n1_35', 'ambulance_at_node__a1_n1_36'),
                                    ('ambulance_at_node__a1_n1_36', 'ambulance_at_node__a1_n1_37'),
                                    ('ambulance_at_node__a1_n1_37', 'ambulance_at_node__a1_n1_38'),
                                    ('ambulance_at_node__a1_n1_38', 'ambulance_at_node__a1_n1_39')]);

cpd_person_in_ambulance__a0_0 = TabularCPD ('person_in_ambulance__a0_0', 2, [[1.0], [0.0]]);
cpd_person_in_ambulance__a1_0 = TabularCPD ('person_in_ambulance__a1_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_0 = TabularCPD ('ambulance_at_node__a0_n0_0', 2, [[0.0], [1.0]]);
cpd_ambulance_at_node__a0_n1_0 = TabularCPD ('ambulance_at_node__a0_n1_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_0 = TabularCPD ('ambulance_at_node__a0_n2_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n3_0 = TabularCPD ('ambulance_at_node__a0_n3_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_0 = TabularCPD ('ambulance_at_node__a0_n4_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n5_0 = TabularCPD ('ambulance_at_node__a0_n5_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n6_0 = TabularCPD ('ambulance_at_node__a0_n6_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n7_0 = TabularCPD ('ambulance_at_node__a0_n7_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n8_0 = TabularCPD ('ambulance_at_node__a0_n8_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n0_0 = TabularCPD ('ambulance_at_node__a1_n0_0', 2, [[0.0], [1.0]]);
cpd_ambulance_at_node__a1_n1_0 = TabularCPD ('ambulance_at_node__a1_n1_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n2_0 = TabularCPD ('ambulance_at_node__a1_n2_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n3_0 = TabularCPD ('ambulance_at_node__a1_n3_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n4_0 = TabularCPD ('ambulance_at_node__a1_n4_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n5_0 = TabularCPD ('ambulance_at_node__a1_n5_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n6_0 = TabularCPD ('ambulance_at_node__a1_n6_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n7_0 = TabularCPD ('ambulance_at_node__a1_n7_0', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a1_n8_0 = TabularCPD ('ambulance_at_node__a1_n8_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n0_0 = TabularCPD ('person_waiting_service__n0_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n1_0 = TabularCPD ('person_waiting_service__n1_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n2_0 = TabularCPD ('person_waiting_service__n2_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n3_0 = TabularCPD ('person_waiting_service__n3_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n4_0 = TabularCPD ('person_waiting_service__n4_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n5_0 = TabularCPD ('person_waiting_service__n5_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n6_0 = TabularCPD ('person_waiting_service__n6_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n7_0 = TabularCPD ('person_waiting_service__n7_0', 2, [[1.0], [0.0]]);
cpd_person_waiting_service__n8_0 = TabularCPD ('person_waiting_service__n8_0', 2, [[1.0], [0.0]]);

cpd_person_in_ambulance__a0_1 = TabularCPD ('person_in_ambulance__a0_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_0'], [2]);
cpd_person_in_ambulance__a0_2 = TabularCPD ('person_in_ambulance__a0_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_1'], [2]);
cpd_person_in_ambulance__a0_3 = TabularCPD ('person_in_ambulance__a0_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_2'], [2]);
cpd_person_in_ambulance__a0_4 = TabularCPD ('person_in_ambulance__a0_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_3'], [2]);
cpd_person_in_ambulance__a0_5 = TabularCPD ('person_in_ambulance__a0_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_4'], [2]);
cpd_person_in_ambulance__a0_6 = TabularCPD ('person_in_ambulance__a0_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_5'], [2]);
cpd_person_in_ambulance__a0_7 = TabularCPD ('person_in_ambulance__a0_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_6'], [2]);
cpd_person_in_ambulance__a0_8 = TabularCPD ('person_in_ambulance__a0_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_7'], [2]);
cpd_person_in_ambulance__a0_9 = TabularCPD ('person_in_ambulance__a0_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_8'], [2]);
cpd_person_in_ambulance__a0_10 = TabularCPD ('person_in_ambulance__a0_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_9'], [2]);
cpd_person_in_ambulance__a0_11 = TabularCPD ('person_in_ambulance__a0_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_10'], [2]);
cpd_person_in_ambulance__a0_12 = TabularCPD ('person_in_ambulance__a0_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_11'], [2]);
cpd_person_in_ambulance__a0_13 = TabularCPD ('person_in_ambulance__a0_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_12'], [2]);
cpd_person_in_ambulance__a0_14 = TabularCPD ('person_in_ambulance__a0_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_13'], [2]);
cpd_person_in_ambulance__a0_15 = TabularCPD ('person_in_ambulance__a0_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_14'], [2]);
cpd_person_in_ambulance__a0_16 = TabularCPD ('person_in_ambulance__a0_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_15'], [2]);
cpd_person_in_ambulance__a0_17 = TabularCPD ('person_in_ambulance__a0_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_16'], [2]);
cpd_person_in_ambulance__a0_18 = TabularCPD ('person_in_ambulance__a0_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_17'], [2]);
cpd_person_in_ambulance__a0_19 = TabularCPD ('person_in_ambulance__a0_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_18'], [2]);
cpd_person_in_ambulance__a0_20 = TabularCPD ('person_in_ambulance__a0_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_19'], [2]);
cpd_person_in_ambulance__a0_21 = TabularCPD ('person_in_ambulance__a0_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_20'], [2]);
cpd_person_in_ambulance__a0_22 = TabularCPD ('person_in_ambulance__a0_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_21'], [2]);
cpd_person_in_ambulance__a0_23 = TabularCPD ('person_in_ambulance__a0_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_22'], [2]);
cpd_person_in_ambulance__a0_24 = TabularCPD ('person_in_ambulance__a0_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_23'], [2]);
cpd_person_in_ambulance__a0_25 = TabularCPD ('person_in_ambulance__a0_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_24'], [2]);
cpd_person_in_ambulance__a0_26 = TabularCPD ('person_in_ambulance__a0_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_25'], [2]);
cpd_person_in_ambulance__a0_27 = TabularCPD ('person_in_ambulance__a0_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_26'], [2]);
cpd_person_in_ambulance__a0_28 = TabularCPD ('person_in_ambulance__a0_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_27'], [2]);
cpd_person_in_ambulance__a0_29 = TabularCPD ('person_in_ambulance__a0_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_28'], [2]);
cpd_person_in_ambulance__a0_30 = TabularCPD ('person_in_ambulance__a0_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_29'], [2]);
cpd_person_in_ambulance__a0_31 = TabularCPD ('person_in_ambulance__a0_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_30'], [2]);
cpd_person_in_ambulance__a0_32 = TabularCPD ('person_in_ambulance__a0_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_31'], [2]);
cpd_person_in_ambulance__a0_33 = TabularCPD ('person_in_ambulance__a0_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_32'], [2]);
cpd_person_in_ambulance__a0_34 = TabularCPD ('person_in_ambulance__a0_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_33'], [2]);
cpd_person_in_ambulance__a0_35 = TabularCPD ('person_in_ambulance__a0_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_34'], [2]);
cpd_person_in_ambulance__a0_36 = TabularCPD ('person_in_ambulance__a0_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_35'], [2]);
cpd_person_in_ambulance__a0_37 = TabularCPD ('person_in_ambulance__a0_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_36'], [2]);
cpd_person_in_ambulance__a0_38 = TabularCPD ('person_in_ambulance__a0_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_37'], [2]);
cpd_person_in_ambulance__a0_39 = TabularCPD ('person_in_ambulance__a0_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a0_38'], [2]);

cpd_person_in_ambulance__a1_1 = TabularCPD ('person_in_ambulance__a1_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_0'], [2]);
cpd_person_in_ambulance__a1_2 = TabularCPD ('person_in_ambulance__a1_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_1'], [2]);
cpd_person_in_ambulance__a1_3 = TabularCPD ('person_in_ambulance__a1_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_2'], [2]);
cpd_person_in_ambulance__a1_4 = TabularCPD ('person_in_ambulance__a1_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_3'], [2]);
cpd_person_in_ambulance__a1_5 = TabularCPD ('person_in_ambulance__a1_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_4'], [2]);
cpd_person_in_ambulance__a1_6 = TabularCPD ('person_in_ambulance__a1_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_5'], [2]);
cpd_person_in_ambulance__a1_7 = TabularCPD ('person_in_ambulance__a1_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_6'], [2]);
cpd_person_in_ambulance__a1_8 = TabularCPD ('person_in_ambulance__a1_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_7'], [2]);
cpd_person_in_ambulance__a1_9 = TabularCPD ('person_in_ambulance__a1_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_8'], [2]);
cpd_person_in_ambulance__a1_10 = TabularCPD ('person_in_ambulance__a1_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_9'], [2]);
cpd_person_in_ambulance__a1_11 = TabularCPD ('person_in_ambulance__a1_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_10'], [2]);
cpd_person_in_ambulance__a1_12 = TabularCPD ('person_in_ambulance__a1_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_11'], [2]);
cpd_person_in_ambulance__a1_13 = TabularCPD ('person_in_ambulance__a1_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_12'], [2]);
cpd_person_in_ambulance__a1_14 = TabularCPD ('person_in_ambulance__a1_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_13'], [2]);
cpd_person_in_ambulance__a1_15 = TabularCPD ('person_in_ambulance__a1_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_14'], [2]);
cpd_person_in_ambulance__a1_16 = TabularCPD ('person_in_ambulance__a1_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_15'], [2]);
cpd_person_in_ambulance__a1_17 = TabularCPD ('person_in_ambulance__a1_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_16'], [2]);
cpd_person_in_ambulance__a1_18 = TabularCPD ('person_in_ambulance__a1_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_17'], [2]);
cpd_person_in_ambulance__a1_19 = TabularCPD ('person_in_ambulance__a1_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_18'], [2]);
cpd_person_in_ambulance__a1_20 = TabularCPD ('person_in_ambulance__a1_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_19'], [2]);
cpd_person_in_ambulance__a1_21 = TabularCPD ('person_in_ambulance__a1_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_20'], [2]);
cpd_person_in_ambulance__a1_22 = TabularCPD ('person_in_ambulance__a1_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_21'], [2]);
cpd_person_in_ambulance__a1_23 = TabularCPD ('person_in_ambulance__a1_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_22'], [2]);
cpd_person_in_ambulance__a1_24 = TabularCPD ('person_in_ambulance__a1_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_23'], [2]);
cpd_person_in_ambulance__a1_25 = TabularCPD ('person_in_ambulance__a1_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_24'], [2]);
cpd_person_in_ambulance__a1_26 = TabularCPD ('person_in_ambulance__a1_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_25'], [2]);
cpd_person_in_ambulance__a1_27 = TabularCPD ('person_in_ambulance__a1_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_26'], [2]);
cpd_person_in_ambulance__a1_28 = TabularCPD ('person_in_ambulance__a1_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_27'], [2]);
cpd_person_in_ambulance__a1_29 = TabularCPD ('person_in_ambulance__a1_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_28'], [2]);
cpd_person_in_ambulance__a1_30 = TabularCPD ('person_in_ambulance__a1_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_29'], [2]);
cpd_person_in_ambulance__a1_31 = TabularCPD ('person_in_ambulance__a1_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_30'], [2]);
cpd_person_in_ambulance__a1_32 = TabularCPD ('person_in_ambulance__a1_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_31'], [2]);
cpd_person_in_ambulance__a1_33 = TabularCPD ('person_in_ambulance__a1_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_32'], [2]);
cpd_person_in_ambulance__a1_34 = TabularCPD ('person_in_ambulance__a1_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_33'], [2]);
cpd_person_in_ambulance__a1_35 = TabularCPD ('person_in_ambulance__a1_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_34'], [2]);
cpd_person_in_ambulance__a1_36 = TabularCPD ('person_in_ambulance__a1_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_35'], [2]);
cpd_person_in_ambulance__a1_37 = TabularCPD ('person_in_ambulance__a1_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_36'], [2]);
cpd_person_in_ambulance__a1_38 = TabularCPD ('person_in_ambulance__a1_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_37'], [2]);
cpd_person_in_ambulance__a1_39 = TabularCPD ('person_in_ambulance__a1_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_in_ambulance__a1_38'], [2]);

cpd_ambulance_at_node__a0_n4_1 = TabularCPD ('ambulance_at_node__a0_n4_1', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_2 = TabularCPD ('ambulance_at_node__a0_n4_2', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_3 = TabularCPD ('ambulance_at_node__a0_n4_3', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_4 = TabularCPD ('ambulance_at_node__a0_n4_4', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_5 = TabularCPD ('ambulance_at_node__a0_n4_5', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_6 = TabularCPD ('ambulance_at_node__a0_n4_6', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_7 = TabularCPD ('ambulance_at_node__a0_n4_7', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_8 = TabularCPD ('ambulance_at_node__a0_n4_8', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_9 = TabularCPD ('ambulance_at_node__a0_n4_9', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_10 = TabularCPD ('ambulance_at_node__a0_n4_10', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_11 = TabularCPD ('ambulance_at_node__a0_n4_11', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_12 = TabularCPD ('ambulance_at_node__a0_n4_12', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_13 = TabularCPD ('ambulance_at_node__a0_n4_13', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_14 = TabularCPD ('ambulance_at_node__a0_n4_14', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_15 = TabularCPD ('ambulance_at_node__a0_n4_15', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_16 = TabularCPD ('ambulance_at_node__a0_n4_16', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_17 = TabularCPD ('ambulance_at_node__a0_n4_17', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_18 = TabularCPD ('ambulance_at_node__a0_n4_18', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_19 = TabularCPD ('ambulance_at_node__a0_n4_19', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_20 = TabularCPD ('ambulance_at_node__a0_n4_20', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_21 = TabularCPD ('ambulance_at_node__a0_n4_21', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_22 = TabularCPD ('ambulance_at_node__a0_n4_22', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_23 = TabularCPD ('ambulance_at_node__a0_n4_23', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_24 = TabularCPD ('ambulance_at_node__a0_n4_24', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_25 = TabularCPD ('ambulance_at_node__a0_n4_25', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_26 = TabularCPD ('ambulance_at_node__a0_n4_26', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_27 = TabularCPD ('ambulance_at_node__a0_n4_27', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_28 = TabularCPD ('ambulance_at_node__a0_n4_28', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_29 = TabularCPD ('ambulance_at_node__a0_n4_29', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_30 = TabularCPD ('ambulance_at_node__a0_n4_30', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_31 = TabularCPD ('ambulance_at_node__a0_n4_31', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_32 = TabularCPD ('ambulance_at_node__a0_n4_32', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_33 = TabularCPD ('ambulance_at_node__a0_n4_33', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_34 = TabularCPD ('ambulance_at_node__a0_n4_34', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_35 = TabularCPD ('ambulance_at_node__a0_n4_35', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_36 = TabularCPD ('ambulance_at_node__a0_n4_36', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_37 = TabularCPD ('ambulance_at_node__a0_n4_37', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_38 = TabularCPD ('ambulance_at_node__a0_n4_38', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n4_39 = TabularCPD ('ambulance_at_node__a0_n4_39', 2, [[1.0], [0.0]]);

cpd_ambulance_at_node__a0_n3_1 = TabularCPD ('ambulance_at_node__a0_n3_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_0'], [2]);
cpd_ambulance_at_node__a0_n3_2 = TabularCPD ('ambulance_at_node__a0_n3_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_1'], [2]);
cpd_ambulance_at_node__a0_n3_3 = TabularCPD ('ambulance_at_node__a0_n3_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_2'], [2]);
cpd_ambulance_at_node__a0_n3_4 = TabularCPD ('ambulance_at_node__a0_n3_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_3'], [2]);
cpd_ambulance_at_node__a0_n3_5 = TabularCPD ('ambulance_at_node__a0_n3_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_4'], [2]);
cpd_ambulance_at_node__a0_n3_6 = TabularCPD ('ambulance_at_node__a0_n3_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_5'], [2]);
cpd_ambulance_at_node__a0_n3_7 = TabularCPD ('ambulance_at_node__a0_n3_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_6'], [2]);
cpd_ambulance_at_node__a0_n3_8 = TabularCPD ('ambulance_at_node__a0_n3_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_7'], [2]);
cpd_ambulance_at_node__a0_n3_9 = TabularCPD ('ambulance_at_node__a0_n3_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_8'], [2]);
cpd_ambulance_at_node__a0_n3_10 = TabularCPD ('ambulance_at_node__a0_n3_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_9'], [2]);
cpd_ambulance_at_node__a0_n3_11 = TabularCPD ('ambulance_at_node__a0_n3_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_10'], [2]);
cpd_ambulance_at_node__a0_n3_12 = TabularCPD ('ambulance_at_node__a0_n3_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_11'], [2]);
cpd_ambulance_at_node__a0_n3_13 = TabularCPD ('ambulance_at_node__a0_n3_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_12'], [2]);
cpd_ambulance_at_node__a0_n3_14 = TabularCPD ('ambulance_at_node__a0_n3_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_13'], [2]);
cpd_ambulance_at_node__a0_n3_15 = TabularCPD ('ambulance_at_node__a0_n3_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_14'], [2]);
cpd_ambulance_at_node__a0_n3_16 = TabularCPD ('ambulance_at_node__a0_n3_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_15'], [2]);
cpd_ambulance_at_node__a0_n3_17 = TabularCPD ('ambulance_at_node__a0_n3_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_16'], [2]);
cpd_ambulance_at_node__a0_n3_18 = TabularCPD ('ambulance_at_node__a0_n3_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_17'], [2]);
cpd_ambulance_at_node__a0_n3_19 = TabularCPD ('ambulance_at_node__a0_n3_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_18'], [2]);
cpd_ambulance_at_node__a0_n3_20 = TabularCPD ('ambulance_at_node__a0_n3_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_19'], [2]);
cpd_ambulance_at_node__a0_n3_21 = TabularCPD ('ambulance_at_node__a0_n3_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_20'], [2]);
cpd_ambulance_at_node__a0_n3_22 = TabularCPD ('ambulance_at_node__a0_n3_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_21'], [2]);
cpd_ambulance_at_node__a0_n3_23 = TabularCPD ('ambulance_at_node__a0_n3_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_22'], [2]);
cpd_ambulance_at_node__a0_n3_24 = TabularCPD ('ambulance_at_node__a0_n3_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_23'], [2]);
cpd_ambulance_at_node__a0_n3_25 = TabularCPD ('ambulance_at_node__a0_n3_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_24'], [2]);
cpd_ambulance_at_node__a0_n3_26 = TabularCPD ('ambulance_at_node__a0_n3_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_25'], [2]);
cpd_ambulance_at_node__a0_n3_27 = TabularCPD ('ambulance_at_node__a0_n3_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_26'], [2]);
cpd_ambulance_at_node__a0_n3_28 = TabularCPD ('ambulance_at_node__a0_n3_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_27'], [2]);
cpd_ambulance_at_node__a0_n3_29 = TabularCPD ('ambulance_at_node__a0_n3_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_28'], [2]);
cpd_ambulance_at_node__a0_n3_30 = TabularCPD ('ambulance_at_node__a0_n3_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_29'], [2]);
cpd_ambulance_at_node__a0_n3_31 = TabularCPD ('ambulance_at_node__a0_n3_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_30'], [2]);
cpd_ambulance_at_node__a0_n3_32 = TabularCPD ('ambulance_at_node__a0_n3_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_31'], [2]);
cpd_ambulance_at_node__a0_n3_33 = TabularCPD ('ambulance_at_node__a0_n3_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_32'], [2]);
cpd_ambulance_at_node__a0_n3_34 = TabularCPD ('ambulance_at_node__a0_n3_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_33'], [2]);
cpd_ambulance_at_node__a0_n3_35 = TabularCPD ('ambulance_at_node__a0_n3_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_34'], [2]);
cpd_ambulance_at_node__a0_n3_36 = TabularCPD ('ambulance_at_node__a0_n3_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_35'], [2]);
cpd_ambulance_at_node__a0_n3_37 = TabularCPD ('ambulance_at_node__a0_n3_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_36'], [2]);
cpd_ambulance_at_node__a0_n3_38 = TabularCPD ('ambulance_at_node__a0_n3_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_37'], [2]);
cpd_ambulance_at_node__a0_n3_39 = TabularCPD ('ambulance_at_node__a0_n3_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n3_38'], [2]);

cpd_ambulance_at_node__a0_n2_1 = TabularCPD ('ambulance_at_node__a0_n2_1', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_2 = TabularCPD ('ambulance_at_node__a0_n2_2', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_3 = TabularCPD ('ambulance_at_node__a0_n2_3', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_4 = TabularCPD ('ambulance_at_node__a0_n2_4', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_5 = TabularCPD ('ambulance_at_node__a0_n2_5', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_6 = TabularCPD ('ambulance_at_node__a0_n2_6', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_7 = TabularCPD ('ambulance_at_node__a0_n2_7', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_8 = TabularCPD ('ambulance_at_node__a0_n2_8', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_9 = TabularCPD ('ambulance_at_node__a0_n2_9', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_10 = TabularCPD ('ambulance_at_node__a0_n2_10', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_11 = TabularCPD ('ambulance_at_node__a0_n2_11', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_12 = TabularCPD ('ambulance_at_node__a0_n2_12', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_13 = TabularCPD ('ambulance_at_node__a0_n2_13', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_14 = TabularCPD ('ambulance_at_node__a0_n2_14', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_15 = TabularCPD ('ambulance_at_node__a0_n2_15', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_16 = TabularCPD ('ambulance_at_node__a0_n2_16', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_17 = TabularCPD ('ambulance_at_node__a0_n2_17', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_18 = TabularCPD ('ambulance_at_node__a0_n2_18', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_19 = TabularCPD ('ambulance_at_node__a0_n2_19', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_20 = TabularCPD ('ambulance_at_node__a0_n2_20', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_21 = TabularCPD ('ambulance_at_node__a0_n2_21', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_22 = TabularCPD ('ambulance_at_node__a0_n2_22', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_23 = TabularCPD ('ambulance_at_node__a0_n2_23', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_24 = TabularCPD ('ambulance_at_node__a0_n2_24', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_25 = TabularCPD ('ambulance_at_node__a0_n2_25', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_26 = TabularCPD ('ambulance_at_node__a0_n2_26', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_27 = TabularCPD ('ambulance_at_node__a0_n2_27', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_28 = TabularCPD ('ambulance_at_node__a0_n2_28', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_29 = TabularCPD ('ambulance_at_node__a0_n2_29', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_30 = TabularCPD ('ambulance_at_node__a0_n2_30', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_31 = TabularCPD ('ambulance_at_node__a0_n2_31', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_32 = TabularCPD ('ambulance_at_node__a0_n2_32', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_33 = TabularCPD ('ambulance_at_node__a0_n2_33', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_34 = TabularCPD ('ambulance_at_node__a0_n2_34', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_35 = TabularCPD ('ambulance_at_node__a0_n2_35', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_36 = TabularCPD ('ambulance_at_node__a0_n2_36', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_37 = TabularCPD ('ambulance_at_node__a0_n2_37', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_38 = TabularCPD ('ambulance_at_node__a0_n2_38', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n2_39 = TabularCPD ('ambulance_at_node__a0_n2_39', 2, [[1.0], [0.0]]);

cpd_ambulance_at_node__a0_n1_1 = TabularCPD ('ambulance_at_node__a0_n1_1', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_0', 'ambulance_at_node__a0_n1_0', 'ambulance_at_node__a0_n2_0', 'ambulance_at_node__a0_n4_0'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_2 = TabularCPD ('ambulance_at_node__a0_n1_2', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_1', 'ambulance_at_node__a0_n1_1', 'ambulance_at_node__a0_n2_1', 'ambulance_at_node__a0_n4_1'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_3 = TabularCPD ('ambulance_at_node__a0_n1_3', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_2', 'ambulance_at_node__a0_n1_2', 'ambulance_at_node__a0_n2_2', 'ambulance_at_node__a0_n4_2'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_4 = TabularCPD ('ambulance_at_node__a0_n1_4', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_3', 'ambulance_at_node__a0_n1_3', 'ambulance_at_node__a0_n2_3', 'ambulance_at_node__a0_n4_3'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_5 = TabularCPD ('ambulance_at_node__a0_n1_5', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_4', 'ambulance_at_node__a0_n1_4', 'ambulance_at_node__a0_n2_4', 'ambulance_at_node__a0_n4_4'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_6 = TabularCPD ('ambulance_at_node__a0_n1_6', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_5', 'ambulance_at_node__a0_n1_5', 'ambulance_at_node__a0_n2_5', 'ambulance_at_node__a0_n4_5'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_7 = TabularCPD ('ambulance_at_node__a0_n1_7', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_6', 'ambulance_at_node__a0_n1_6', 'ambulance_at_node__a0_n2_6', 'ambulance_at_node__a0_n4_6'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_8 = TabularCPD ('ambulance_at_node__a0_n1_8', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_7', 'ambulance_at_node__a0_n1_7', 'ambulance_at_node__a0_n2_7', 'ambulance_at_node__a0_n4_7'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_9 = TabularCPD ('ambulance_at_node__a0_n1_9', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_8', 'ambulance_at_node__a0_n1_8', 'ambulance_at_node__a0_n2_8', 'ambulance_at_node__a0_n4_8'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_10 = TabularCPD ('ambulance_at_node__a0_n1_10', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_9', 'ambulance_at_node__a0_n1_9', 'ambulance_at_node__a0_n2_9', 'ambulance_at_node__a0_n4_9'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_11 = TabularCPD ('ambulance_at_node__a0_n1_11', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_10', 'ambulance_at_node__a0_n1_10', 'ambulance_at_node__a0_n2_10', 'ambulance_at_node__a0_n4_10'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_12 = TabularCPD ('ambulance_at_node__a0_n1_12', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_11', 'ambulance_at_node__a0_n1_11', 'ambulance_at_node__a0_n2_11', 'ambulance_at_node__a0_n4_11'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_13 = TabularCPD ('ambulance_at_node__a0_n1_13', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_12', 'ambulance_at_node__a0_n1_12', 'ambulance_at_node__a0_n2_12', 'ambulance_at_node__a0_n4_12'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_14 = TabularCPD ('ambulance_at_node__a0_n1_14', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_13', 'ambulance_at_node__a0_n1_13', 'ambulance_at_node__a0_n2_13', 'ambulance_at_node__a0_n4_13'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_15 = TabularCPD ('ambulance_at_node__a0_n1_15', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_14', 'ambulance_at_node__a0_n1_14', 'ambulance_at_node__a0_n2_14', 'ambulance_at_node__a0_n4_14'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_16 = TabularCPD ('ambulance_at_node__a0_n1_16', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_15', 'ambulance_at_node__a0_n1_15', 'ambulance_at_node__a0_n2_15', 'ambulance_at_node__a0_n4_15'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_17 = TabularCPD ('ambulance_at_node__a0_n1_17', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_16', 'ambulance_at_node__a0_n1_16', 'ambulance_at_node__a0_n2_16', 'ambulance_at_node__a0_n4_16'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_18 = TabularCPD ('ambulance_at_node__a0_n1_18', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_17', 'ambulance_at_node__a0_n1_17', 'ambulance_at_node__a0_n2_17', 'ambulance_at_node__a0_n4_17'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_19 = TabularCPD ('ambulance_at_node__a0_n1_19', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_18', 'ambulance_at_node__a0_n1_18', 'ambulance_at_node__a0_n2_18', 'ambulance_at_node__a0_n4_18'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_20 = TabularCPD ('ambulance_at_node__a0_n1_20', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_19', 'ambulance_at_node__a0_n1_19', 'ambulance_at_node__a0_n2_19', 'ambulance_at_node__a0_n4_19'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_21 = TabularCPD ('ambulance_at_node__a0_n1_21', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_20', 'ambulance_at_node__a0_n1_20', 'ambulance_at_node__a0_n2_20', 'ambulance_at_node__a0_n4_20'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_22 = TabularCPD ('ambulance_at_node__a0_n1_22', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_21', 'ambulance_at_node__a0_n1_21', 'ambulance_at_node__a0_n2_21', 'ambulance_at_node__a0_n4_21'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_23 = TabularCPD ('ambulance_at_node__a0_n1_23', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_22', 'ambulance_at_node__a0_n1_22', 'ambulance_at_node__a0_n2_22', 'ambulance_at_node__a0_n4_22'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_24 = TabularCPD ('ambulance_at_node__a0_n1_24', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_23', 'ambulance_at_node__a0_n1_23', 'ambulance_at_node__a0_n2_23', 'ambulance_at_node__a0_n4_23'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_25 = TabularCPD ('ambulance_at_node__a0_n1_25', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_24', 'ambulance_at_node__a0_n1_24', 'ambulance_at_node__a0_n2_24', 'ambulance_at_node__a0_n4_24'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_26 = TabularCPD ('ambulance_at_node__a0_n1_26', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_25', 'ambulance_at_node__a0_n1_25', 'ambulance_at_node__a0_n2_25', 'ambulance_at_node__a0_n4_25'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_27 = TabularCPD ('ambulance_at_node__a0_n1_27', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_26', 'ambulance_at_node__a0_n1_26', 'ambulance_at_node__a0_n2_26', 'ambulance_at_node__a0_n4_26'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_28 = TabularCPD ('ambulance_at_node__a0_n1_28', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_27', 'ambulance_at_node__a0_n1_27', 'ambulance_at_node__a0_n2_27', 'ambulance_at_node__a0_n4_27'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_29 = TabularCPD ('ambulance_at_node__a0_n1_29', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_28', 'ambulance_at_node__a0_n1_28', 'ambulance_at_node__a0_n2_28', 'ambulance_at_node__a0_n4_28'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_30 = TabularCPD ('ambulance_at_node__a0_n1_30', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_29', 'ambulance_at_node__a0_n1_29', 'ambulance_at_node__a0_n2_29', 'ambulance_at_node__a0_n4_29'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_31 = TabularCPD ('ambulance_at_node__a0_n1_31', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_30', 'ambulance_at_node__a0_n1_30', 'ambulance_at_node__a0_n2_30', 'ambulance_at_node__a0_n4_30'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_32 = TabularCPD ('ambulance_at_node__a0_n1_32', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_31', 'ambulance_at_node__a0_n1_31', 'ambulance_at_node__a0_n2_31', 'ambulance_at_node__a0_n4_31'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_33 = TabularCPD ('ambulance_at_node__a0_n1_33', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_32', 'ambulance_at_node__a0_n1_32', 'ambulance_at_node__a0_n2_32', 'ambulance_at_node__a0_n4_32'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_34 = TabularCPD ('ambulance_at_node__a0_n1_34', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_33', 'ambulance_at_node__a0_n1_33', 'ambulance_at_node__a0_n2_33', 'ambulance_at_node__a0_n4_33'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_35 = TabularCPD ('ambulance_at_node__a0_n1_35', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_34', 'ambulance_at_node__a0_n1_34', 'ambulance_at_node__a0_n2_34', 'ambulance_at_node__a0_n4_34'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_36 = TabularCPD ('ambulance_at_node__a0_n1_36', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_35', 'ambulance_at_node__a0_n1_35', 'ambulance_at_node__a0_n2_35', 'ambulance_at_node__a0_n4_35'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_37 = TabularCPD ('ambulance_at_node__a0_n1_37', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_36', 'ambulance_at_node__a0_n1_36', 'ambulance_at_node__a0_n2_36', 'ambulance_at_node__a0_n4_36'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_38 = TabularCPD ('ambulance_at_node__a0_n1_38', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_37', 'ambulance_at_node__a0_n1_37', 'ambulance_at_node__a0_n2_37', 'ambulance_at_node__a0_n4_37'], [2, 2, 2, 2]);
cpd_ambulance_at_node__a0_n1_39 = TabularCPD ('ambulance_at_node__a0_n1_39', 2, [[1.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0], [0.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]], ['ambulance_at_node__a0_n0_38', 'ambulance_at_node__a0_n1_38', 'ambulance_at_node__a0_n2_38', 'ambulance_at_node__a0_n4_38'], [2, 2, 2, 2]);

cpd_ambulance_at_node__a0_n8_1 = TabularCPD ('ambulance_at_node__a0_n8_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_0'], [2]);
cpd_ambulance_at_node__a0_n8_2 = TabularCPD ('ambulance_at_node__a0_n8_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_1'], [2]);
cpd_ambulance_at_node__a0_n8_3 = TabularCPD ('ambulance_at_node__a0_n8_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_2'], [2]);
cpd_ambulance_at_node__a0_n8_4 = TabularCPD ('ambulance_at_node__a0_n8_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_3'], [2]);
cpd_ambulance_at_node__a0_n8_5 = TabularCPD ('ambulance_at_node__a0_n8_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_4'], [2]);
cpd_ambulance_at_node__a0_n8_6 = TabularCPD ('ambulance_at_node__a0_n8_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_5'], [2]);
cpd_ambulance_at_node__a0_n8_7 = TabularCPD ('ambulance_at_node__a0_n8_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_6'], [2]);
cpd_ambulance_at_node__a0_n8_8 = TabularCPD ('ambulance_at_node__a0_n8_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_7'], [2]);
cpd_ambulance_at_node__a0_n8_9 = TabularCPD ('ambulance_at_node__a0_n8_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_8'], [2]);
cpd_ambulance_at_node__a0_n8_10 = TabularCPD ('ambulance_at_node__a0_n8_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_9'], [2]);
cpd_ambulance_at_node__a0_n8_11 = TabularCPD ('ambulance_at_node__a0_n8_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_10'], [2]);
cpd_ambulance_at_node__a0_n8_12 = TabularCPD ('ambulance_at_node__a0_n8_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_11'], [2]);
cpd_ambulance_at_node__a0_n8_13 = TabularCPD ('ambulance_at_node__a0_n8_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_12'], [2]);
cpd_ambulance_at_node__a0_n8_14 = TabularCPD ('ambulance_at_node__a0_n8_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_13'], [2]);
cpd_ambulance_at_node__a0_n8_15 = TabularCPD ('ambulance_at_node__a0_n8_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_14'], [2]);
cpd_ambulance_at_node__a0_n8_16 = TabularCPD ('ambulance_at_node__a0_n8_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_15'], [2]);
cpd_ambulance_at_node__a0_n8_17 = TabularCPD ('ambulance_at_node__a0_n8_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_16'], [2]);
cpd_ambulance_at_node__a0_n8_18 = TabularCPD ('ambulance_at_node__a0_n8_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_17'], [2]);
cpd_ambulance_at_node__a0_n8_19 = TabularCPD ('ambulance_at_node__a0_n8_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_18'], [2]);
cpd_ambulance_at_node__a0_n8_20 = TabularCPD ('ambulance_at_node__a0_n8_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_19'], [2]);
cpd_ambulance_at_node__a0_n8_21 = TabularCPD ('ambulance_at_node__a0_n8_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_20'], [2]);
cpd_ambulance_at_node__a0_n8_22 = TabularCPD ('ambulance_at_node__a0_n8_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_21'], [2]);
cpd_ambulance_at_node__a0_n8_23 = TabularCPD ('ambulance_at_node__a0_n8_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_22'], [2]);
cpd_ambulance_at_node__a0_n8_24 = TabularCPD ('ambulance_at_node__a0_n8_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_23'], [2]);
cpd_ambulance_at_node__a0_n8_25 = TabularCPD ('ambulance_at_node__a0_n8_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_24'], [2]);
cpd_ambulance_at_node__a0_n8_26 = TabularCPD ('ambulance_at_node__a0_n8_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_25'], [2]);
cpd_ambulance_at_node__a0_n8_27 = TabularCPD ('ambulance_at_node__a0_n8_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_26'], [2]);
cpd_ambulance_at_node__a0_n8_28 = TabularCPD ('ambulance_at_node__a0_n8_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_27'], [2]);
cpd_ambulance_at_node__a0_n8_29 = TabularCPD ('ambulance_at_node__a0_n8_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_28'], [2]);
cpd_ambulance_at_node__a0_n8_30 = TabularCPD ('ambulance_at_node__a0_n8_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_29'], [2]);
cpd_ambulance_at_node__a0_n8_31 = TabularCPD ('ambulance_at_node__a0_n8_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_30'], [2]);
cpd_ambulance_at_node__a0_n8_32 = TabularCPD ('ambulance_at_node__a0_n8_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_31'], [2]);
cpd_ambulance_at_node__a0_n8_33 = TabularCPD ('ambulance_at_node__a0_n8_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_32'], [2]);
cpd_ambulance_at_node__a0_n8_34 = TabularCPD ('ambulance_at_node__a0_n8_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_33'], [2]);
cpd_ambulance_at_node__a0_n8_35 = TabularCPD ('ambulance_at_node__a0_n8_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_34'], [2]);
cpd_ambulance_at_node__a0_n8_36 = TabularCPD ('ambulance_at_node__a0_n8_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_35'], [2]);
cpd_ambulance_at_node__a0_n8_37 = TabularCPD ('ambulance_at_node__a0_n8_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_36'], [2]);
cpd_ambulance_at_node__a0_n8_38 = TabularCPD ('ambulance_at_node__a0_n8_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_37'], [2]);
cpd_ambulance_at_node__a0_n8_39 = TabularCPD ('ambulance_at_node__a0_n8_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n8_38'], [2]);

cpd_ambulance_at_node__a0_n7_1 = TabularCPD ('ambulance_at_node__a0_n7_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_0'], [2]);
cpd_ambulance_at_node__a0_n7_2 = TabularCPD ('ambulance_at_node__a0_n7_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_1'], [2]);
cpd_ambulance_at_node__a0_n7_3 = TabularCPD ('ambulance_at_node__a0_n7_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_2'], [2]);
cpd_ambulance_at_node__a0_n7_4 = TabularCPD ('ambulance_at_node__a0_n7_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_3'], [2]);
cpd_ambulance_at_node__a0_n7_5 = TabularCPD ('ambulance_at_node__a0_n7_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_4'], [2]);
cpd_ambulance_at_node__a0_n7_6 = TabularCPD ('ambulance_at_node__a0_n7_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_5'], [2]);
cpd_ambulance_at_node__a0_n7_7 = TabularCPD ('ambulance_at_node__a0_n7_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_6'], [2]);
cpd_ambulance_at_node__a0_n7_8 = TabularCPD ('ambulance_at_node__a0_n7_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_7'], [2]);
cpd_ambulance_at_node__a0_n7_9 = TabularCPD ('ambulance_at_node__a0_n7_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_8'], [2]);
cpd_ambulance_at_node__a0_n7_10 = TabularCPD ('ambulance_at_node__a0_n7_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_9'], [2]);
cpd_ambulance_at_node__a0_n7_11 = TabularCPD ('ambulance_at_node__a0_n7_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_10'], [2]);
cpd_ambulance_at_node__a0_n7_12 = TabularCPD ('ambulance_at_node__a0_n7_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_11'], [2]);
cpd_ambulance_at_node__a0_n7_13 = TabularCPD ('ambulance_at_node__a0_n7_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_12'], [2]);
cpd_ambulance_at_node__a0_n7_14 = TabularCPD ('ambulance_at_node__a0_n7_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_13'], [2]);
cpd_ambulance_at_node__a0_n7_15 = TabularCPD ('ambulance_at_node__a0_n7_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_14'], [2]);
cpd_ambulance_at_node__a0_n7_16 = TabularCPD ('ambulance_at_node__a0_n7_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_15'], [2]);
cpd_ambulance_at_node__a0_n7_17 = TabularCPD ('ambulance_at_node__a0_n7_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_16'], [2]);
cpd_ambulance_at_node__a0_n7_18 = TabularCPD ('ambulance_at_node__a0_n7_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_17'], [2]);
cpd_ambulance_at_node__a0_n7_19 = TabularCPD ('ambulance_at_node__a0_n7_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_18'], [2]);
cpd_ambulance_at_node__a0_n7_20 = TabularCPD ('ambulance_at_node__a0_n7_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_19'], [2]);
cpd_ambulance_at_node__a0_n7_21 = TabularCPD ('ambulance_at_node__a0_n7_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_20'], [2]);
cpd_ambulance_at_node__a0_n7_22 = TabularCPD ('ambulance_at_node__a0_n7_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_21'], [2]);
cpd_ambulance_at_node__a0_n7_23 = TabularCPD ('ambulance_at_node__a0_n7_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_22'], [2]);
cpd_ambulance_at_node__a0_n7_24 = TabularCPD ('ambulance_at_node__a0_n7_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_23'], [2]);
cpd_ambulance_at_node__a0_n7_25 = TabularCPD ('ambulance_at_node__a0_n7_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_24'], [2]);
cpd_ambulance_at_node__a0_n7_26 = TabularCPD ('ambulance_at_node__a0_n7_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_25'], [2]);
cpd_ambulance_at_node__a0_n7_27 = TabularCPD ('ambulance_at_node__a0_n7_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_26'], [2]);
cpd_ambulance_at_node__a0_n7_28 = TabularCPD ('ambulance_at_node__a0_n7_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_27'], [2]);
cpd_ambulance_at_node__a0_n7_29 = TabularCPD ('ambulance_at_node__a0_n7_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_28'], [2]);
cpd_ambulance_at_node__a0_n7_30 = TabularCPD ('ambulance_at_node__a0_n7_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_29'], [2]);
cpd_ambulance_at_node__a0_n7_31 = TabularCPD ('ambulance_at_node__a0_n7_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_30'], [2]);
cpd_ambulance_at_node__a0_n7_32 = TabularCPD ('ambulance_at_node__a0_n7_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_31'], [2]);
cpd_ambulance_at_node__a0_n7_33 = TabularCPD ('ambulance_at_node__a0_n7_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_32'], [2]);
cpd_ambulance_at_node__a0_n7_34 = TabularCPD ('ambulance_at_node__a0_n7_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_33'], [2]);
cpd_ambulance_at_node__a0_n7_35 = TabularCPD ('ambulance_at_node__a0_n7_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_34'], [2]);
cpd_ambulance_at_node__a0_n7_36 = TabularCPD ('ambulance_at_node__a0_n7_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_35'], [2]);
cpd_ambulance_at_node__a0_n7_37 = TabularCPD ('ambulance_at_node__a0_n7_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_36'], [2]);
cpd_ambulance_at_node__a0_n7_38 = TabularCPD ('ambulance_at_node__a0_n7_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_37'], [2]);
cpd_ambulance_at_node__a0_n7_39 = TabularCPD ('ambulance_at_node__a0_n7_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n7_38'], [2]);

cpd_ambulance_at_node__a0_n6_1 = TabularCPD ('ambulance_at_node__a0_n6_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_0'], [2]);
cpd_ambulance_at_node__a0_n6_2 = TabularCPD ('ambulance_at_node__a0_n6_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_1'], [2]);
cpd_ambulance_at_node__a0_n6_3 = TabularCPD ('ambulance_at_node__a0_n6_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_2'], [2]);
cpd_ambulance_at_node__a0_n6_4 = TabularCPD ('ambulance_at_node__a0_n6_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_3'], [2]);
cpd_ambulance_at_node__a0_n6_5 = TabularCPD ('ambulance_at_node__a0_n6_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_4'], [2]);
cpd_ambulance_at_node__a0_n6_6 = TabularCPD ('ambulance_at_node__a0_n6_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_5'], [2]);
cpd_ambulance_at_node__a0_n6_7 = TabularCPD ('ambulance_at_node__a0_n6_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_6'], [2]);
cpd_ambulance_at_node__a0_n6_8 = TabularCPD ('ambulance_at_node__a0_n6_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_7'], [2]);
cpd_ambulance_at_node__a0_n6_9 = TabularCPD ('ambulance_at_node__a0_n6_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_8'], [2]);
cpd_ambulance_at_node__a0_n6_10 = TabularCPD ('ambulance_at_node__a0_n6_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_9'], [2]);
cpd_ambulance_at_node__a0_n6_11 = TabularCPD ('ambulance_at_node__a0_n6_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_10'], [2]);
cpd_ambulance_at_node__a0_n6_12 = TabularCPD ('ambulance_at_node__a0_n6_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_11'], [2]);
cpd_ambulance_at_node__a0_n6_13 = TabularCPD ('ambulance_at_node__a0_n6_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_12'], [2]);
cpd_ambulance_at_node__a0_n6_14 = TabularCPD ('ambulance_at_node__a0_n6_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_13'], [2]);
cpd_ambulance_at_node__a0_n6_15 = TabularCPD ('ambulance_at_node__a0_n6_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_14'], [2]);
cpd_ambulance_at_node__a0_n6_16 = TabularCPD ('ambulance_at_node__a0_n6_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_15'], [2]);
cpd_ambulance_at_node__a0_n6_17 = TabularCPD ('ambulance_at_node__a0_n6_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_16'], [2]);
cpd_ambulance_at_node__a0_n6_18 = TabularCPD ('ambulance_at_node__a0_n6_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_17'], [2]);
cpd_ambulance_at_node__a0_n6_19 = TabularCPD ('ambulance_at_node__a0_n6_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_18'], [2]);
cpd_ambulance_at_node__a0_n6_20 = TabularCPD ('ambulance_at_node__a0_n6_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_19'], [2]);
cpd_ambulance_at_node__a0_n6_21 = TabularCPD ('ambulance_at_node__a0_n6_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_20'], [2]);
cpd_ambulance_at_node__a0_n6_22 = TabularCPD ('ambulance_at_node__a0_n6_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_21'], [2]);
cpd_ambulance_at_node__a0_n6_23 = TabularCPD ('ambulance_at_node__a0_n6_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_22'], [2]);
cpd_ambulance_at_node__a0_n6_24 = TabularCPD ('ambulance_at_node__a0_n6_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_23'], [2]);
cpd_ambulance_at_node__a0_n6_25 = TabularCPD ('ambulance_at_node__a0_n6_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_24'], [2]);
cpd_ambulance_at_node__a0_n6_26 = TabularCPD ('ambulance_at_node__a0_n6_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_25'], [2]);
cpd_ambulance_at_node__a0_n6_27 = TabularCPD ('ambulance_at_node__a0_n6_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_26'], [2]);
cpd_ambulance_at_node__a0_n6_28 = TabularCPD ('ambulance_at_node__a0_n6_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_27'], [2]);
cpd_ambulance_at_node__a0_n6_29 = TabularCPD ('ambulance_at_node__a0_n6_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_28'], [2]);
cpd_ambulance_at_node__a0_n6_30 = TabularCPD ('ambulance_at_node__a0_n6_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_29'], [2]);
cpd_ambulance_at_node__a0_n6_31 = TabularCPD ('ambulance_at_node__a0_n6_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_30'], [2]);
cpd_ambulance_at_node__a0_n6_32 = TabularCPD ('ambulance_at_node__a0_n6_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_31'], [2]);
cpd_ambulance_at_node__a0_n6_33 = TabularCPD ('ambulance_at_node__a0_n6_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_32'], [2]);
cpd_ambulance_at_node__a0_n6_34 = TabularCPD ('ambulance_at_node__a0_n6_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_33'], [2]);
cpd_ambulance_at_node__a0_n6_35 = TabularCPD ('ambulance_at_node__a0_n6_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_34'], [2]);
cpd_ambulance_at_node__a0_n6_36 = TabularCPD ('ambulance_at_node__a0_n6_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_35'], [2]);
cpd_ambulance_at_node__a0_n6_37 = TabularCPD ('ambulance_at_node__a0_n6_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_36'], [2]);
cpd_ambulance_at_node__a0_n6_38 = TabularCPD ('ambulance_at_node__a0_n6_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_37'], [2]);
cpd_ambulance_at_node__a0_n6_39 = TabularCPD ('ambulance_at_node__a0_n6_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n6_38'], [2]);

cpd_ambulance_at_node__a0_n5_1 = TabularCPD ('ambulance_at_node__a0_n5_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_0'], [2]);
cpd_ambulance_at_node__a0_n5_2 = TabularCPD ('ambulance_at_node__a0_n5_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_1'], [2]);
cpd_ambulance_at_node__a0_n5_3 = TabularCPD ('ambulance_at_node__a0_n5_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_2'], [2]);
cpd_ambulance_at_node__a0_n5_4 = TabularCPD ('ambulance_at_node__a0_n5_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_3'], [2]);
cpd_ambulance_at_node__a0_n5_5 = TabularCPD ('ambulance_at_node__a0_n5_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_4'], [2]);
cpd_ambulance_at_node__a0_n5_6 = TabularCPD ('ambulance_at_node__a0_n5_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_5'], [2]);
cpd_ambulance_at_node__a0_n5_7 = TabularCPD ('ambulance_at_node__a0_n5_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_6'], [2]);
cpd_ambulance_at_node__a0_n5_8 = TabularCPD ('ambulance_at_node__a0_n5_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_7'], [2]);
cpd_ambulance_at_node__a0_n5_9 = TabularCPD ('ambulance_at_node__a0_n5_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_8'], [2]);
cpd_ambulance_at_node__a0_n5_10 = TabularCPD ('ambulance_at_node__a0_n5_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_9'], [2]);
cpd_ambulance_at_node__a0_n5_11 = TabularCPD ('ambulance_at_node__a0_n5_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_10'], [2]);
cpd_ambulance_at_node__a0_n5_12 = TabularCPD ('ambulance_at_node__a0_n5_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_11'], [2]);
cpd_ambulance_at_node__a0_n5_13 = TabularCPD ('ambulance_at_node__a0_n5_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_12'], [2]);
cpd_ambulance_at_node__a0_n5_14 = TabularCPD ('ambulance_at_node__a0_n5_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_13'], [2]);
cpd_ambulance_at_node__a0_n5_15 = TabularCPD ('ambulance_at_node__a0_n5_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_14'], [2]);
cpd_ambulance_at_node__a0_n5_16 = TabularCPD ('ambulance_at_node__a0_n5_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_15'], [2]);
cpd_ambulance_at_node__a0_n5_17 = TabularCPD ('ambulance_at_node__a0_n5_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_16'], [2]);
cpd_ambulance_at_node__a0_n5_18 = TabularCPD ('ambulance_at_node__a0_n5_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_17'], [2]);
cpd_ambulance_at_node__a0_n5_19 = TabularCPD ('ambulance_at_node__a0_n5_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_18'], [2]);
cpd_ambulance_at_node__a0_n5_20 = TabularCPD ('ambulance_at_node__a0_n5_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_19'], [2]);
cpd_ambulance_at_node__a0_n5_21 = TabularCPD ('ambulance_at_node__a0_n5_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_20'], [2]);
cpd_ambulance_at_node__a0_n5_22 = TabularCPD ('ambulance_at_node__a0_n5_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_21'], [2]);
cpd_ambulance_at_node__a0_n5_23 = TabularCPD ('ambulance_at_node__a0_n5_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_22'], [2]);
cpd_ambulance_at_node__a0_n5_24 = TabularCPD ('ambulance_at_node__a0_n5_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_23'], [2]);
cpd_ambulance_at_node__a0_n5_25 = TabularCPD ('ambulance_at_node__a0_n5_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_24'], [2]);
cpd_ambulance_at_node__a0_n5_26 = TabularCPD ('ambulance_at_node__a0_n5_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_25'], [2]);
cpd_ambulance_at_node__a0_n5_27 = TabularCPD ('ambulance_at_node__a0_n5_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_26'], [2]);
cpd_ambulance_at_node__a0_n5_28 = TabularCPD ('ambulance_at_node__a0_n5_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_27'], [2]);
cpd_ambulance_at_node__a0_n5_29 = TabularCPD ('ambulance_at_node__a0_n5_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_28'], [2]);
cpd_ambulance_at_node__a0_n5_30 = TabularCPD ('ambulance_at_node__a0_n5_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_29'], [2]);
cpd_ambulance_at_node__a0_n5_31 = TabularCPD ('ambulance_at_node__a0_n5_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_30'], [2]);
cpd_ambulance_at_node__a0_n5_32 = TabularCPD ('ambulance_at_node__a0_n5_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_31'], [2]);
cpd_ambulance_at_node__a0_n5_33 = TabularCPD ('ambulance_at_node__a0_n5_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_32'], [2]);
cpd_ambulance_at_node__a0_n5_34 = TabularCPD ('ambulance_at_node__a0_n5_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_33'], [2]);
cpd_ambulance_at_node__a0_n5_35 = TabularCPD ('ambulance_at_node__a0_n5_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_34'], [2]);
cpd_ambulance_at_node__a0_n5_36 = TabularCPD ('ambulance_at_node__a0_n5_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_35'], [2]);
cpd_ambulance_at_node__a0_n5_37 = TabularCPD ('ambulance_at_node__a0_n5_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_36'], [2]);
cpd_ambulance_at_node__a0_n5_38 = TabularCPD ('ambulance_at_node__a0_n5_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_37'], [2]);
cpd_ambulance_at_node__a0_n5_39 = TabularCPD ('ambulance_at_node__a0_n5_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a0_n5_38'], [2]);

cpd_person_waiting_service__n0_1 = TabularCPD ('person_waiting_service__n0_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_0'], [2]);
cpd_person_waiting_service__n0_2 = TabularCPD ('person_waiting_service__n0_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_1'], [2]);
cpd_person_waiting_service__n0_3 = TabularCPD ('person_waiting_service__n0_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_2'], [2]);
cpd_person_waiting_service__n0_4 = TabularCPD ('person_waiting_service__n0_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_3'], [2]);
cpd_person_waiting_service__n0_5 = TabularCPD ('person_waiting_service__n0_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_4'], [2]);
cpd_person_waiting_service__n0_6 = TabularCPD ('person_waiting_service__n0_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_5'], [2]);
cpd_person_waiting_service__n0_7 = TabularCPD ('person_waiting_service__n0_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_6'], [2]);
cpd_person_waiting_service__n0_8 = TabularCPD ('person_waiting_service__n0_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_7'], [2]);
cpd_person_waiting_service__n0_9 = TabularCPD ('person_waiting_service__n0_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_8'], [2]);
cpd_person_waiting_service__n0_10 = TabularCPD ('person_waiting_service__n0_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_9'], [2]);
cpd_person_waiting_service__n0_11 = TabularCPD ('person_waiting_service__n0_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_10'], [2]);
cpd_person_waiting_service__n0_12 = TabularCPD ('person_waiting_service__n0_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_11'], [2]);
cpd_person_waiting_service__n0_13 = TabularCPD ('person_waiting_service__n0_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_12'], [2]);
cpd_person_waiting_service__n0_14 = TabularCPD ('person_waiting_service__n0_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_13'], [2]);
cpd_person_waiting_service__n0_15 = TabularCPD ('person_waiting_service__n0_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_14'], [2]);
cpd_person_waiting_service__n0_16 = TabularCPD ('person_waiting_service__n0_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_15'], [2]);
cpd_person_waiting_service__n0_17 = TabularCPD ('person_waiting_service__n0_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_16'], [2]);
cpd_person_waiting_service__n0_18 = TabularCPD ('person_waiting_service__n0_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_17'], [2]);
cpd_person_waiting_service__n0_19 = TabularCPD ('person_waiting_service__n0_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_18'], [2]);
cpd_person_waiting_service__n0_20 = TabularCPD ('person_waiting_service__n0_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_19'], [2]);
cpd_person_waiting_service__n0_21 = TabularCPD ('person_waiting_service__n0_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_20'], [2]);
cpd_person_waiting_service__n0_22 = TabularCPD ('person_waiting_service__n0_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_21'], [2]);
cpd_person_waiting_service__n0_23 = TabularCPD ('person_waiting_service__n0_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_22'], [2]);
cpd_person_waiting_service__n0_24 = TabularCPD ('person_waiting_service__n0_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_23'], [2]);
cpd_person_waiting_service__n0_25 = TabularCPD ('person_waiting_service__n0_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_24'], [2]);
cpd_person_waiting_service__n0_26 = TabularCPD ('person_waiting_service__n0_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_25'], [2]);
cpd_person_waiting_service__n0_27 = TabularCPD ('person_waiting_service__n0_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_26'], [2]);
cpd_person_waiting_service__n0_28 = TabularCPD ('person_waiting_service__n0_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_27'], [2]);
cpd_person_waiting_service__n0_29 = TabularCPD ('person_waiting_service__n0_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_28'], [2]);
cpd_person_waiting_service__n0_30 = TabularCPD ('person_waiting_service__n0_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_29'], [2]);
cpd_person_waiting_service__n0_31 = TabularCPD ('person_waiting_service__n0_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_30'], [2]);
cpd_person_waiting_service__n0_32 = TabularCPD ('person_waiting_service__n0_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_31'], [2]);
cpd_person_waiting_service__n0_33 = TabularCPD ('person_waiting_service__n0_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_32'], [2]);
cpd_person_waiting_service__n0_34 = TabularCPD ('person_waiting_service__n0_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_33'], [2]);
cpd_person_waiting_service__n0_35 = TabularCPD ('person_waiting_service__n0_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_34'], [2]);
cpd_person_waiting_service__n0_36 = TabularCPD ('person_waiting_service__n0_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_35'], [2]);
cpd_person_waiting_service__n0_37 = TabularCPD ('person_waiting_service__n0_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_36'], [2]);
cpd_person_waiting_service__n0_38 = TabularCPD ('person_waiting_service__n0_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_37'], [2]);
cpd_person_waiting_service__n0_39 = TabularCPD ('person_waiting_service__n0_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['person_waiting_service__n0_38'], [2]);

cpd_ambulance_at_node__a0_n0_1 = TabularCPD ('ambulance_at_node__a0_n0_1', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_2 = TabularCPD ('ambulance_at_node__a0_n0_2', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_3 = TabularCPD ('ambulance_at_node__a0_n0_3', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_4 = TabularCPD ('ambulance_at_node__a0_n0_4', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_5 = TabularCPD ('ambulance_at_node__a0_n0_5', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_6 = TabularCPD ('ambulance_at_node__a0_n0_6', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_7 = TabularCPD ('ambulance_at_node__a0_n0_7', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_8 = TabularCPD ('ambulance_at_node__a0_n0_8', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_9 = TabularCPD ('ambulance_at_node__a0_n0_9', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_10 = TabularCPD ('ambulance_at_node__a0_n0_10', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_11 = TabularCPD ('ambulance_at_node__a0_n0_11', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_12 = TabularCPD ('ambulance_at_node__a0_n0_12', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_13 = TabularCPD ('ambulance_at_node__a0_n0_13', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_14 = TabularCPD ('ambulance_at_node__a0_n0_14', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_15 = TabularCPD ('ambulance_at_node__a0_n0_15', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_16 = TabularCPD ('ambulance_at_node__a0_n0_16', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_17 = TabularCPD ('ambulance_at_node__a0_n0_17', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_18 = TabularCPD ('ambulance_at_node__a0_n0_18', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_19 = TabularCPD ('ambulance_at_node__a0_n0_19', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_20 = TabularCPD ('ambulance_at_node__a0_n0_20', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_21 = TabularCPD ('ambulance_at_node__a0_n0_21', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_22 = TabularCPD ('ambulance_at_node__a0_n0_22', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_23 = TabularCPD ('ambulance_at_node__a0_n0_23', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_24 = TabularCPD ('ambulance_at_node__a0_n0_24', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_25 = TabularCPD ('ambulance_at_node__a0_n0_25', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_26 = TabularCPD ('ambulance_at_node__a0_n0_26', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_27 = TabularCPD ('ambulance_at_node__a0_n0_27', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_28 = TabularCPD ('ambulance_at_node__a0_n0_28', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_29 = TabularCPD ('ambulance_at_node__a0_n0_29', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_30 = TabularCPD ('ambulance_at_node__a0_n0_30', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_31 = TabularCPD ('ambulance_at_node__a0_n0_31', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_32 = TabularCPD ('ambulance_at_node__a0_n0_32', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_33 = TabularCPD ('ambulance_at_node__a0_n0_33', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_34 = TabularCPD ('ambulance_at_node__a0_n0_34', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_35 = TabularCPD ('ambulance_at_node__a0_n0_35', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_36 = TabularCPD ('ambulance_at_node__a0_n0_36', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_37 = TabularCPD ('ambulance_at_node__a0_n0_37', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_38 = TabularCPD ('ambulance_at_node__a0_n0_38', 2, [[1.0], [0.0]]);
cpd_ambulance_at_node__a0_n0_39 = TabularCPD ('ambulance_at_node__a0_n0_39', 2, [[1.0], [0.0]]);

cpd_person_waiting_service__n3_1 = TabularCPD ('person_waiting_service__n3_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_0'], [2]);
cpd_person_waiting_service__n3_2 = TabularCPD ('person_waiting_service__n3_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_1'], [2]);
cpd_person_waiting_service__n3_3 = TabularCPD ('person_waiting_service__n3_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_2'], [2]);
cpd_person_waiting_service__n3_4 = TabularCPD ('person_waiting_service__n3_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_3'], [2]);
cpd_person_waiting_service__n3_5 = TabularCPD ('person_waiting_service__n3_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_4'], [2]);
cpd_person_waiting_service__n3_6 = TabularCPD ('person_waiting_service__n3_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_5'], [2]);
cpd_person_waiting_service__n3_7 = TabularCPD ('person_waiting_service__n3_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_6'], [2]);
cpd_person_waiting_service__n3_8 = TabularCPD ('person_waiting_service__n3_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_7'], [2]);
cpd_person_waiting_service__n3_9 = TabularCPD ('person_waiting_service__n3_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_8'], [2]);
cpd_person_waiting_service__n3_10 = TabularCPD ('person_waiting_service__n3_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_9'], [2]);
cpd_person_waiting_service__n3_11 = TabularCPD ('person_waiting_service__n3_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_10'], [2]);
cpd_person_waiting_service__n3_12 = TabularCPD ('person_waiting_service__n3_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_11'], [2]);
cpd_person_waiting_service__n3_13 = TabularCPD ('person_waiting_service__n3_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_12'], [2]);
cpd_person_waiting_service__n3_14 = TabularCPD ('person_waiting_service__n3_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_13'], [2]);
cpd_person_waiting_service__n3_15 = TabularCPD ('person_waiting_service__n3_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_14'], [2]);
cpd_person_waiting_service__n3_16 = TabularCPD ('person_waiting_service__n3_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_15'], [2]);
cpd_person_waiting_service__n3_17 = TabularCPD ('person_waiting_service__n3_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_16'], [2]);
cpd_person_waiting_service__n3_18 = TabularCPD ('person_waiting_service__n3_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_17'], [2]);
cpd_person_waiting_service__n3_19 = TabularCPD ('person_waiting_service__n3_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_18'], [2]);
cpd_person_waiting_service__n3_20 = TabularCPD ('person_waiting_service__n3_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_19'], [2]);
cpd_person_waiting_service__n3_21 = TabularCPD ('person_waiting_service__n3_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_20'], [2]);
cpd_person_waiting_service__n3_22 = TabularCPD ('person_waiting_service__n3_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_21'], [2]);
cpd_person_waiting_service__n3_23 = TabularCPD ('person_waiting_service__n3_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_22'], [2]);
cpd_person_waiting_service__n3_24 = TabularCPD ('person_waiting_service__n3_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_23'], [2]);
cpd_person_waiting_service__n3_25 = TabularCPD ('person_waiting_service__n3_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_24'], [2]);
cpd_person_waiting_service__n3_26 = TabularCPD ('person_waiting_service__n3_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_25'], [2]);
cpd_person_waiting_service__n3_27 = TabularCPD ('person_waiting_service__n3_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_26'], [2]);
cpd_person_waiting_service__n3_28 = TabularCPD ('person_waiting_service__n3_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_27'], [2]);
cpd_person_waiting_service__n3_29 = TabularCPD ('person_waiting_service__n3_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_28'], [2]);
cpd_person_waiting_service__n3_30 = TabularCPD ('person_waiting_service__n3_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_29'], [2]);
cpd_person_waiting_service__n3_31 = TabularCPD ('person_waiting_service__n3_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_30'], [2]);
cpd_person_waiting_service__n3_32 = TabularCPD ('person_waiting_service__n3_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_31'], [2]);
cpd_person_waiting_service__n3_33 = TabularCPD ('person_waiting_service__n3_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_32'], [2]);
cpd_person_waiting_service__n3_34 = TabularCPD ('person_waiting_service__n3_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_33'], [2]);
cpd_person_waiting_service__n3_35 = TabularCPD ('person_waiting_service__n3_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_34'], [2]);
cpd_person_waiting_service__n3_36 = TabularCPD ('person_waiting_service__n3_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_35'], [2]);
cpd_person_waiting_service__n3_37 = TabularCPD ('person_waiting_service__n3_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_36'], [2]);
cpd_person_waiting_service__n3_38 = TabularCPD ('person_waiting_service__n3_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_37'], [2]);
cpd_person_waiting_service__n3_39 = TabularCPD ('person_waiting_service__n3_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n3_38'], [2]);

cpd_person_waiting_service__n4_1 = TabularCPD ('person_waiting_service__n4_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_0'], [2]);
cpd_person_waiting_service__n4_2 = TabularCPD ('person_waiting_service__n4_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_1'], [2]);
cpd_person_waiting_service__n4_3 = TabularCPD ('person_waiting_service__n4_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_2'], [2]);
cpd_person_waiting_service__n4_4 = TabularCPD ('person_waiting_service__n4_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_3'], [2]);
cpd_person_waiting_service__n4_5 = TabularCPD ('person_waiting_service__n4_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_4'], [2]);
cpd_person_waiting_service__n4_6 = TabularCPD ('person_waiting_service__n4_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_5'], [2]);
cpd_person_waiting_service__n4_7 = TabularCPD ('person_waiting_service__n4_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_6'], [2]);
cpd_person_waiting_service__n4_8 = TabularCPD ('person_waiting_service__n4_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_7'], [2]);
cpd_person_waiting_service__n4_9 = TabularCPD ('person_waiting_service__n4_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_8'], [2]);
cpd_person_waiting_service__n4_10 = TabularCPD ('person_waiting_service__n4_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_9'], [2]);
cpd_person_waiting_service__n4_11 = TabularCPD ('person_waiting_service__n4_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_10'], [2]);
cpd_person_waiting_service__n4_12 = TabularCPD ('person_waiting_service__n4_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_11'], [2]);
cpd_person_waiting_service__n4_13 = TabularCPD ('person_waiting_service__n4_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_12'], [2]);
cpd_person_waiting_service__n4_14 = TabularCPD ('person_waiting_service__n4_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_13'], [2]);
cpd_person_waiting_service__n4_15 = TabularCPD ('person_waiting_service__n4_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_14'], [2]);
cpd_person_waiting_service__n4_16 = TabularCPD ('person_waiting_service__n4_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_15'], [2]);
cpd_person_waiting_service__n4_17 = TabularCPD ('person_waiting_service__n4_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_16'], [2]);
cpd_person_waiting_service__n4_18 = TabularCPD ('person_waiting_service__n4_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_17'], [2]);
cpd_person_waiting_service__n4_19 = TabularCPD ('person_waiting_service__n4_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_18'], [2]);
cpd_person_waiting_service__n4_20 = TabularCPD ('person_waiting_service__n4_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_19'], [2]);
cpd_person_waiting_service__n4_21 = TabularCPD ('person_waiting_service__n4_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_20'], [2]);
cpd_person_waiting_service__n4_22 = TabularCPD ('person_waiting_service__n4_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_21'], [2]);
cpd_person_waiting_service__n4_23 = TabularCPD ('person_waiting_service__n4_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_22'], [2]);
cpd_person_waiting_service__n4_24 = TabularCPD ('person_waiting_service__n4_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_23'], [2]);
cpd_person_waiting_service__n4_25 = TabularCPD ('person_waiting_service__n4_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_24'], [2]);
cpd_person_waiting_service__n4_26 = TabularCPD ('person_waiting_service__n4_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_25'], [2]);
cpd_person_waiting_service__n4_27 = TabularCPD ('person_waiting_service__n4_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_26'], [2]);
cpd_person_waiting_service__n4_28 = TabularCPD ('person_waiting_service__n4_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_27'], [2]);
cpd_person_waiting_service__n4_29 = TabularCPD ('person_waiting_service__n4_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_28'], [2]);
cpd_person_waiting_service__n4_30 = TabularCPD ('person_waiting_service__n4_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_29'], [2]);
cpd_person_waiting_service__n4_31 = TabularCPD ('person_waiting_service__n4_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_30'], [2]);
cpd_person_waiting_service__n4_32 = TabularCPD ('person_waiting_service__n4_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_31'], [2]);
cpd_person_waiting_service__n4_33 = TabularCPD ('person_waiting_service__n4_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_32'], [2]);
cpd_person_waiting_service__n4_34 = TabularCPD ('person_waiting_service__n4_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_33'], [2]);
cpd_person_waiting_service__n4_35 = TabularCPD ('person_waiting_service__n4_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_34'], [2]);
cpd_person_waiting_service__n4_36 = TabularCPD ('person_waiting_service__n4_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_35'], [2]);
cpd_person_waiting_service__n4_37 = TabularCPD ('person_waiting_service__n4_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_36'], [2]);
cpd_person_waiting_service__n4_38 = TabularCPD ('person_waiting_service__n4_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_37'], [2]);
cpd_person_waiting_service__n4_39 = TabularCPD ('person_waiting_service__n4_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n4_38'], [2]);

cpd_person_waiting_service__n1_1 = TabularCPD ('person_waiting_service__n1_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_0'], [2]);
cpd_person_waiting_service__n1_2 = TabularCPD ('person_waiting_service__n1_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_1'], [2]);
cpd_person_waiting_service__n1_3 = TabularCPD ('person_waiting_service__n1_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_2'], [2]);
cpd_person_waiting_service__n1_4 = TabularCPD ('person_waiting_service__n1_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_3'], [2]);
cpd_person_waiting_service__n1_5 = TabularCPD ('person_waiting_service__n1_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_4'], [2]);
cpd_person_waiting_service__n1_6 = TabularCPD ('person_waiting_service__n1_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_5'], [2]);
cpd_person_waiting_service__n1_7 = TabularCPD ('person_waiting_service__n1_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_6'], [2]);
cpd_person_waiting_service__n1_8 = TabularCPD ('person_waiting_service__n1_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_7'], [2]);
cpd_person_waiting_service__n1_9 = TabularCPD ('person_waiting_service__n1_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_8'], [2]);
cpd_person_waiting_service__n1_10 = TabularCPD ('person_waiting_service__n1_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_9'], [2]);
cpd_person_waiting_service__n1_11 = TabularCPD ('person_waiting_service__n1_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_10'], [2]);
cpd_person_waiting_service__n1_12 = TabularCPD ('person_waiting_service__n1_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_11'], [2]);
cpd_person_waiting_service__n1_13 = TabularCPD ('person_waiting_service__n1_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_12'], [2]);
cpd_person_waiting_service__n1_14 = TabularCPD ('person_waiting_service__n1_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_13'], [2]);
cpd_person_waiting_service__n1_15 = TabularCPD ('person_waiting_service__n1_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_14'], [2]);
cpd_person_waiting_service__n1_16 = TabularCPD ('person_waiting_service__n1_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_15'], [2]);
cpd_person_waiting_service__n1_17 = TabularCPD ('person_waiting_service__n1_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_16'], [2]);
cpd_person_waiting_service__n1_18 = TabularCPD ('person_waiting_service__n1_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_17'], [2]);
cpd_person_waiting_service__n1_19 = TabularCPD ('person_waiting_service__n1_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_18'], [2]);
cpd_person_waiting_service__n1_20 = TabularCPD ('person_waiting_service__n1_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_19'], [2]);
cpd_person_waiting_service__n1_21 = TabularCPD ('person_waiting_service__n1_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_20'], [2]);
cpd_person_waiting_service__n1_22 = TabularCPD ('person_waiting_service__n1_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_21'], [2]);
cpd_person_waiting_service__n1_23 = TabularCPD ('person_waiting_service__n1_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_22'], [2]);
cpd_person_waiting_service__n1_24 = TabularCPD ('person_waiting_service__n1_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_23'], [2]);
cpd_person_waiting_service__n1_25 = TabularCPD ('person_waiting_service__n1_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_24'], [2]);
cpd_person_waiting_service__n1_26 = TabularCPD ('person_waiting_service__n1_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_25'], [2]);
cpd_person_waiting_service__n1_27 = TabularCPD ('person_waiting_service__n1_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_26'], [2]);
cpd_person_waiting_service__n1_28 = TabularCPD ('person_waiting_service__n1_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_27'], [2]);
cpd_person_waiting_service__n1_29 = TabularCPD ('person_waiting_service__n1_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_28'], [2]);
cpd_person_waiting_service__n1_30 = TabularCPD ('person_waiting_service__n1_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_29'], [2]);
cpd_person_waiting_service__n1_31 = TabularCPD ('person_waiting_service__n1_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_30'], [2]);
cpd_person_waiting_service__n1_32 = TabularCPD ('person_waiting_service__n1_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_31'], [2]);
cpd_person_waiting_service__n1_33 = TabularCPD ('person_waiting_service__n1_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_32'], [2]);
cpd_person_waiting_service__n1_34 = TabularCPD ('person_waiting_service__n1_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_33'], [2]);
cpd_person_waiting_service__n1_35 = TabularCPD ('person_waiting_service__n1_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_34'], [2]);
cpd_person_waiting_service__n1_36 = TabularCPD ('person_waiting_service__n1_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_35'], [2]);
cpd_person_waiting_service__n1_37 = TabularCPD ('person_waiting_service__n1_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_36'], [2]);
cpd_person_waiting_service__n1_38 = TabularCPD ('person_waiting_service__n1_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_37'], [2]);
cpd_person_waiting_service__n1_39 = TabularCPD ('person_waiting_service__n1_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n1_38'], [2]);

cpd_person_waiting_service__n2_1 = TabularCPD ('person_waiting_service__n2_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_0'], [2]);
cpd_person_waiting_service__n2_2 = TabularCPD ('person_waiting_service__n2_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_1'], [2]);
cpd_person_waiting_service__n2_3 = TabularCPD ('person_waiting_service__n2_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_2'], [2]);
cpd_person_waiting_service__n2_4 = TabularCPD ('person_waiting_service__n2_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_3'], [2]);
cpd_person_waiting_service__n2_5 = TabularCPD ('person_waiting_service__n2_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_4'], [2]);
cpd_person_waiting_service__n2_6 = TabularCPD ('person_waiting_service__n2_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_5'], [2]);
cpd_person_waiting_service__n2_7 = TabularCPD ('person_waiting_service__n2_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_6'], [2]);
cpd_person_waiting_service__n2_8 = TabularCPD ('person_waiting_service__n2_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_7'], [2]);
cpd_person_waiting_service__n2_9 = TabularCPD ('person_waiting_service__n2_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_8'], [2]);
cpd_person_waiting_service__n2_10 = TabularCPD ('person_waiting_service__n2_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_9'], [2]);
cpd_person_waiting_service__n2_11 = TabularCPD ('person_waiting_service__n2_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_10'], [2]);
cpd_person_waiting_service__n2_12 = TabularCPD ('person_waiting_service__n2_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_11'], [2]);
cpd_person_waiting_service__n2_13 = TabularCPD ('person_waiting_service__n2_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_12'], [2]);
cpd_person_waiting_service__n2_14 = TabularCPD ('person_waiting_service__n2_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_13'], [2]);
cpd_person_waiting_service__n2_15 = TabularCPD ('person_waiting_service__n2_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_14'], [2]);
cpd_person_waiting_service__n2_16 = TabularCPD ('person_waiting_service__n2_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_15'], [2]);
cpd_person_waiting_service__n2_17 = TabularCPD ('person_waiting_service__n2_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_16'], [2]);
cpd_person_waiting_service__n2_18 = TabularCPD ('person_waiting_service__n2_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_17'], [2]);
cpd_person_waiting_service__n2_19 = TabularCPD ('person_waiting_service__n2_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_18'], [2]);
cpd_person_waiting_service__n2_20 = TabularCPD ('person_waiting_service__n2_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_19'], [2]);
cpd_person_waiting_service__n2_21 = TabularCPD ('person_waiting_service__n2_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_20'], [2]);
cpd_person_waiting_service__n2_22 = TabularCPD ('person_waiting_service__n2_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_21'], [2]);
cpd_person_waiting_service__n2_23 = TabularCPD ('person_waiting_service__n2_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_22'], [2]);
cpd_person_waiting_service__n2_24 = TabularCPD ('person_waiting_service__n2_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_23'], [2]);
cpd_person_waiting_service__n2_25 = TabularCPD ('person_waiting_service__n2_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_24'], [2]);
cpd_person_waiting_service__n2_26 = TabularCPD ('person_waiting_service__n2_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_25'], [2]);
cpd_person_waiting_service__n2_27 = TabularCPD ('person_waiting_service__n2_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_26'], [2]);
cpd_person_waiting_service__n2_28 = TabularCPD ('person_waiting_service__n2_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_27'], [2]);
cpd_person_waiting_service__n2_29 = TabularCPD ('person_waiting_service__n2_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_28'], [2]);
cpd_person_waiting_service__n2_30 = TabularCPD ('person_waiting_service__n2_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_29'], [2]);
cpd_person_waiting_service__n2_31 = TabularCPD ('person_waiting_service__n2_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_30'], [2]);
cpd_person_waiting_service__n2_32 = TabularCPD ('person_waiting_service__n2_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_31'], [2]);
cpd_person_waiting_service__n2_33 = TabularCPD ('person_waiting_service__n2_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_32'], [2]);
cpd_person_waiting_service__n2_34 = TabularCPD ('person_waiting_service__n2_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_33'], [2]);
cpd_person_waiting_service__n2_35 = TabularCPD ('person_waiting_service__n2_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_34'], [2]);
cpd_person_waiting_service__n2_36 = TabularCPD ('person_waiting_service__n2_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_35'], [2]);
cpd_person_waiting_service__n2_37 = TabularCPD ('person_waiting_service__n2_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_36'], [2]);
cpd_person_waiting_service__n2_38 = TabularCPD ('person_waiting_service__n2_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_37'], [2]);
cpd_person_waiting_service__n2_39 = TabularCPD ('person_waiting_service__n2_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n2_38'], [2]);

cpd_person_waiting_service__n7_1 = TabularCPD ('person_waiting_service__n7_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_0'], [2]);
cpd_person_waiting_service__n7_2 = TabularCPD ('person_waiting_service__n7_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_1'], [2]);
cpd_person_waiting_service__n7_3 = TabularCPD ('person_waiting_service__n7_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_2'], [2]);
cpd_person_waiting_service__n7_4 = TabularCPD ('person_waiting_service__n7_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_3'], [2]);
cpd_person_waiting_service__n7_5 = TabularCPD ('person_waiting_service__n7_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_4'], [2]);
cpd_person_waiting_service__n7_6 = TabularCPD ('person_waiting_service__n7_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_5'], [2]);
cpd_person_waiting_service__n7_7 = TabularCPD ('person_waiting_service__n7_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_6'], [2]);
cpd_person_waiting_service__n7_8 = TabularCPD ('person_waiting_service__n7_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_7'], [2]);
cpd_person_waiting_service__n7_9 = TabularCPD ('person_waiting_service__n7_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_8'], [2]);
cpd_person_waiting_service__n7_10 = TabularCPD ('person_waiting_service__n7_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_9'], [2]);
cpd_person_waiting_service__n7_11 = TabularCPD ('person_waiting_service__n7_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_10'], [2]);
cpd_person_waiting_service__n7_12 = TabularCPD ('person_waiting_service__n7_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_11'], [2]);
cpd_person_waiting_service__n7_13 = TabularCPD ('person_waiting_service__n7_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_12'], [2]);
cpd_person_waiting_service__n7_14 = TabularCPD ('person_waiting_service__n7_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_13'], [2]);
cpd_person_waiting_service__n7_15 = TabularCPD ('person_waiting_service__n7_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_14'], [2]);
cpd_person_waiting_service__n7_16 = TabularCPD ('person_waiting_service__n7_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_15'], [2]);
cpd_person_waiting_service__n7_17 = TabularCPD ('person_waiting_service__n7_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_16'], [2]);
cpd_person_waiting_service__n7_18 = TabularCPD ('person_waiting_service__n7_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_17'], [2]);
cpd_person_waiting_service__n7_19 = TabularCPD ('person_waiting_service__n7_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_18'], [2]);
cpd_person_waiting_service__n7_20 = TabularCPD ('person_waiting_service__n7_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_19'], [2]);
cpd_person_waiting_service__n7_21 = TabularCPD ('person_waiting_service__n7_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_20'], [2]);
cpd_person_waiting_service__n7_22 = TabularCPD ('person_waiting_service__n7_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_21'], [2]);
cpd_person_waiting_service__n7_23 = TabularCPD ('person_waiting_service__n7_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_22'], [2]);
cpd_person_waiting_service__n7_24 = TabularCPD ('person_waiting_service__n7_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_23'], [2]);
cpd_person_waiting_service__n7_25 = TabularCPD ('person_waiting_service__n7_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_24'], [2]);
cpd_person_waiting_service__n7_26 = TabularCPD ('person_waiting_service__n7_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_25'], [2]);
cpd_person_waiting_service__n7_27 = TabularCPD ('person_waiting_service__n7_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_26'], [2]);
cpd_person_waiting_service__n7_28 = TabularCPD ('person_waiting_service__n7_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_27'], [2]);
cpd_person_waiting_service__n7_29 = TabularCPD ('person_waiting_service__n7_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_28'], [2]);
cpd_person_waiting_service__n7_30 = TabularCPD ('person_waiting_service__n7_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_29'], [2]);
cpd_person_waiting_service__n7_31 = TabularCPD ('person_waiting_service__n7_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_30'], [2]);
cpd_person_waiting_service__n7_32 = TabularCPD ('person_waiting_service__n7_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_31'], [2]);
cpd_person_waiting_service__n7_33 = TabularCPD ('person_waiting_service__n7_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_32'], [2]);
cpd_person_waiting_service__n7_34 = TabularCPD ('person_waiting_service__n7_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_33'], [2]);
cpd_person_waiting_service__n7_35 = TabularCPD ('person_waiting_service__n7_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_34'], [2]);
cpd_person_waiting_service__n7_36 = TabularCPD ('person_waiting_service__n7_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_35'], [2]);
cpd_person_waiting_service__n7_37 = TabularCPD ('person_waiting_service__n7_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_36'], [2]);
cpd_person_waiting_service__n7_38 = TabularCPD ('person_waiting_service__n7_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_37'], [2]);
cpd_person_waiting_service__n7_39 = TabularCPD ('person_waiting_service__n7_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n7_38'], [2]);

cpd_person_waiting_service__n8_1 = TabularCPD ('person_waiting_service__n8_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_0'], [2]);
cpd_person_waiting_service__n8_2 = TabularCPD ('person_waiting_service__n8_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_1'], [2]);
cpd_person_waiting_service__n8_3 = TabularCPD ('person_waiting_service__n8_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_2'], [2]);
cpd_person_waiting_service__n8_4 = TabularCPD ('person_waiting_service__n8_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_3'], [2]);
cpd_person_waiting_service__n8_5 = TabularCPD ('person_waiting_service__n8_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_4'], [2]);
cpd_person_waiting_service__n8_6 = TabularCPD ('person_waiting_service__n8_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_5'], [2]);
cpd_person_waiting_service__n8_7 = TabularCPD ('person_waiting_service__n8_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_6'], [2]);
cpd_person_waiting_service__n8_8 = TabularCPD ('person_waiting_service__n8_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_7'], [2]);
cpd_person_waiting_service__n8_9 = TabularCPD ('person_waiting_service__n8_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_8'], [2]);
cpd_person_waiting_service__n8_10 = TabularCPD ('person_waiting_service__n8_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_9'], [2]);
cpd_person_waiting_service__n8_11 = TabularCPD ('person_waiting_service__n8_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_10'], [2]);
cpd_person_waiting_service__n8_12 = TabularCPD ('person_waiting_service__n8_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_11'], [2]);
cpd_person_waiting_service__n8_13 = TabularCPD ('person_waiting_service__n8_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_12'], [2]);
cpd_person_waiting_service__n8_14 = TabularCPD ('person_waiting_service__n8_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_13'], [2]);
cpd_person_waiting_service__n8_15 = TabularCPD ('person_waiting_service__n8_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_14'], [2]);
cpd_person_waiting_service__n8_16 = TabularCPD ('person_waiting_service__n8_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_15'], [2]);
cpd_person_waiting_service__n8_17 = TabularCPD ('person_waiting_service__n8_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_16'], [2]);
cpd_person_waiting_service__n8_18 = TabularCPD ('person_waiting_service__n8_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_17'], [2]);
cpd_person_waiting_service__n8_19 = TabularCPD ('person_waiting_service__n8_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_18'], [2]);
cpd_person_waiting_service__n8_20 = TabularCPD ('person_waiting_service__n8_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_19'], [2]);
cpd_person_waiting_service__n8_21 = TabularCPD ('person_waiting_service__n8_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_20'], [2]);
cpd_person_waiting_service__n8_22 = TabularCPD ('person_waiting_service__n8_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_21'], [2]);
cpd_person_waiting_service__n8_23 = TabularCPD ('person_waiting_service__n8_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_22'], [2]);
cpd_person_waiting_service__n8_24 = TabularCPD ('person_waiting_service__n8_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_23'], [2]);
cpd_person_waiting_service__n8_25 = TabularCPD ('person_waiting_service__n8_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_24'], [2]);
cpd_person_waiting_service__n8_26 = TabularCPD ('person_waiting_service__n8_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_25'], [2]);
cpd_person_waiting_service__n8_27 = TabularCPD ('person_waiting_service__n8_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_26'], [2]);
cpd_person_waiting_service__n8_28 = TabularCPD ('person_waiting_service__n8_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_27'], [2]);
cpd_person_waiting_service__n8_29 = TabularCPD ('person_waiting_service__n8_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_28'], [2]);
cpd_person_waiting_service__n8_30 = TabularCPD ('person_waiting_service__n8_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_29'], [2]);
cpd_person_waiting_service__n8_31 = TabularCPD ('person_waiting_service__n8_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_30'], [2]);
cpd_person_waiting_service__n8_32 = TabularCPD ('person_waiting_service__n8_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_31'], [2]);
cpd_person_waiting_service__n8_33 = TabularCPD ('person_waiting_service__n8_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_32'], [2]);
cpd_person_waiting_service__n8_34 = TabularCPD ('person_waiting_service__n8_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_33'], [2]);
cpd_person_waiting_service__n8_35 = TabularCPD ('person_waiting_service__n8_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_34'], [2]);
cpd_person_waiting_service__n8_36 = TabularCPD ('person_waiting_service__n8_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_35'], [2]);
cpd_person_waiting_service__n8_37 = TabularCPD ('person_waiting_service__n8_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_36'], [2]);
cpd_person_waiting_service__n8_38 = TabularCPD ('person_waiting_service__n8_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_37'], [2]);
cpd_person_waiting_service__n8_39 = TabularCPD ('person_waiting_service__n8_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n8_38'], [2]);

cpd_person_waiting_service__n5_1 = TabularCPD ('person_waiting_service__n5_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_0'], [2]);
cpd_person_waiting_service__n5_2 = TabularCPD ('person_waiting_service__n5_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_1'], [2]);
cpd_person_waiting_service__n5_3 = TabularCPD ('person_waiting_service__n5_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_2'], [2]);
cpd_person_waiting_service__n5_4 = TabularCPD ('person_waiting_service__n5_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_3'], [2]);
cpd_person_waiting_service__n5_5 = TabularCPD ('person_waiting_service__n5_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_4'], [2]);
cpd_person_waiting_service__n5_6 = TabularCPD ('person_waiting_service__n5_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_5'], [2]);
cpd_person_waiting_service__n5_7 = TabularCPD ('person_waiting_service__n5_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_6'], [2]);
cpd_person_waiting_service__n5_8 = TabularCPD ('person_waiting_service__n5_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_7'], [2]);
cpd_person_waiting_service__n5_9 = TabularCPD ('person_waiting_service__n5_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_8'], [2]);
cpd_person_waiting_service__n5_10 = TabularCPD ('person_waiting_service__n5_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_9'], [2]);
cpd_person_waiting_service__n5_11 = TabularCPD ('person_waiting_service__n5_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_10'], [2]);
cpd_person_waiting_service__n5_12 = TabularCPD ('person_waiting_service__n5_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_11'], [2]);
cpd_person_waiting_service__n5_13 = TabularCPD ('person_waiting_service__n5_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_12'], [2]);
cpd_person_waiting_service__n5_14 = TabularCPD ('person_waiting_service__n5_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_13'], [2]);
cpd_person_waiting_service__n5_15 = TabularCPD ('person_waiting_service__n5_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_14'], [2]);
cpd_person_waiting_service__n5_16 = TabularCPD ('person_waiting_service__n5_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_15'], [2]);
cpd_person_waiting_service__n5_17 = TabularCPD ('person_waiting_service__n5_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_16'], [2]);
cpd_person_waiting_service__n5_18 = TabularCPD ('person_waiting_service__n5_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_17'], [2]);
cpd_person_waiting_service__n5_19 = TabularCPD ('person_waiting_service__n5_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_18'], [2]);
cpd_person_waiting_service__n5_20 = TabularCPD ('person_waiting_service__n5_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_19'], [2]);
cpd_person_waiting_service__n5_21 = TabularCPD ('person_waiting_service__n5_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_20'], [2]);
cpd_person_waiting_service__n5_22 = TabularCPD ('person_waiting_service__n5_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_21'], [2]);
cpd_person_waiting_service__n5_23 = TabularCPD ('person_waiting_service__n5_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_22'], [2]);
cpd_person_waiting_service__n5_24 = TabularCPD ('person_waiting_service__n5_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_23'], [2]);
cpd_person_waiting_service__n5_25 = TabularCPD ('person_waiting_service__n5_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_24'], [2]);
cpd_person_waiting_service__n5_26 = TabularCPD ('person_waiting_service__n5_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_25'], [2]);
cpd_person_waiting_service__n5_27 = TabularCPD ('person_waiting_service__n5_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_26'], [2]);
cpd_person_waiting_service__n5_28 = TabularCPD ('person_waiting_service__n5_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_27'], [2]);
cpd_person_waiting_service__n5_29 = TabularCPD ('person_waiting_service__n5_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_28'], [2]);
cpd_person_waiting_service__n5_30 = TabularCPD ('person_waiting_service__n5_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_29'], [2]);
cpd_person_waiting_service__n5_31 = TabularCPD ('person_waiting_service__n5_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_30'], [2]);
cpd_person_waiting_service__n5_32 = TabularCPD ('person_waiting_service__n5_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_31'], [2]);
cpd_person_waiting_service__n5_33 = TabularCPD ('person_waiting_service__n5_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_32'], [2]);
cpd_person_waiting_service__n5_34 = TabularCPD ('person_waiting_service__n5_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_33'], [2]);
cpd_person_waiting_service__n5_35 = TabularCPD ('person_waiting_service__n5_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_34'], [2]);
cpd_person_waiting_service__n5_36 = TabularCPD ('person_waiting_service__n5_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_35'], [2]);
cpd_person_waiting_service__n5_37 = TabularCPD ('person_waiting_service__n5_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_36'], [2]);
cpd_person_waiting_service__n5_38 = TabularCPD ('person_waiting_service__n5_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_37'], [2]);
cpd_person_waiting_service__n5_39 = TabularCPD ('person_waiting_service__n5_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n5_38'], [2]);

cpd_person_waiting_service__n6_1 = TabularCPD ('person_waiting_service__n6_1', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_0'], [2]);
cpd_person_waiting_service__n6_2 = TabularCPD ('person_waiting_service__n6_2', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_1'], [2]);
cpd_person_waiting_service__n6_3 = TabularCPD ('person_waiting_service__n6_3', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_2'], [2]);
cpd_person_waiting_service__n6_4 = TabularCPD ('person_waiting_service__n6_4', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_3'], [2]);
cpd_person_waiting_service__n6_5 = TabularCPD ('person_waiting_service__n6_5', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_4'], [2]);
cpd_person_waiting_service__n6_6 = TabularCPD ('person_waiting_service__n6_6', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_5'], [2]);
cpd_person_waiting_service__n6_7 = TabularCPD ('person_waiting_service__n6_7', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_6'], [2]);
cpd_person_waiting_service__n6_8 = TabularCPD ('person_waiting_service__n6_8', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_7'], [2]);
cpd_person_waiting_service__n6_9 = TabularCPD ('person_waiting_service__n6_9', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_8'], [2]);
cpd_person_waiting_service__n6_10 = TabularCPD ('person_waiting_service__n6_10', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_9'], [2]);
cpd_person_waiting_service__n6_11 = TabularCPD ('person_waiting_service__n6_11', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_10'], [2]);
cpd_person_waiting_service__n6_12 = TabularCPD ('person_waiting_service__n6_12', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_11'], [2]);
cpd_person_waiting_service__n6_13 = TabularCPD ('person_waiting_service__n6_13', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_12'], [2]);
cpd_person_waiting_service__n6_14 = TabularCPD ('person_waiting_service__n6_14', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_13'], [2]);
cpd_person_waiting_service__n6_15 = TabularCPD ('person_waiting_service__n6_15', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_14'], [2]);
cpd_person_waiting_service__n6_16 = TabularCPD ('person_waiting_service__n6_16', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_15'], [2]);
cpd_person_waiting_service__n6_17 = TabularCPD ('person_waiting_service__n6_17', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_16'], [2]);
cpd_person_waiting_service__n6_18 = TabularCPD ('person_waiting_service__n6_18', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_17'], [2]);
cpd_person_waiting_service__n6_19 = TabularCPD ('person_waiting_service__n6_19', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_18'], [2]);
cpd_person_waiting_service__n6_20 = TabularCPD ('person_waiting_service__n6_20', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_19'], [2]);
cpd_person_waiting_service__n6_21 = TabularCPD ('person_waiting_service__n6_21', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_20'], [2]);
cpd_person_waiting_service__n6_22 = TabularCPD ('person_waiting_service__n6_22', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_21'], [2]);
cpd_person_waiting_service__n6_23 = TabularCPD ('person_waiting_service__n6_23', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_22'], [2]);
cpd_person_waiting_service__n6_24 = TabularCPD ('person_waiting_service__n6_24', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_23'], [2]);
cpd_person_waiting_service__n6_25 = TabularCPD ('person_waiting_service__n6_25', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_24'], [2]);
cpd_person_waiting_service__n6_26 = TabularCPD ('person_waiting_service__n6_26', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_25'], [2]);
cpd_person_waiting_service__n6_27 = TabularCPD ('person_waiting_service__n6_27', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_26'], [2]);
cpd_person_waiting_service__n6_28 = TabularCPD ('person_waiting_service__n6_28', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_27'], [2]);
cpd_person_waiting_service__n6_29 = TabularCPD ('person_waiting_service__n6_29', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_28'], [2]);
cpd_person_waiting_service__n6_30 = TabularCPD ('person_waiting_service__n6_30', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_29'], [2]);
cpd_person_waiting_service__n6_31 = TabularCPD ('person_waiting_service__n6_31', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_30'], [2]);
cpd_person_waiting_service__n6_32 = TabularCPD ('person_waiting_service__n6_32', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_31'], [2]);
cpd_person_waiting_service__n6_33 = TabularCPD ('person_waiting_service__n6_33', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_32'], [2]);
cpd_person_waiting_service__n6_34 = TabularCPD ('person_waiting_service__n6_34', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_33'], [2]);
cpd_person_waiting_service__n6_35 = TabularCPD ('person_waiting_service__n6_35', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_34'], [2]);
cpd_person_waiting_service__n6_36 = TabularCPD ('person_waiting_service__n6_36', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_35'], [2]);
cpd_person_waiting_service__n6_37 = TabularCPD ('person_waiting_service__n6_37', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_36'], [2]);
cpd_person_waiting_service__n6_38 = TabularCPD ('person_waiting_service__n6_38', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_37'], [2]);
cpd_person_waiting_service__n6_39 = TabularCPD ('person_waiting_service__n6_39', 2, [[0.95, 0.0], [0.05, 1.0]], ['person_waiting_service__n6_38'], [2]);

cpd_ambulance_at_node__a1_n6_1 = TabularCPD ('ambulance_at_node__a1_n6_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_0'], [2]);
cpd_ambulance_at_node__a1_n6_2 = TabularCPD ('ambulance_at_node__a1_n6_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_1'], [2]);
cpd_ambulance_at_node__a1_n6_3 = TabularCPD ('ambulance_at_node__a1_n6_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_2'], [2]);
cpd_ambulance_at_node__a1_n6_4 = TabularCPD ('ambulance_at_node__a1_n6_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_3'], [2]);
cpd_ambulance_at_node__a1_n6_5 = TabularCPD ('ambulance_at_node__a1_n6_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_4'], [2]);
cpd_ambulance_at_node__a1_n6_6 = TabularCPD ('ambulance_at_node__a1_n6_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_5'], [2]);
cpd_ambulance_at_node__a1_n6_7 = TabularCPD ('ambulance_at_node__a1_n6_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_6'], [2]);
cpd_ambulance_at_node__a1_n6_8 = TabularCPD ('ambulance_at_node__a1_n6_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_7'], [2]);
cpd_ambulance_at_node__a1_n6_9 = TabularCPD ('ambulance_at_node__a1_n6_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_8'], [2]);
cpd_ambulance_at_node__a1_n6_10 = TabularCPD ('ambulance_at_node__a1_n6_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_9'], [2]);
cpd_ambulance_at_node__a1_n6_11 = TabularCPD ('ambulance_at_node__a1_n6_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_10'], [2]);
cpd_ambulance_at_node__a1_n6_12 = TabularCPD ('ambulance_at_node__a1_n6_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_11'], [2]);
cpd_ambulance_at_node__a1_n6_13 = TabularCPD ('ambulance_at_node__a1_n6_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_12'], [2]);
cpd_ambulance_at_node__a1_n6_14 = TabularCPD ('ambulance_at_node__a1_n6_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_13'], [2]);
cpd_ambulance_at_node__a1_n6_15 = TabularCPD ('ambulance_at_node__a1_n6_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_14'], [2]);
cpd_ambulance_at_node__a1_n6_16 = TabularCPD ('ambulance_at_node__a1_n6_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_15'], [2]);
cpd_ambulance_at_node__a1_n6_17 = TabularCPD ('ambulance_at_node__a1_n6_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_16'], [2]);
cpd_ambulance_at_node__a1_n6_18 = TabularCPD ('ambulance_at_node__a1_n6_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_17'], [2]);
cpd_ambulance_at_node__a1_n6_19 = TabularCPD ('ambulance_at_node__a1_n6_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_18'], [2]);
cpd_ambulance_at_node__a1_n6_20 = TabularCPD ('ambulance_at_node__a1_n6_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_19'], [2]);
cpd_ambulance_at_node__a1_n6_21 = TabularCPD ('ambulance_at_node__a1_n6_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_20'], [2]);
cpd_ambulance_at_node__a1_n6_22 = TabularCPD ('ambulance_at_node__a1_n6_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_21'], [2]);
cpd_ambulance_at_node__a1_n6_23 = TabularCPD ('ambulance_at_node__a1_n6_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_22'], [2]);
cpd_ambulance_at_node__a1_n6_24 = TabularCPD ('ambulance_at_node__a1_n6_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_23'], [2]);
cpd_ambulance_at_node__a1_n6_25 = TabularCPD ('ambulance_at_node__a1_n6_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_24'], [2]);
cpd_ambulance_at_node__a1_n6_26 = TabularCPD ('ambulance_at_node__a1_n6_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_25'], [2]);
cpd_ambulance_at_node__a1_n6_27 = TabularCPD ('ambulance_at_node__a1_n6_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_26'], [2]);
cpd_ambulance_at_node__a1_n6_28 = TabularCPD ('ambulance_at_node__a1_n6_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_27'], [2]);
cpd_ambulance_at_node__a1_n6_29 = TabularCPD ('ambulance_at_node__a1_n6_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_28'], [2]);
cpd_ambulance_at_node__a1_n6_30 = TabularCPD ('ambulance_at_node__a1_n6_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_29'], [2]);
cpd_ambulance_at_node__a1_n6_31 = TabularCPD ('ambulance_at_node__a1_n6_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_30'], [2]);
cpd_ambulance_at_node__a1_n6_32 = TabularCPD ('ambulance_at_node__a1_n6_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_31'], [2]);
cpd_ambulance_at_node__a1_n6_33 = TabularCPD ('ambulance_at_node__a1_n6_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_32'], [2]);
cpd_ambulance_at_node__a1_n6_34 = TabularCPD ('ambulance_at_node__a1_n6_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_33'], [2]);
cpd_ambulance_at_node__a1_n6_35 = TabularCPD ('ambulance_at_node__a1_n6_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_34'], [2]);
cpd_ambulance_at_node__a1_n6_36 = TabularCPD ('ambulance_at_node__a1_n6_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_35'], [2]);
cpd_ambulance_at_node__a1_n6_37 = TabularCPD ('ambulance_at_node__a1_n6_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_36'], [2]);
cpd_ambulance_at_node__a1_n6_38 = TabularCPD ('ambulance_at_node__a1_n6_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_37'], [2]);
cpd_ambulance_at_node__a1_n6_39 = TabularCPD ('ambulance_at_node__a1_n6_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n6_38'], [2]);

cpd_ambulance_at_node__a1_n7_1 = TabularCPD ('ambulance_at_node__a1_n7_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_0'], [2]);
cpd_ambulance_at_node__a1_n7_2 = TabularCPD ('ambulance_at_node__a1_n7_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_1'], [2]);
cpd_ambulance_at_node__a1_n7_3 = TabularCPD ('ambulance_at_node__a1_n7_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_2'], [2]);
cpd_ambulance_at_node__a1_n7_4 = TabularCPD ('ambulance_at_node__a1_n7_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_3'], [2]);
cpd_ambulance_at_node__a1_n7_5 = TabularCPD ('ambulance_at_node__a1_n7_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_4'], [2]);
cpd_ambulance_at_node__a1_n7_6 = TabularCPD ('ambulance_at_node__a1_n7_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_5'], [2]);
cpd_ambulance_at_node__a1_n7_7 = TabularCPD ('ambulance_at_node__a1_n7_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_6'], [2]);
cpd_ambulance_at_node__a1_n7_8 = TabularCPD ('ambulance_at_node__a1_n7_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_7'], [2]);
cpd_ambulance_at_node__a1_n7_9 = TabularCPD ('ambulance_at_node__a1_n7_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_8'], [2]);
cpd_ambulance_at_node__a1_n7_10 = TabularCPD ('ambulance_at_node__a1_n7_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_9'], [2]);
cpd_ambulance_at_node__a1_n7_11 = TabularCPD ('ambulance_at_node__a1_n7_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_10'], [2]);
cpd_ambulance_at_node__a1_n7_12 = TabularCPD ('ambulance_at_node__a1_n7_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_11'], [2]);
cpd_ambulance_at_node__a1_n7_13 = TabularCPD ('ambulance_at_node__a1_n7_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_12'], [2]);
cpd_ambulance_at_node__a1_n7_14 = TabularCPD ('ambulance_at_node__a1_n7_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_13'], [2]);
cpd_ambulance_at_node__a1_n7_15 = TabularCPD ('ambulance_at_node__a1_n7_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_14'], [2]);
cpd_ambulance_at_node__a1_n7_16 = TabularCPD ('ambulance_at_node__a1_n7_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_15'], [2]);
cpd_ambulance_at_node__a1_n7_17 = TabularCPD ('ambulance_at_node__a1_n7_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_16'], [2]);
cpd_ambulance_at_node__a1_n7_18 = TabularCPD ('ambulance_at_node__a1_n7_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_17'], [2]);
cpd_ambulance_at_node__a1_n7_19 = TabularCPD ('ambulance_at_node__a1_n7_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_18'], [2]);
cpd_ambulance_at_node__a1_n7_20 = TabularCPD ('ambulance_at_node__a1_n7_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_19'], [2]);
cpd_ambulance_at_node__a1_n7_21 = TabularCPD ('ambulance_at_node__a1_n7_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_20'], [2]);
cpd_ambulance_at_node__a1_n7_22 = TabularCPD ('ambulance_at_node__a1_n7_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_21'], [2]);
cpd_ambulance_at_node__a1_n7_23 = TabularCPD ('ambulance_at_node__a1_n7_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_22'], [2]);
cpd_ambulance_at_node__a1_n7_24 = TabularCPD ('ambulance_at_node__a1_n7_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_23'], [2]);
cpd_ambulance_at_node__a1_n7_25 = TabularCPD ('ambulance_at_node__a1_n7_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_24'], [2]);
cpd_ambulance_at_node__a1_n7_26 = TabularCPD ('ambulance_at_node__a1_n7_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_25'], [2]);
cpd_ambulance_at_node__a1_n7_27 = TabularCPD ('ambulance_at_node__a1_n7_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_26'], [2]);
cpd_ambulance_at_node__a1_n7_28 = TabularCPD ('ambulance_at_node__a1_n7_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_27'], [2]);
cpd_ambulance_at_node__a1_n7_29 = TabularCPD ('ambulance_at_node__a1_n7_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_28'], [2]);
cpd_ambulance_at_node__a1_n7_30 = TabularCPD ('ambulance_at_node__a1_n7_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_29'], [2]);
cpd_ambulance_at_node__a1_n7_31 = TabularCPD ('ambulance_at_node__a1_n7_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_30'], [2]);
cpd_ambulance_at_node__a1_n7_32 = TabularCPD ('ambulance_at_node__a1_n7_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_31'], [2]);
cpd_ambulance_at_node__a1_n7_33 = TabularCPD ('ambulance_at_node__a1_n7_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_32'], [2]);
cpd_ambulance_at_node__a1_n7_34 = TabularCPD ('ambulance_at_node__a1_n7_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_33'], [2]);
cpd_ambulance_at_node__a1_n7_35 = TabularCPD ('ambulance_at_node__a1_n7_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_34'], [2]);
cpd_ambulance_at_node__a1_n7_36 = TabularCPD ('ambulance_at_node__a1_n7_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_35'], [2]);
cpd_ambulance_at_node__a1_n7_37 = TabularCPD ('ambulance_at_node__a1_n7_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_36'], [2]);
cpd_ambulance_at_node__a1_n7_38 = TabularCPD ('ambulance_at_node__a1_n7_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_37'], [2]);
cpd_ambulance_at_node__a1_n7_39 = TabularCPD ('ambulance_at_node__a1_n7_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n7_38'], [2]);

cpd_ambulance_at_node__a1_n8_1 = TabularCPD ('ambulance_at_node__a1_n8_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_0'], [2]);
cpd_ambulance_at_node__a1_n8_2 = TabularCPD ('ambulance_at_node__a1_n8_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_1'], [2]);
cpd_ambulance_at_node__a1_n8_3 = TabularCPD ('ambulance_at_node__a1_n8_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_2'], [2]);
cpd_ambulance_at_node__a1_n8_4 = TabularCPD ('ambulance_at_node__a1_n8_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_3'], [2]);
cpd_ambulance_at_node__a1_n8_5 = TabularCPD ('ambulance_at_node__a1_n8_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_4'], [2]);
cpd_ambulance_at_node__a1_n8_6 = TabularCPD ('ambulance_at_node__a1_n8_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_5'], [2]);
cpd_ambulance_at_node__a1_n8_7 = TabularCPD ('ambulance_at_node__a1_n8_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_6'], [2]);
cpd_ambulance_at_node__a1_n8_8 = TabularCPD ('ambulance_at_node__a1_n8_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_7'], [2]);
cpd_ambulance_at_node__a1_n8_9 = TabularCPD ('ambulance_at_node__a1_n8_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_8'], [2]);
cpd_ambulance_at_node__a1_n8_10 = TabularCPD ('ambulance_at_node__a1_n8_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_9'], [2]);
cpd_ambulance_at_node__a1_n8_11 = TabularCPD ('ambulance_at_node__a1_n8_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_10'], [2]);
cpd_ambulance_at_node__a1_n8_12 = TabularCPD ('ambulance_at_node__a1_n8_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_11'], [2]);
cpd_ambulance_at_node__a1_n8_13 = TabularCPD ('ambulance_at_node__a1_n8_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_12'], [2]);
cpd_ambulance_at_node__a1_n8_14 = TabularCPD ('ambulance_at_node__a1_n8_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_13'], [2]);
cpd_ambulance_at_node__a1_n8_15 = TabularCPD ('ambulance_at_node__a1_n8_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_14'], [2]);
cpd_ambulance_at_node__a1_n8_16 = TabularCPD ('ambulance_at_node__a1_n8_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_15'], [2]);
cpd_ambulance_at_node__a1_n8_17 = TabularCPD ('ambulance_at_node__a1_n8_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_16'], [2]);
cpd_ambulance_at_node__a1_n8_18 = TabularCPD ('ambulance_at_node__a1_n8_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_17'], [2]);
cpd_ambulance_at_node__a1_n8_19 = TabularCPD ('ambulance_at_node__a1_n8_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_18'], [2]);
cpd_ambulance_at_node__a1_n8_20 = TabularCPD ('ambulance_at_node__a1_n8_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_19'], [2]);
cpd_ambulance_at_node__a1_n8_21 = TabularCPD ('ambulance_at_node__a1_n8_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_20'], [2]);
cpd_ambulance_at_node__a1_n8_22 = TabularCPD ('ambulance_at_node__a1_n8_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_21'], [2]);
cpd_ambulance_at_node__a1_n8_23 = TabularCPD ('ambulance_at_node__a1_n8_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_22'], [2]);
cpd_ambulance_at_node__a1_n8_24 = TabularCPD ('ambulance_at_node__a1_n8_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_23'], [2]);
cpd_ambulance_at_node__a1_n8_25 = TabularCPD ('ambulance_at_node__a1_n8_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_24'], [2]);
cpd_ambulance_at_node__a1_n8_26 = TabularCPD ('ambulance_at_node__a1_n8_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_25'], [2]);
cpd_ambulance_at_node__a1_n8_27 = TabularCPD ('ambulance_at_node__a1_n8_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_26'], [2]);
cpd_ambulance_at_node__a1_n8_28 = TabularCPD ('ambulance_at_node__a1_n8_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_27'], [2]);
cpd_ambulance_at_node__a1_n8_29 = TabularCPD ('ambulance_at_node__a1_n8_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_28'], [2]);
cpd_ambulance_at_node__a1_n8_30 = TabularCPD ('ambulance_at_node__a1_n8_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_29'], [2]);
cpd_ambulance_at_node__a1_n8_31 = TabularCPD ('ambulance_at_node__a1_n8_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_30'], [2]);
cpd_ambulance_at_node__a1_n8_32 = TabularCPD ('ambulance_at_node__a1_n8_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_31'], [2]);
cpd_ambulance_at_node__a1_n8_33 = TabularCPD ('ambulance_at_node__a1_n8_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_32'], [2]);
cpd_ambulance_at_node__a1_n8_34 = TabularCPD ('ambulance_at_node__a1_n8_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_33'], [2]);
cpd_ambulance_at_node__a1_n8_35 = TabularCPD ('ambulance_at_node__a1_n8_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_34'], [2]);
cpd_ambulance_at_node__a1_n8_36 = TabularCPD ('ambulance_at_node__a1_n8_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_35'], [2]);
cpd_ambulance_at_node__a1_n8_37 = TabularCPD ('ambulance_at_node__a1_n8_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_36'], [2]);
cpd_ambulance_at_node__a1_n8_38 = TabularCPD ('ambulance_at_node__a1_n8_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_37'], [2]);
cpd_ambulance_at_node__a1_n8_39 = TabularCPD ('ambulance_at_node__a1_n8_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n8_38'], [2]);

cpd_ambulance_at_node__a1_n2_1 = TabularCPD ('ambulance_at_node__a1_n2_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_0'], [2]);
cpd_ambulance_at_node__a1_n2_2 = TabularCPD ('ambulance_at_node__a1_n2_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_1'], [2]);
cpd_ambulance_at_node__a1_n2_3 = TabularCPD ('ambulance_at_node__a1_n2_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_2'], [2]);
cpd_ambulance_at_node__a1_n2_4 = TabularCPD ('ambulance_at_node__a1_n2_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_3'], [2]);
cpd_ambulance_at_node__a1_n2_5 = TabularCPD ('ambulance_at_node__a1_n2_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_4'], [2]);
cpd_ambulance_at_node__a1_n2_6 = TabularCPD ('ambulance_at_node__a1_n2_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_5'], [2]);
cpd_ambulance_at_node__a1_n2_7 = TabularCPD ('ambulance_at_node__a1_n2_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_6'], [2]);
cpd_ambulance_at_node__a1_n2_8 = TabularCPD ('ambulance_at_node__a1_n2_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_7'], [2]);
cpd_ambulance_at_node__a1_n2_9 = TabularCPD ('ambulance_at_node__a1_n2_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_8'], [2]);
cpd_ambulance_at_node__a1_n2_10 = TabularCPD ('ambulance_at_node__a1_n2_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_9'], [2]);
cpd_ambulance_at_node__a1_n2_11 = TabularCPD ('ambulance_at_node__a1_n2_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_10'], [2]);
cpd_ambulance_at_node__a1_n2_12 = TabularCPD ('ambulance_at_node__a1_n2_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_11'], [2]);
cpd_ambulance_at_node__a1_n2_13 = TabularCPD ('ambulance_at_node__a1_n2_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_12'], [2]);
cpd_ambulance_at_node__a1_n2_14 = TabularCPD ('ambulance_at_node__a1_n2_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_13'], [2]);
cpd_ambulance_at_node__a1_n2_15 = TabularCPD ('ambulance_at_node__a1_n2_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_14'], [2]);
cpd_ambulance_at_node__a1_n2_16 = TabularCPD ('ambulance_at_node__a1_n2_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_15'], [2]);
cpd_ambulance_at_node__a1_n2_17 = TabularCPD ('ambulance_at_node__a1_n2_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_16'], [2]);
cpd_ambulance_at_node__a1_n2_18 = TabularCPD ('ambulance_at_node__a1_n2_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_17'], [2]);
cpd_ambulance_at_node__a1_n2_19 = TabularCPD ('ambulance_at_node__a1_n2_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_18'], [2]);
cpd_ambulance_at_node__a1_n2_20 = TabularCPD ('ambulance_at_node__a1_n2_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_19'], [2]);
cpd_ambulance_at_node__a1_n2_21 = TabularCPD ('ambulance_at_node__a1_n2_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_20'], [2]);
cpd_ambulance_at_node__a1_n2_22 = TabularCPD ('ambulance_at_node__a1_n2_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_21'], [2]);
cpd_ambulance_at_node__a1_n2_23 = TabularCPD ('ambulance_at_node__a1_n2_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_22'], [2]);
cpd_ambulance_at_node__a1_n2_24 = TabularCPD ('ambulance_at_node__a1_n2_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_23'], [2]);
cpd_ambulance_at_node__a1_n2_25 = TabularCPD ('ambulance_at_node__a1_n2_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_24'], [2]);
cpd_ambulance_at_node__a1_n2_26 = TabularCPD ('ambulance_at_node__a1_n2_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_25'], [2]);
cpd_ambulance_at_node__a1_n2_27 = TabularCPD ('ambulance_at_node__a1_n2_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_26'], [2]);
cpd_ambulance_at_node__a1_n2_28 = TabularCPD ('ambulance_at_node__a1_n2_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_27'], [2]);
cpd_ambulance_at_node__a1_n2_29 = TabularCPD ('ambulance_at_node__a1_n2_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_28'], [2]);
cpd_ambulance_at_node__a1_n2_30 = TabularCPD ('ambulance_at_node__a1_n2_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_29'], [2]);
cpd_ambulance_at_node__a1_n2_31 = TabularCPD ('ambulance_at_node__a1_n2_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_30'], [2]);
cpd_ambulance_at_node__a1_n2_32 = TabularCPD ('ambulance_at_node__a1_n2_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_31'], [2]);
cpd_ambulance_at_node__a1_n2_33 = TabularCPD ('ambulance_at_node__a1_n2_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_32'], [2]);
cpd_ambulance_at_node__a1_n2_34 = TabularCPD ('ambulance_at_node__a1_n2_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_33'], [2]);
cpd_ambulance_at_node__a1_n2_35 = TabularCPD ('ambulance_at_node__a1_n2_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_34'], [2]);
cpd_ambulance_at_node__a1_n2_36 = TabularCPD ('ambulance_at_node__a1_n2_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_35'], [2]);
cpd_ambulance_at_node__a1_n2_37 = TabularCPD ('ambulance_at_node__a1_n2_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_36'], [2]);
cpd_ambulance_at_node__a1_n2_38 = TabularCPD ('ambulance_at_node__a1_n2_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_37'], [2]);
cpd_ambulance_at_node__a1_n2_39 = TabularCPD ('ambulance_at_node__a1_n2_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n2_38'], [2]);

cpd_ambulance_at_node__a1_n3_1 = TabularCPD ('ambulance_at_node__a1_n3_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_0'], [2]);
cpd_ambulance_at_node__a1_n3_2 = TabularCPD ('ambulance_at_node__a1_n3_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_1'], [2]);
cpd_ambulance_at_node__a1_n3_3 = TabularCPD ('ambulance_at_node__a1_n3_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_2'], [2]);
cpd_ambulance_at_node__a1_n3_4 = TabularCPD ('ambulance_at_node__a1_n3_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_3'], [2]);
cpd_ambulance_at_node__a1_n3_5 = TabularCPD ('ambulance_at_node__a1_n3_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_4'], [2]);
cpd_ambulance_at_node__a1_n3_6 = TabularCPD ('ambulance_at_node__a1_n3_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_5'], [2]);
cpd_ambulance_at_node__a1_n3_7 = TabularCPD ('ambulance_at_node__a1_n3_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_6'], [2]);
cpd_ambulance_at_node__a1_n3_8 = TabularCPD ('ambulance_at_node__a1_n3_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_7'], [2]);
cpd_ambulance_at_node__a1_n3_9 = TabularCPD ('ambulance_at_node__a1_n3_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_8'], [2]);
cpd_ambulance_at_node__a1_n3_10 = TabularCPD ('ambulance_at_node__a1_n3_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_9'], [2]);
cpd_ambulance_at_node__a1_n3_11 = TabularCPD ('ambulance_at_node__a1_n3_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_10'], [2]);
cpd_ambulance_at_node__a1_n3_12 = TabularCPD ('ambulance_at_node__a1_n3_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_11'], [2]);
cpd_ambulance_at_node__a1_n3_13 = TabularCPD ('ambulance_at_node__a1_n3_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_12'], [2]);
cpd_ambulance_at_node__a1_n3_14 = TabularCPD ('ambulance_at_node__a1_n3_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_13'], [2]);
cpd_ambulance_at_node__a1_n3_15 = TabularCPD ('ambulance_at_node__a1_n3_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_14'], [2]);
cpd_ambulance_at_node__a1_n3_16 = TabularCPD ('ambulance_at_node__a1_n3_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_15'], [2]);
cpd_ambulance_at_node__a1_n3_17 = TabularCPD ('ambulance_at_node__a1_n3_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_16'], [2]);
cpd_ambulance_at_node__a1_n3_18 = TabularCPD ('ambulance_at_node__a1_n3_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_17'], [2]);
cpd_ambulance_at_node__a1_n3_19 = TabularCPD ('ambulance_at_node__a1_n3_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_18'], [2]);
cpd_ambulance_at_node__a1_n3_20 = TabularCPD ('ambulance_at_node__a1_n3_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_19'], [2]);
cpd_ambulance_at_node__a1_n3_21 = TabularCPD ('ambulance_at_node__a1_n3_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_20'], [2]);
cpd_ambulance_at_node__a1_n3_22 = TabularCPD ('ambulance_at_node__a1_n3_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_21'], [2]);
cpd_ambulance_at_node__a1_n3_23 = TabularCPD ('ambulance_at_node__a1_n3_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_22'], [2]);
cpd_ambulance_at_node__a1_n3_24 = TabularCPD ('ambulance_at_node__a1_n3_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_23'], [2]);
cpd_ambulance_at_node__a1_n3_25 = TabularCPD ('ambulance_at_node__a1_n3_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_24'], [2]);
cpd_ambulance_at_node__a1_n3_26 = TabularCPD ('ambulance_at_node__a1_n3_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_25'], [2]);
cpd_ambulance_at_node__a1_n3_27 = TabularCPD ('ambulance_at_node__a1_n3_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_26'], [2]);
cpd_ambulance_at_node__a1_n3_28 = TabularCPD ('ambulance_at_node__a1_n3_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_27'], [2]);
cpd_ambulance_at_node__a1_n3_29 = TabularCPD ('ambulance_at_node__a1_n3_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_28'], [2]);
cpd_ambulance_at_node__a1_n3_30 = TabularCPD ('ambulance_at_node__a1_n3_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_29'], [2]);
cpd_ambulance_at_node__a1_n3_31 = TabularCPD ('ambulance_at_node__a1_n3_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_30'], [2]);
cpd_ambulance_at_node__a1_n3_32 = TabularCPD ('ambulance_at_node__a1_n3_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_31'], [2]);
cpd_ambulance_at_node__a1_n3_33 = TabularCPD ('ambulance_at_node__a1_n3_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_32'], [2]);
cpd_ambulance_at_node__a1_n3_34 = TabularCPD ('ambulance_at_node__a1_n3_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_33'], [2]);
cpd_ambulance_at_node__a1_n3_35 = TabularCPD ('ambulance_at_node__a1_n3_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_34'], [2]);
cpd_ambulance_at_node__a1_n3_36 = TabularCPD ('ambulance_at_node__a1_n3_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_35'], [2]);
cpd_ambulance_at_node__a1_n3_37 = TabularCPD ('ambulance_at_node__a1_n3_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_36'], [2]);
cpd_ambulance_at_node__a1_n3_38 = TabularCPD ('ambulance_at_node__a1_n3_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_37'], [2]);
cpd_ambulance_at_node__a1_n3_39 = TabularCPD ('ambulance_at_node__a1_n3_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n3_38'], [2]);

cpd_ambulance_at_node__a1_n4_1 = TabularCPD ('ambulance_at_node__a1_n4_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_0'], [2]);
cpd_ambulance_at_node__a1_n4_2 = TabularCPD ('ambulance_at_node__a1_n4_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_1'], [2]);
cpd_ambulance_at_node__a1_n4_3 = TabularCPD ('ambulance_at_node__a1_n4_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_2'], [2]);
cpd_ambulance_at_node__a1_n4_4 = TabularCPD ('ambulance_at_node__a1_n4_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_3'], [2]);
cpd_ambulance_at_node__a1_n4_5 = TabularCPD ('ambulance_at_node__a1_n4_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_4'], [2]);
cpd_ambulance_at_node__a1_n4_6 = TabularCPD ('ambulance_at_node__a1_n4_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_5'], [2]);
cpd_ambulance_at_node__a1_n4_7 = TabularCPD ('ambulance_at_node__a1_n4_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_6'], [2]);
cpd_ambulance_at_node__a1_n4_8 = TabularCPD ('ambulance_at_node__a1_n4_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_7'], [2]);
cpd_ambulance_at_node__a1_n4_9 = TabularCPD ('ambulance_at_node__a1_n4_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_8'], [2]);
cpd_ambulance_at_node__a1_n4_10 = TabularCPD ('ambulance_at_node__a1_n4_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_9'], [2]);
cpd_ambulance_at_node__a1_n4_11 = TabularCPD ('ambulance_at_node__a1_n4_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_10'], [2]);
cpd_ambulance_at_node__a1_n4_12 = TabularCPD ('ambulance_at_node__a1_n4_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_11'], [2]);
cpd_ambulance_at_node__a1_n4_13 = TabularCPD ('ambulance_at_node__a1_n4_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_12'], [2]);
cpd_ambulance_at_node__a1_n4_14 = TabularCPD ('ambulance_at_node__a1_n4_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_13'], [2]);
cpd_ambulance_at_node__a1_n4_15 = TabularCPD ('ambulance_at_node__a1_n4_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_14'], [2]);
cpd_ambulance_at_node__a1_n4_16 = TabularCPD ('ambulance_at_node__a1_n4_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_15'], [2]);
cpd_ambulance_at_node__a1_n4_17 = TabularCPD ('ambulance_at_node__a1_n4_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_16'], [2]);
cpd_ambulance_at_node__a1_n4_18 = TabularCPD ('ambulance_at_node__a1_n4_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_17'], [2]);
cpd_ambulance_at_node__a1_n4_19 = TabularCPD ('ambulance_at_node__a1_n4_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_18'], [2]);
cpd_ambulance_at_node__a1_n4_20 = TabularCPD ('ambulance_at_node__a1_n4_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_19'], [2]);
cpd_ambulance_at_node__a1_n4_21 = TabularCPD ('ambulance_at_node__a1_n4_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_20'], [2]);
cpd_ambulance_at_node__a1_n4_22 = TabularCPD ('ambulance_at_node__a1_n4_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_21'], [2]);
cpd_ambulance_at_node__a1_n4_23 = TabularCPD ('ambulance_at_node__a1_n4_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_22'], [2]);
cpd_ambulance_at_node__a1_n4_24 = TabularCPD ('ambulance_at_node__a1_n4_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_23'], [2]);
cpd_ambulance_at_node__a1_n4_25 = TabularCPD ('ambulance_at_node__a1_n4_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_24'], [2]);
cpd_ambulance_at_node__a1_n4_26 = TabularCPD ('ambulance_at_node__a1_n4_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_25'], [2]);
cpd_ambulance_at_node__a1_n4_27 = TabularCPD ('ambulance_at_node__a1_n4_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_26'], [2]);
cpd_ambulance_at_node__a1_n4_28 = TabularCPD ('ambulance_at_node__a1_n4_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_27'], [2]);
cpd_ambulance_at_node__a1_n4_29 = TabularCPD ('ambulance_at_node__a1_n4_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_28'], [2]);
cpd_ambulance_at_node__a1_n4_30 = TabularCPD ('ambulance_at_node__a1_n4_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_29'], [2]);
cpd_ambulance_at_node__a1_n4_31 = TabularCPD ('ambulance_at_node__a1_n4_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_30'], [2]);
cpd_ambulance_at_node__a1_n4_32 = TabularCPD ('ambulance_at_node__a1_n4_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_31'], [2]);
cpd_ambulance_at_node__a1_n4_33 = TabularCPD ('ambulance_at_node__a1_n4_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_32'], [2]);
cpd_ambulance_at_node__a1_n4_34 = TabularCPD ('ambulance_at_node__a1_n4_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_33'], [2]);
cpd_ambulance_at_node__a1_n4_35 = TabularCPD ('ambulance_at_node__a1_n4_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_34'], [2]);
cpd_ambulance_at_node__a1_n4_36 = TabularCPD ('ambulance_at_node__a1_n4_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_35'], [2]);
cpd_ambulance_at_node__a1_n4_37 = TabularCPD ('ambulance_at_node__a1_n4_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_36'], [2]);
cpd_ambulance_at_node__a1_n4_38 = TabularCPD ('ambulance_at_node__a1_n4_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_37'], [2]);
cpd_ambulance_at_node__a1_n4_39 = TabularCPD ('ambulance_at_node__a1_n4_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n4_38'], [2]);

cpd_ambulance_at_node__a1_n5_1 = TabularCPD ('ambulance_at_node__a1_n5_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_0'], [2]);
cpd_ambulance_at_node__a1_n5_2 = TabularCPD ('ambulance_at_node__a1_n5_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_1'], [2]);
cpd_ambulance_at_node__a1_n5_3 = TabularCPD ('ambulance_at_node__a1_n5_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_2'], [2]);
cpd_ambulance_at_node__a1_n5_4 = TabularCPD ('ambulance_at_node__a1_n5_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_3'], [2]);
cpd_ambulance_at_node__a1_n5_5 = TabularCPD ('ambulance_at_node__a1_n5_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_4'], [2]);
cpd_ambulance_at_node__a1_n5_6 = TabularCPD ('ambulance_at_node__a1_n5_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_5'], [2]);
cpd_ambulance_at_node__a1_n5_7 = TabularCPD ('ambulance_at_node__a1_n5_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_6'], [2]);
cpd_ambulance_at_node__a1_n5_8 = TabularCPD ('ambulance_at_node__a1_n5_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_7'], [2]);
cpd_ambulance_at_node__a1_n5_9 = TabularCPD ('ambulance_at_node__a1_n5_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_8'], [2]);
cpd_ambulance_at_node__a1_n5_10 = TabularCPD ('ambulance_at_node__a1_n5_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_9'], [2]);
cpd_ambulance_at_node__a1_n5_11 = TabularCPD ('ambulance_at_node__a1_n5_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_10'], [2]);
cpd_ambulance_at_node__a1_n5_12 = TabularCPD ('ambulance_at_node__a1_n5_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_11'], [2]);
cpd_ambulance_at_node__a1_n5_13 = TabularCPD ('ambulance_at_node__a1_n5_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_12'], [2]);
cpd_ambulance_at_node__a1_n5_14 = TabularCPD ('ambulance_at_node__a1_n5_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_13'], [2]);
cpd_ambulance_at_node__a1_n5_15 = TabularCPD ('ambulance_at_node__a1_n5_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_14'], [2]);
cpd_ambulance_at_node__a1_n5_16 = TabularCPD ('ambulance_at_node__a1_n5_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_15'], [2]);
cpd_ambulance_at_node__a1_n5_17 = TabularCPD ('ambulance_at_node__a1_n5_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_16'], [2]);
cpd_ambulance_at_node__a1_n5_18 = TabularCPD ('ambulance_at_node__a1_n5_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_17'], [2]);
cpd_ambulance_at_node__a1_n5_19 = TabularCPD ('ambulance_at_node__a1_n5_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_18'], [2]);
cpd_ambulance_at_node__a1_n5_20 = TabularCPD ('ambulance_at_node__a1_n5_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_19'], [2]);
cpd_ambulance_at_node__a1_n5_21 = TabularCPD ('ambulance_at_node__a1_n5_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_20'], [2]);
cpd_ambulance_at_node__a1_n5_22 = TabularCPD ('ambulance_at_node__a1_n5_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_21'], [2]);
cpd_ambulance_at_node__a1_n5_23 = TabularCPD ('ambulance_at_node__a1_n5_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_22'], [2]);
cpd_ambulance_at_node__a1_n5_24 = TabularCPD ('ambulance_at_node__a1_n5_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_23'], [2]);
cpd_ambulance_at_node__a1_n5_25 = TabularCPD ('ambulance_at_node__a1_n5_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_24'], [2]);
cpd_ambulance_at_node__a1_n5_26 = TabularCPD ('ambulance_at_node__a1_n5_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_25'], [2]);
cpd_ambulance_at_node__a1_n5_27 = TabularCPD ('ambulance_at_node__a1_n5_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_26'], [2]);
cpd_ambulance_at_node__a1_n5_28 = TabularCPD ('ambulance_at_node__a1_n5_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_27'], [2]);
cpd_ambulance_at_node__a1_n5_29 = TabularCPD ('ambulance_at_node__a1_n5_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_28'], [2]);
cpd_ambulance_at_node__a1_n5_30 = TabularCPD ('ambulance_at_node__a1_n5_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_29'], [2]);
cpd_ambulance_at_node__a1_n5_31 = TabularCPD ('ambulance_at_node__a1_n5_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_30'], [2]);
cpd_ambulance_at_node__a1_n5_32 = TabularCPD ('ambulance_at_node__a1_n5_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_31'], [2]);
cpd_ambulance_at_node__a1_n5_33 = TabularCPD ('ambulance_at_node__a1_n5_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_32'], [2]);
cpd_ambulance_at_node__a1_n5_34 = TabularCPD ('ambulance_at_node__a1_n5_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_33'], [2]);
cpd_ambulance_at_node__a1_n5_35 = TabularCPD ('ambulance_at_node__a1_n5_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_34'], [2]);
cpd_ambulance_at_node__a1_n5_36 = TabularCPD ('ambulance_at_node__a1_n5_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_35'], [2]);
cpd_ambulance_at_node__a1_n5_37 = TabularCPD ('ambulance_at_node__a1_n5_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_36'], [2]);
cpd_ambulance_at_node__a1_n5_38 = TabularCPD ('ambulance_at_node__a1_n5_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_37'], [2]);
cpd_ambulance_at_node__a1_n5_39 = TabularCPD ('ambulance_at_node__a1_n5_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n5_38'], [2]);

cpd_ambulance_at_node__a1_n0_1 = TabularCPD ('ambulance_at_node__a1_n0_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_0'], [2]);
cpd_ambulance_at_node__a1_n0_2 = TabularCPD ('ambulance_at_node__a1_n0_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_1'], [2]);
cpd_ambulance_at_node__a1_n0_3 = TabularCPD ('ambulance_at_node__a1_n0_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_2'], [2]);
cpd_ambulance_at_node__a1_n0_4 = TabularCPD ('ambulance_at_node__a1_n0_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_3'], [2]);
cpd_ambulance_at_node__a1_n0_5 = TabularCPD ('ambulance_at_node__a1_n0_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_4'], [2]);
cpd_ambulance_at_node__a1_n0_6 = TabularCPD ('ambulance_at_node__a1_n0_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_5'], [2]);
cpd_ambulance_at_node__a1_n0_7 = TabularCPD ('ambulance_at_node__a1_n0_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_6'], [2]);
cpd_ambulance_at_node__a1_n0_8 = TabularCPD ('ambulance_at_node__a1_n0_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_7'], [2]);
cpd_ambulance_at_node__a1_n0_9 = TabularCPD ('ambulance_at_node__a1_n0_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_8'], [2]);
cpd_ambulance_at_node__a1_n0_10 = TabularCPD ('ambulance_at_node__a1_n0_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_9'], [2]);
cpd_ambulance_at_node__a1_n0_11 = TabularCPD ('ambulance_at_node__a1_n0_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_10'], [2]);
cpd_ambulance_at_node__a1_n0_12 = TabularCPD ('ambulance_at_node__a1_n0_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_11'], [2]);
cpd_ambulance_at_node__a1_n0_13 = TabularCPD ('ambulance_at_node__a1_n0_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_12'], [2]);
cpd_ambulance_at_node__a1_n0_14 = TabularCPD ('ambulance_at_node__a1_n0_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_13'], [2]);
cpd_ambulance_at_node__a1_n0_15 = TabularCPD ('ambulance_at_node__a1_n0_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_14'], [2]);
cpd_ambulance_at_node__a1_n0_16 = TabularCPD ('ambulance_at_node__a1_n0_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_15'], [2]);
cpd_ambulance_at_node__a1_n0_17 = TabularCPD ('ambulance_at_node__a1_n0_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_16'], [2]);
cpd_ambulance_at_node__a1_n0_18 = TabularCPD ('ambulance_at_node__a1_n0_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_17'], [2]);
cpd_ambulance_at_node__a1_n0_19 = TabularCPD ('ambulance_at_node__a1_n0_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_18'], [2]);
cpd_ambulance_at_node__a1_n0_20 = TabularCPD ('ambulance_at_node__a1_n0_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_19'], [2]);
cpd_ambulance_at_node__a1_n0_21 = TabularCPD ('ambulance_at_node__a1_n0_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_20'], [2]);
cpd_ambulance_at_node__a1_n0_22 = TabularCPD ('ambulance_at_node__a1_n0_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_21'], [2]);
cpd_ambulance_at_node__a1_n0_23 = TabularCPD ('ambulance_at_node__a1_n0_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_22'], [2]);
cpd_ambulance_at_node__a1_n0_24 = TabularCPD ('ambulance_at_node__a1_n0_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_23'], [2]);
cpd_ambulance_at_node__a1_n0_25 = TabularCPD ('ambulance_at_node__a1_n0_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_24'], [2]);
cpd_ambulance_at_node__a1_n0_26 = TabularCPD ('ambulance_at_node__a1_n0_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_25'], [2]);
cpd_ambulance_at_node__a1_n0_27 = TabularCPD ('ambulance_at_node__a1_n0_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_26'], [2]);
cpd_ambulance_at_node__a1_n0_28 = TabularCPD ('ambulance_at_node__a1_n0_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_27'], [2]);
cpd_ambulance_at_node__a1_n0_29 = TabularCPD ('ambulance_at_node__a1_n0_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_28'], [2]);
cpd_ambulance_at_node__a1_n0_30 = TabularCPD ('ambulance_at_node__a1_n0_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_29'], [2]);
cpd_ambulance_at_node__a1_n0_31 = TabularCPD ('ambulance_at_node__a1_n0_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_30'], [2]);
cpd_ambulance_at_node__a1_n0_32 = TabularCPD ('ambulance_at_node__a1_n0_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_31'], [2]);
cpd_ambulance_at_node__a1_n0_33 = TabularCPD ('ambulance_at_node__a1_n0_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_32'], [2]);
cpd_ambulance_at_node__a1_n0_34 = TabularCPD ('ambulance_at_node__a1_n0_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_33'], [2]);
cpd_ambulance_at_node__a1_n0_35 = TabularCPD ('ambulance_at_node__a1_n0_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_34'], [2]);
cpd_ambulance_at_node__a1_n0_36 = TabularCPD ('ambulance_at_node__a1_n0_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_35'], [2]);
cpd_ambulance_at_node__a1_n0_37 = TabularCPD ('ambulance_at_node__a1_n0_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_36'], [2]);
cpd_ambulance_at_node__a1_n0_38 = TabularCPD ('ambulance_at_node__a1_n0_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_37'], [2]);
cpd_ambulance_at_node__a1_n0_39 = TabularCPD ('ambulance_at_node__a1_n0_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n0_38'], [2]);

cpd_ambulance_at_node__a1_n1_1 = TabularCPD ('ambulance_at_node__a1_n1_1', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_0'], [2]);
cpd_ambulance_at_node__a1_n1_2 = TabularCPD ('ambulance_at_node__a1_n1_2', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_1'], [2]);
cpd_ambulance_at_node__a1_n1_3 = TabularCPD ('ambulance_at_node__a1_n1_3', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_2'], [2]);
cpd_ambulance_at_node__a1_n1_4 = TabularCPD ('ambulance_at_node__a1_n1_4', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_3'], [2]);
cpd_ambulance_at_node__a1_n1_5 = TabularCPD ('ambulance_at_node__a1_n1_5', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_4'], [2]);
cpd_ambulance_at_node__a1_n1_6 = TabularCPD ('ambulance_at_node__a1_n1_6', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_5'], [2]);
cpd_ambulance_at_node__a1_n1_7 = TabularCPD ('ambulance_at_node__a1_n1_7', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_6'], [2]);
cpd_ambulance_at_node__a1_n1_8 = TabularCPD ('ambulance_at_node__a1_n1_8', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_7'], [2]);
cpd_ambulance_at_node__a1_n1_9 = TabularCPD ('ambulance_at_node__a1_n1_9', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_8'], [2]);
cpd_ambulance_at_node__a1_n1_10 = TabularCPD ('ambulance_at_node__a1_n1_10', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_9'], [2]);
cpd_ambulance_at_node__a1_n1_11 = TabularCPD ('ambulance_at_node__a1_n1_11', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_10'], [2]);
cpd_ambulance_at_node__a1_n1_12 = TabularCPD ('ambulance_at_node__a1_n1_12', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_11'], [2]);
cpd_ambulance_at_node__a1_n1_13 = TabularCPD ('ambulance_at_node__a1_n1_13', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_12'], [2]);
cpd_ambulance_at_node__a1_n1_14 = TabularCPD ('ambulance_at_node__a1_n1_14', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_13'], [2]);
cpd_ambulance_at_node__a1_n1_15 = TabularCPD ('ambulance_at_node__a1_n1_15', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_14'], [2]);
cpd_ambulance_at_node__a1_n1_16 = TabularCPD ('ambulance_at_node__a1_n1_16', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_15'], [2]);
cpd_ambulance_at_node__a1_n1_17 = TabularCPD ('ambulance_at_node__a1_n1_17', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_16'], [2]);
cpd_ambulance_at_node__a1_n1_18 = TabularCPD ('ambulance_at_node__a1_n1_18', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_17'], [2]);
cpd_ambulance_at_node__a1_n1_19 = TabularCPD ('ambulance_at_node__a1_n1_19', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_18'], [2]);
cpd_ambulance_at_node__a1_n1_20 = TabularCPD ('ambulance_at_node__a1_n1_20', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_19'], [2]);
cpd_ambulance_at_node__a1_n1_21 = TabularCPD ('ambulance_at_node__a1_n1_21', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_20'], [2]);
cpd_ambulance_at_node__a1_n1_22 = TabularCPD ('ambulance_at_node__a1_n1_22', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_21'], [2]);
cpd_ambulance_at_node__a1_n1_23 = TabularCPD ('ambulance_at_node__a1_n1_23', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_22'], [2]);
cpd_ambulance_at_node__a1_n1_24 = TabularCPD ('ambulance_at_node__a1_n1_24', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_23'], [2]);
cpd_ambulance_at_node__a1_n1_25 = TabularCPD ('ambulance_at_node__a1_n1_25', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_24'], [2]);
cpd_ambulance_at_node__a1_n1_26 = TabularCPD ('ambulance_at_node__a1_n1_26', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_25'], [2]);
cpd_ambulance_at_node__a1_n1_27 = TabularCPD ('ambulance_at_node__a1_n1_27', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_26'], [2]);
cpd_ambulance_at_node__a1_n1_28 = TabularCPD ('ambulance_at_node__a1_n1_28', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_27'], [2]);
cpd_ambulance_at_node__a1_n1_29 = TabularCPD ('ambulance_at_node__a1_n1_29', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_28'], [2]);
cpd_ambulance_at_node__a1_n1_30 = TabularCPD ('ambulance_at_node__a1_n1_30', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_29'], [2]);
cpd_ambulance_at_node__a1_n1_31 = TabularCPD ('ambulance_at_node__a1_n1_31', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_30'], [2]);
cpd_ambulance_at_node__a1_n1_32 = TabularCPD ('ambulance_at_node__a1_n1_32', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_31'], [2]);
cpd_ambulance_at_node__a1_n1_33 = TabularCPD ('ambulance_at_node__a1_n1_33', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_32'], [2]);
cpd_ambulance_at_node__a1_n1_34 = TabularCPD ('ambulance_at_node__a1_n1_34', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_33'], [2]);
cpd_ambulance_at_node__a1_n1_35 = TabularCPD ('ambulance_at_node__a1_n1_35', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_34'], [2]);
cpd_ambulance_at_node__a1_n1_36 = TabularCPD ('ambulance_at_node__a1_n1_36', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_35'], [2]);
cpd_ambulance_at_node__a1_n1_37 = TabularCPD ('ambulance_at_node__a1_n1_37', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_36'], [2]);
cpd_ambulance_at_node__a1_n1_38 = TabularCPD ('ambulance_at_node__a1_n1_38', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_37'], [2]);
cpd_ambulance_at_node__a1_n1_39 = TabularCPD ('ambulance_at_node__a1_n1_39', 2, [[1.0, 0.0], [0.0, 1.0]], ['ambulance_at_node__a1_n1_38'], [2]);

ambulance_mdp_model.add_cpds(cpd_person_in_ambulance__a0_0,
                             cpd_person_in_ambulance__a1_0,
                             cpd_ambulance_at_node__a0_n0_0,
                             cpd_ambulance_at_node__a0_n1_0,
                             cpd_ambulance_at_node__a0_n2_0,
                             cpd_ambulance_at_node__a0_n3_0,
                             cpd_ambulance_at_node__a0_n4_0,
                             cpd_ambulance_at_node__a0_n5_0,
                             cpd_ambulance_at_node__a0_n6_0,
                             cpd_ambulance_at_node__a0_n7_0,
                             cpd_ambulance_at_node__a0_n8_0,
                             cpd_ambulance_at_node__a1_n0_0,
                             cpd_ambulance_at_node__a1_n1_0,
                             cpd_ambulance_at_node__a1_n2_0,
                             cpd_ambulance_at_node__a1_n3_0,
                             cpd_ambulance_at_node__a1_n4_0,
                             cpd_ambulance_at_node__a1_n5_0,
                             cpd_ambulance_at_node__a1_n6_0,
                             cpd_ambulance_at_node__a1_n7_0,
                             cpd_ambulance_at_node__a1_n8_0,
                             cpd_person_waiting_service__n0_0,
                             cpd_person_waiting_service__n1_0,
                             cpd_person_waiting_service__n2_0,
                             cpd_person_waiting_service__n3_0,
                             cpd_person_waiting_service__n4_0,
                             cpd_person_waiting_service__n5_0,
                             cpd_person_waiting_service__n6_0,
                             cpd_person_waiting_service__n7_0,
                             cpd_person_waiting_service__n8_0,
                             cpd_person_in_ambulance__a0_1,
                             cpd_person_in_ambulance__a1_1,
                             cpd_ambulance_at_node__a0_n0_1,
                             cpd_ambulance_at_node__a0_n1_1,
                             cpd_ambulance_at_node__a0_n2_1,
                             cpd_ambulance_at_node__a0_n3_1,
                             cpd_ambulance_at_node__a0_n4_1,
                             cpd_ambulance_at_node__a0_n5_1,
                             cpd_ambulance_at_node__a0_n6_1,
                             cpd_ambulance_at_node__a0_n7_1,
                             cpd_ambulance_at_node__a0_n8_1,
                             cpd_ambulance_at_node__a1_n0_1,
                             cpd_ambulance_at_node__a1_n1_1,
                             cpd_ambulance_at_node__a1_n2_1,
                             cpd_ambulance_at_node__a1_n3_1,
                             cpd_ambulance_at_node__a1_n4_1,
                             cpd_ambulance_at_node__a1_n5_1,
                             cpd_ambulance_at_node__a1_n6_1,
                             cpd_ambulance_at_node__a1_n7_1,
                             cpd_ambulance_at_node__a1_n8_1,
                             cpd_person_waiting_service__n0_1,
                             cpd_person_waiting_service__n1_1,
                             cpd_person_waiting_service__n2_1,
                             cpd_person_waiting_service__n3_1,
                             cpd_person_waiting_service__n4_1,
                             cpd_person_waiting_service__n5_1,
                             cpd_person_waiting_service__n6_1,
                             cpd_person_waiting_service__n7_1,
                             cpd_person_waiting_service__n8_1,
                             cpd_person_in_ambulance__a0_2,
                             cpd_person_in_ambulance__a1_2,
                             cpd_ambulance_at_node__a0_n0_2,
                             cpd_ambulance_at_node__a0_n1_2,
                             cpd_ambulance_at_node__a0_n2_2,
                             cpd_ambulance_at_node__a0_n3_2,
                             cpd_ambulance_at_node__a0_n4_2,
                             cpd_ambulance_at_node__a0_n5_2,
                             cpd_ambulance_at_node__a0_n6_2,
                             cpd_ambulance_at_node__a0_n7_2,
                             cpd_ambulance_at_node__a0_n8_2,
                             cpd_ambulance_at_node__a1_n0_2,
                             cpd_ambulance_at_node__a1_n1_2,
                             cpd_ambulance_at_node__a1_n2_2,
                             cpd_ambulance_at_node__a1_n3_2,
                             cpd_ambulance_at_node__a1_n4_2,
                             cpd_ambulance_at_node__a1_n5_2,
                             cpd_ambulance_at_node__a1_n6_2,
                             cpd_ambulance_at_node__a1_n7_2,
                             cpd_ambulance_at_node__a1_n8_2,
                             cpd_person_waiting_service__n0_2,
                             cpd_person_waiting_service__n1_2,
                             cpd_person_waiting_service__n2_2,
                             cpd_person_waiting_service__n3_2,
                             cpd_person_waiting_service__n4_2,
                             cpd_person_waiting_service__n5_2,
                             cpd_person_waiting_service__n6_2,
                             cpd_person_waiting_service__n7_2,
                             cpd_person_waiting_service__n8_2,
                             cpd_person_in_ambulance__a0_3,
                             cpd_person_in_ambulance__a1_3,
                             cpd_ambulance_at_node__a0_n0_3,
                             cpd_ambulance_at_node__a0_n1_3,
                             cpd_ambulance_at_node__a0_n2_3,
                             cpd_ambulance_at_node__a0_n3_3,
                             cpd_ambulance_at_node__a0_n4_3,
                             cpd_ambulance_at_node__a0_n5_3,
                             cpd_ambulance_at_node__a0_n6_3,
                             cpd_ambulance_at_node__a0_n7_3,
                             cpd_ambulance_at_node__a0_n8_3,
                             cpd_ambulance_at_node__a1_n0_3,
                             cpd_ambulance_at_node__a1_n1_3,
                             cpd_ambulance_at_node__a1_n2_3,
                             cpd_ambulance_at_node__a1_n3_3,
                             cpd_ambulance_at_node__a1_n4_3,
                             cpd_ambulance_at_node__a1_n5_3,
                             cpd_ambulance_at_node__a1_n6_3,
                             cpd_ambulance_at_node__a1_n7_3,
                             cpd_ambulance_at_node__a1_n8_3,
                             cpd_person_waiting_service__n0_3,
                             cpd_person_waiting_service__n1_3,
                             cpd_person_waiting_service__n2_3,
                             cpd_person_waiting_service__n3_3,
                             cpd_person_waiting_service__n4_3,
                             cpd_person_waiting_service__n5_3,
                             cpd_person_waiting_service__n6_3,
                             cpd_person_waiting_service__n7_3,
                             cpd_person_waiting_service__n8_3,
                             cpd_person_in_ambulance__a0_4,
                             cpd_person_in_ambulance__a1_4,
                             cpd_ambulance_at_node__a0_n0_4,
                             cpd_ambulance_at_node__a0_n1_4,
                             cpd_ambulance_at_node__a0_n2_4,
                             cpd_ambulance_at_node__a0_n3_4,
                             cpd_ambulance_at_node__a0_n4_4,
                             cpd_ambulance_at_node__a0_n5_4,
                             cpd_ambulance_at_node__a0_n6_4,
                             cpd_ambulance_at_node__a0_n7_4,
                             cpd_ambulance_at_node__a0_n8_4,
                             cpd_ambulance_at_node__a1_n0_4,
                             cpd_ambulance_at_node__a1_n1_4,
                             cpd_ambulance_at_node__a1_n2_4,
                             cpd_ambulance_at_node__a1_n3_4,
                             cpd_ambulance_at_node__a1_n4_4,
                             cpd_ambulance_at_node__a1_n5_4,
                             cpd_ambulance_at_node__a1_n6_4,
                             cpd_ambulance_at_node__a1_n7_4,
                             cpd_ambulance_at_node__a1_n8_4,
                             cpd_person_waiting_service__n0_4,
                             cpd_person_waiting_service__n1_4,
                             cpd_person_waiting_service__n2_4,
                             cpd_person_waiting_service__n3_4,
                             cpd_person_waiting_service__n4_4,
                             cpd_person_waiting_service__n5_4,
                             cpd_person_waiting_service__n6_4,
                             cpd_person_waiting_service__n7_4,
                             cpd_person_waiting_service__n8_4,
                             cpd_person_in_ambulance__a0_5,
                             cpd_person_in_ambulance__a1_5,
                             cpd_ambulance_at_node__a0_n0_5,
                             cpd_ambulance_at_node__a0_n1_5,
                             cpd_ambulance_at_node__a0_n2_5,
                             cpd_ambulance_at_node__a0_n3_5,
                             cpd_ambulance_at_node__a0_n4_5,
                             cpd_ambulance_at_node__a0_n5_5,
                             cpd_ambulance_at_node__a0_n6_5,
                             cpd_ambulance_at_node__a0_n7_5,
                             cpd_ambulance_at_node__a0_n8_5,
                             cpd_ambulance_at_node__a1_n0_5,
                             cpd_ambulance_at_node__a1_n1_5,
                             cpd_ambulance_at_node__a1_n2_5,
                             cpd_ambulance_at_node__a1_n3_5,
                             cpd_ambulance_at_node__a1_n4_5,
                             cpd_ambulance_at_node__a1_n5_5,
                             cpd_ambulance_at_node__a1_n6_5,
                             cpd_ambulance_at_node__a1_n7_5,
                             cpd_ambulance_at_node__a1_n8_5,
                             cpd_person_waiting_service__n0_5,
                             cpd_person_waiting_service__n1_5,
                             cpd_person_waiting_service__n2_5,
                             cpd_person_waiting_service__n3_5,
                             cpd_person_waiting_service__n4_5,
                             cpd_person_waiting_service__n5_5,
                             cpd_person_waiting_service__n6_5,
                             cpd_person_waiting_service__n7_5,
                             cpd_person_waiting_service__n8_5,
                             cpd_person_in_ambulance__a0_6,
                             cpd_person_in_ambulance__a1_6,
                             cpd_ambulance_at_node__a0_n0_6,
                             cpd_ambulance_at_node__a0_n1_6,
                             cpd_ambulance_at_node__a0_n2_6,
                             cpd_ambulance_at_node__a0_n3_6,
                             cpd_ambulance_at_node__a0_n4_6,
                             cpd_ambulance_at_node__a0_n5_6,
                             cpd_ambulance_at_node__a0_n6_6,
                             cpd_ambulance_at_node__a0_n7_6,
                             cpd_ambulance_at_node__a0_n8_6,
                             cpd_ambulance_at_node__a1_n0_6,
                             cpd_ambulance_at_node__a1_n1_6,
                             cpd_ambulance_at_node__a1_n2_6,
                             cpd_ambulance_at_node__a1_n3_6,
                             cpd_ambulance_at_node__a1_n4_6,
                             cpd_ambulance_at_node__a1_n5_6,
                             cpd_ambulance_at_node__a1_n6_6,
                             cpd_ambulance_at_node__a1_n7_6,
                             cpd_ambulance_at_node__a1_n8_6,
                             cpd_person_waiting_service__n0_6,
                             cpd_person_waiting_service__n1_6,
                             cpd_person_waiting_service__n2_6,
                             cpd_person_waiting_service__n3_6,
                             cpd_person_waiting_service__n4_6,
                             cpd_person_waiting_service__n5_6,
                             cpd_person_waiting_service__n6_6,
                             cpd_person_waiting_service__n7_6,
                             cpd_person_waiting_service__n8_6,
                             cpd_person_in_ambulance__a0_7,
                             cpd_person_in_ambulance__a1_7,
                             cpd_ambulance_at_node__a0_n0_7,
                             cpd_ambulance_at_node__a0_n1_7,
                             cpd_ambulance_at_node__a0_n2_7,
                             cpd_ambulance_at_node__a0_n3_7,
                             cpd_ambulance_at_node__a0_n4_7,
                             cpd_ambulance_at_node__a0_n5_7,
                             cpd_ambulance_at_node__a0_n6_7,
                             cpd_ambulance_at_node__a0_n7_7,
                             cpd_ambulance_at_node__a0_n8_7,
                             cpd_ambulance_at_node__a1_n0_7,
                             cpd_ambulance_at_node__a1_n1_7,
                             cpd_ambulance_at_node__a1_n2_7,
                             cpd_ambulance_at_node__a1_n3_7,
                             cpd_ambulance_at_node__a1_n4_7,
                             cpd_ambulance_at_node__a1_n5_7,
                             cpd_ambulance_at_node__a1_n6_7,
                             cpd_ambulance_at_node__a1_n7_7,
                             cpd_ambulance_at_node__a1_n8_7,
                             cpd_person_waiting_service__n0_7,
                             cpd_person_waiting_service__n1_7,
                             cpd_person_waiting_service__n2_7,
                             cpd_person_waiting_service__n3_7,
                             cpd_person_waiting_service__n4_7,
                             cpd_person_waiting_service__n5_7,
                             cpd_person_waiting_service__n6_7,
                             cpd_person_waiting_service__n7_7,
                             cpd_person_waiting_service__n8_7,
                             cpd_person_in_ambulance__a0_8,
                             cpd_person_in_ambulance__a1_8,
                             cpd_ambulance_at_node__a0_n0_8,
                             cpd_ambulance_at_node__a0_n1_8,
                             cpd_ambulance_at_node__a0_n2_8,
                             cpd_ambulance_at_node__a0_n3_8,
                             cpd_ambulance_at_node__a0_n4_8,
                             cpd_ambulance_at_node__a0_n5_8,
                             cpd_ambulance_at_node__a0_n6_8,
                             cpd_ambulance_at_node__a0_n7_8,
                             cpd_ambulance_at_node__a0_n8_8,
                             cpd_ambulance_at_node__a1_n0_8,
                             cpd_ambulance_at_node__a1_n1_8,
                             cpd_ambulance_at_node__a1_n2_8,
                             cpd_ambulance_at_node__a1_n3_8,
                             cpd_ambulance_at_node__a1_n4_8,
                             cpd_ambulance_at_node__a1_n5_8,
                             cpd_ambulance_at_node__a1_n6_8,
                             cpd_ambulance_at_node__a1_n7_8,
                             cpd_ambulance_at_node__a1_n8_8,
                             cpd_person_waiting_service__n0_8,
                             cpd_person_waiting_service__n1_8,
                             cpd_person_waiting_service__n2_8,
                             cpd_person_waiting_service__n3_8,
                             cpd_person_waiting_service__n4_8,
                             cpd_person_waiting_service__n5_8,
                             cpd_person_waiting_service__n6_8,
                             cpd_person_waiting_service__n7_8,
                             cpd_person_waiting_service__n8_8,
                             cpd_person_in_ambulance__a0_9,
                             cpd_person_in_ambulance__a1_9,
                             cpd_ambulance_at_node__a0_n0_9,
                             cpd_ambulance_at_node__a0_n1_9,
                             cpd_ambulance_at_node__a0_n2_9,
                             cpd_ambulance_at_node__a0_n3_9,
                             cpd_ambulance_at_node__a0_n4_9,
                             cpd_ambulance_at_node__a0_n5_9,
                             cpd_ambulance_at_node__a0_n6_9,
                             cpd_ambulance_at_node__a0_n7_9,
                             cpd_ambulance_at_node__a0_n8_9,
                             cpd_ambulance_at_node__a1_n0_9,
                             cpd_ambulance_at_node__a1_n1_9,
                             cpd_ambulance_at_node__a1_n2_9,
                             cpd_ambulance_at_node__a1_n3_9,
                             cpd_ambulance_at_node__a1_n4_9,
                             cpd_ambulance_at_node__a1_n5_9,
                             cpd_ambulance_at_node__a1_n6_9,
                             cpd_ambulance_at_node__a1_n7_9,
                             cpd_ambulance_at_node__a1_n8_9,
                             cpd_person_waiting_service__n0_9,
                             cpd_person_waiting_service__n1_9,
                             cpd_person_waiting_service__n2_9,
                             cpd_person_waiting_service__n3_9,
                             cpd_person_waiting_service__n4_9,
                             cpd_person_waiting_service__n5_9,
                             cpd_person_waiting_service__n6_9,
                             cpd_person_waiting_service__n7_9,
                             cpd_person_waiting_service__n8_9,
                             cpd_person_in_ambulance__a0_10,
                             cpd_person_in_ambulance__a1_10,
                             cpd_ambulance_at_node__a0_n0_10,
                             cpd_ambulance_at_node__a0_n1_10,
                             cpd_ambulance_at_node__a0_n2_10,
                             cpd_ambulance_at_node__a0_n3_10,
                             cpd_ambulance_at_node__a0_n4_10,
                             cpd_ambulance_at_node__a0_n5_10,
                             cpd_ambulance_at_node__a0_n6_10,
                             cpd_ambulance_at_node__a0_n7_10,
                             cpd_ambulance_at_node__a0_n8_10,
                             cpd_ambulance_at_node__a1_n0_10,
                             cpd_ambulance_at_node__a1_n1_10,
                             cpd_ambulance_at_node__a1_n2_10,
                             cpd_ambulance_at_node__a1_n3_10,
                             cpd_ambulance_at_node__a1_n4_10,
                             cpd_ambulance_at_node__a1_n5_10,
                             cpd_ambulance_at_node__a1_n6_10,
                             cpd_ambulance_at_node__a1_n7_10,
                             cpd_ambulance_at_node__a1_n8_10,
                             cpd_person_waiting_service__n0_10,
                             cpd_person_waiting_service__n1_10,
                             cpd_person_waiting_service__n2_10,
                             cpd_person_waiting_service__n3_10,
                             cpd_person_waiting_service__n4_10,
                             cpd_person_waiting_service__n5_10,
                             cpd_person_waiting_service__n6_10,
                             cpd_person_waiting_service__n7_10,
                             cpd_person_waiting_service__n8_10,
                             cpd_person_in_ambulance__a0_11,
                             cpd_person_in_ambulance__a1_11,
                             cpd_ambulance_at_node__a0_n0_11,
                             cpd_ambulance_at_node__a0_n1_11,
                             cpd_ambulance_at_node__a0_n2_11,
                             cpd_ambulance_at_node__a0_n3_11,
                             cpd_ambulance_at_node__a0_n4_11,
                             cpd_ambulance_at_node__a0_n5_11,
                             cpd_ambulance_at_node__a0_n6_11,
                             cpd_ambulance_at_node__a0_n7_11,
                             cpd_ambulance_at_node__a0_n8_11,
                             cpd_ambulance_at_node__a1_n0_11,
                             cpd_ambulance_at_node__a1_n1_11,
                             cpd_ambulance_at_node__a1_n2_11,
                             cpd_ambulance_at_node__a1_n3_11,
                             cpd_ambulance_at_node__a1_n4_11,
                             cpd_ambulance_at_node__a1_n5_11,
                             cpd_ambulance_at_node__a1_n6_11,
                             cpd_ambulance_at_node__a1_n7_11,
                             cpd_ambulance_at_node__a1_n8_11,
                             cpd_person_waiting_service__n0_11,
                             cpd_person_waiting_service__n1_11,
                             cpd_person_waiting_service__n2_11,
                             cpd_person_waiting_service__n3_11,
                             cpd_person_waiting_service__n4_11,
                             cpd_person_waiting_service__n5_11,
                             cpd_person_waiting_service__n6_11,
                             cpd_person_waiting_service__n7_11,
                             cpd_person_waiting_service__n8_11,
                             cpd_person_in_ambulance__a0_12,
                             cpd_person_in_ambulance__a1_12,
                             cpd_ambulance_at_node__a0_n0_12,
                             cpd_ambulance_at_node__a0_n1_12,
                             cpd_ambulance_at_node__a0_n2_12,
                             cpd_ambulance_at_node__a0_n3_12,
                             cpd_ambulance_at_node__a0_n4_12,
                             cpd_ambulance_at_node__a0_n5_12,
                             cpd_ambulance_at_node__a0_n6_12,
                             cpd_ambulance_at_node__a0_n7_12,
                             cpd_ambulance_at_node__a0_n8_12,
                             cpd_ambulance_at_node__a1_n0_12,
                             cpd_ambulance_at_node__a1_n1_12,
                             cpd_ambulance_at_node__a1_n2_12,
                             cpd_ambulance_at_node__a1_n3_12,
                             cpd_ambulance_at_node__a1_n4_12,
                             cpd_ambulance_at_node__a1_n5_12,
                             cpd_ambulance_at_node__a1_n6_12,
                             cpd_ambulance_at_node__a1_n7_12,
                             cpd_ambulance_at_node__a1_n8_12,
                             cpd_person_waiting_service__n0_12,
                             cpd_person_waiting_service__n1_12,
                             cpd_person_waiting_service__n2_12,
                             cpd_person_waiting_service__n3_12,
                             cpd_person_waiting_service__n4_12,
                             cpd_person_waiting_service__n5_12,
                             cpd_person_waiting_service__n6_12,
                             cpd_person_waiting_service__n7_12,
                             cpd_person_waiting_service__n8_12,
                             cpd_person_in_ambulance__a0_13,
                             cpd_person_in_ambulance__a1_13,
                             cpd_ambulance_at_node__a0_n0_13,
                             cpd_ambulance_at_node__a0_n1_13,
                             cpd_ambulance_at_node__a0_n2_13,
                             cpd_ambulance_at_node__a0_n3_13,
                             cpd_ambulance_at_node__a0_n4_13,
                             cpd_ambulance_at_node__a0_n5_13,
                             cpd_ambulance_at_node__a0_n6_13,
                             cpd_ambulance_at_node__a0_n7_13,
                             cpd_ambulance_at_node__a0_n8_13,
                             cpd_ambulance_at_node__a1_n0_13,
                             cpd_ambulance_at_node__a1_n1_13,
                             cpd_ambulance_at_node__a1_n2_13,
                             cpd_ambulance_at_node__a1_n3_13,
                             cpd_ambulance_at_node__a1_n4_13,
                             cpd_ambulance_at_node__a1_n5_13,
                             cpd_ambulance_at_node__a1_n6_13,
                             cpd_ambulance_at_node__a1_n7_13,
                             cpd_ambulance_at_node__a1_n8_13,
                             cpd_person_waiting_service__n0_13,
                             cpd_person_waiting_service__n1_13,
                             cpd_person_waiting_service__n2_13,
                             cpd_person_waiting_service__n3_13,
                             cpd_person_waiting_service__n4_13,
                             cpd_person_waiting_service__n5_13,
                             cpd_person_waiting_service__n6_13,
                             cpd_person_waiting_service__n7_13,
                             cpd_person_waiting_service__n8_13,
                             cpd_person_in_ambulance__a0_14,
                             cpd_person_in_ambulance__a1_14,
                             cpd_ambulance_at_node__a0_n0_14,
                             cpd_ambulance_at_node__a0_n1_14,
                             cpd_ambulance_at_node__a0_n2_14,
                             cpd_ambulance_at_node__a0_n3_14,
                             cpd_ambulance_at_node__a0_n4_14,
                             cpd_ambulance_at_node__a0_n5_14,
                             cpd_ambulance_at_node__a0_n6_14,
                             cpd_ambulance_at_node__a0_n7_14,
                             cpd_ambulance_at_node__a0_n8_14,
                             cpd_ambulance_at_node__a1_n0_14,
                             cpd_ambulance_at_node__a1_n1_14,
                             cpd_ambulance_at_node__a1_n2_14,
                             cpd_ambulance_at_node__a1_n3_14,
                             cpd_ambulance_at_node__a1_n4_14,
                             cpd_ambulance_at_node__a1_n5_14,
                             cpd_ambulance_at_node__a1_n6_14,
                             cpd_ambulance_at_node__a1_n7_14,
                             cpd_ambulance_at_node__a1_n8_14,
                             cpd_person_waiting_service__n0_14,
                             cpd_person_waiting_service__n1_14,
                             cpd_person_waiting_service__n2_14,
                             cpd_person_waiting_service__n3_14,
                             cpd_person_waiting_service__n4_14,
                             cpd_person_waiting_service__n5_14,
                             cpd_person_waiting_service__n6_14,
                             cpd_person_waiting_service__n7_14,
                             cpd_person_waiting_service__n8_14,
                             cpd_person_in_ambulance__a0_15,
                             cpd_person_in_ambulance__a1_15,
                             cpd_ambulance_at_node__a0_n0_15,
                             cpd_ambulance_at_node__a0_n1_15,
                             cpd_ambulance_at_node__a0_n2_15,
                             cpd_ambulance_at_node__a0_n3_15,
                             cpd_ambulance_at_node__a0_n4_15,
                             cpd_ambulance_at_node__a0_n5_15,
                             cpd_ambulance_at_node__a0_n6_15,
                             cpd_ambulance_at_node__a0_n7_15,
                             cpd_ambulance_at_node__a0_n8_15,
                             cpd_ambulance_at_node__a1_n0_15,
                             cpd_ambulance_at_node__a1_n1_15,
                             cpd_ambulance_at_node__a1_n2_15,
                             cpd_ambulance_at_node__a1_n3_15,
                             cpd_ambulance_at_node__a1_n4_15,
                             cpd_ambulance_at_node__a1_n5_15,
                             cpd_ambulance_at_node__a1_n6_15,
                             cpd_ambulance_at_node__a1_n7_15,
                             cpd_ambulance_at_node__a1_n8_15,
                             cpd_person_waiting_service__n0_15,
                             cpd_person_waiting_service__n1_15,
                             cpd_person_waiting_service__n2_15,
                             cpd_person_waiting_service__n3_15,
                             cpd_person_waiting_service__n4_15,
                             cpd_person_waiting_service__n5_15,
                             cpd_person_waiting_service__n6_15,
                             cpd_person_waiting_service__n7_15,
                             cpd_person_waiting_service__n8_15,
                             cpd_person_in_ambulance__a0_16,
                             cpd_person_in_ambulance__a1_16,
                             cpd_ambulance_at_node__a0_n0_16,
                             cpd_ambulance_at_node__a0_n1_16,
                             cpd_ambulance_at_node__a0_n2_16,
                             cpd_ambulance_at_node__a0_n3_16,
                             cpd_ambulance_at_node__a0_n4_16,
                             cpd_ambulance_at_node__a0_n5_16,
                             cpd_ambulance_at_node__a0_n6_16,
                             cpd_ambulance_at_node__a0_n7_16,
                             cpd_ambulance_at_node__a0_n8_16,
                             cpd_ambulance_at_node__a1_n0_16,
                             cpd_ambulance_at_node__a1_n1_16,
                             cpd_ambulance_at_node__a1_n2_16,
                             cpd_ambulance_at_node__a1_n3_16,
                             cpd_ambulance_at_node__a1_n4_16,
                             cpd_ambulance_at_node__a1_n5_16,
                             cpd_ambulance_at_node__a1_n6_16,
                             cpd_ambulance_at_node__a1_n7_16,
                             cpd_ambulance_at_node__a1_n8_16,
                             cpd_person_waiting_service__n0_16,
                             cpd_person_waiting_service__n1_16,
                             cpd_person_waiting_service__n2_16,
                             cpd_person_waiting_service__n3_16,
                             cpd_person_waiting_service__n4_16,
                             cpd_person_waiting_service__n5_16,
                             cpd_person_waiting_service__n6_16,
                             cpd_person_waiting_service__n7_16,
                             cpd_person_waiting_service__n8_16,
                             cpd_person_in_ambulance__a0_17,
                             cpd_person_in_ambulance__a1_17,
                             cpd_ambulance_at_node__a0_n0_17,
                             cpd_ambulance_at_node__a0_n1_17,
                             cpd_ambulance_at_node__a0_n2_17,
                             cpd_ambulance_at_node__a0_n3_17,
                             cpd_ambulance_at_node__a0_n4_17,
                             cpd_ambulance_at_node__a0_n5_17,
                             cpd_ambulance_at_node__a0_n6_17,
                             cpd_ambulance_at_node__a0_n7_17,
                             cpd_ambulance_at_node__a0_n8_17,
                             cpd_ambulance_at_node__a1_n0_17,
                             cpd_ambulance_at_node__a1_n1_17,
                             cpd_ambulance_at_node__a1_n2_17,
                             cpd_ambulance_at_node__a1_n3_17,
                             cpd_ambulance_at_node__a1_n4_17,
                             cpd_ambulance_at_node__a1_n5_17,
                             cpd_ambulance_at_node__a1_n6_17,
                             cpd_ambulance_at_node__a1_n7_17,
                             cpd_ambulance_at_node__a1_n8_17,
                             cpd_person_waiting_service__n0_17,
                             cpd_person_waiting_service__n1_17,
                             cpd_person_waiting_service__n2_17,
                             cpd_person_waiting_service__n3_17,
                             cpd_person_waiting_service__n4_17,
                             cpd_person_waiting_service__n5_17,
                             cpd_person_waiting_service__n6_17,
                             cpd_person_waiting_service__n7_17,
                             cpd_person_waiting_service__n8_17,
                             cpd_person_in_ambulance__a0_18,
                             cpd_person_in_ambulance__a1_18,
                             cpd_ambulance_at_node__a0_n0_18,
                             cpd_ambulance_at_node__a0_n1_18,
                             cpd_ambulance_at_node__a0_n2_18,
                             cpd_ambulance_at_node__a0_n3_18,
                             cpd_ambulance_at_node__a0_n4_18,
                             cpd_ambulance_at_node__a0_n5_18,
                             cpd_ambulance_at_node__a0_n6_18,
                             cpd_ambulance_at_node__a0_n7_18,
                             cpd_ambulance_at_node__a0_n8_18,
                             cpd_ambulance_at_node__a1_n0_18,
                             cpd_ambulance_at_node__a1_n1_18,
                             cpd_ambulance_at_node__a1_n2_18,
                             cpd_ambulance_at_node__a1_n3_18,
                             cpd_ambulance_at_node__a1_n4_18,
                             cpd_ambulance_at_node__a1_n5_18,
                             cpd_ambulance_at_node__a1_n6_18,
                             cpd_ambulance_at_node__a1_n7_18,
                             cpd_ambulance_at_node__a1_n8_18,
                             cpd_person_waiting_service__n0_18,
                             cpd_person_waiting_service__n1_18,
                             cpd_person_waiting_service__n2_18,
                             cpd_person_waiting_service__n3_18,
                             cpd_person_waiting_service__n4_18,
                             cpd_person_waiting_service__n5_18,
                             cpd_person_waiting_service__n6_18,
                             cpd_person_waiting_service__n7_18,
                             cpd_person_waiting_service__n8_18,
                             cpd_person_in_ambulance__a0_19,
                             cpd_person_in_ambulance__a1_19,
                             cpd_ambulance_at_node__a0_n0_19,
                             cpd_ambulance_at_node__a0_n1_19,
                             cpd_ambulance_at_node__a0_n2_19,
                             cpd_ambulance_at_node__a0_n3_19,
                             cpd_ambulance_at_node__a0_n4_19,
                             cpd_ambulance_at_node__a0_n5_19,
                             cpd_ambulance_at_node__a0_n6_19,
                             cpd_ambulance_at_node__a0_n7_19,
                             cpd_ambulance_at_node__a0_n8_19,
                             cpd_ambulance_at_node__a1_n0_19,
                             cpd_ambulance_at_node__a1_n1_19,
                             cpd_ambulance_at_node__a1_n2_19,
                             cpd_ambulance_at_node__a1_n3_19,
                             cpd_ambulance_at_node__a1_n4_19,
                             cpd_ambulance_at_node__a1_n5_19,
                             cpd_ambulance_at_node__a1_n6_19,
                             cpd_ambulance_at_node__a1_n7_19,
                             cpd_ambulance_at_node__a1_n8_19,
                             cpd_person_waiting_service__n0_19,
                             cpd_person_waiting_service__n1_19,
                             cpd_person_waiting_service__n2_19,
                             cpd_person_waiting_service__n3_19,
                             cpd_person_waiting_service__n4_19,
                             cpd_person_waiting_service__n5_19,
                             cpd_person_waiting_service__n6_19,
                             cpd_person_waiting_service__n7_19,
                             cpd_person_waiting_service__n8_19,
                             cpd_person_in_ambulance__a0_20,
                             cpd_person_in_ambulance__a1_20,
                             cpd_ambulance_at_node__a0_n0_20,
                             cpd_ambulance_at_node__a0_n1_20,
                             cpd_ambulance_at_node__a0_n2_20,
                             cpd_ambulance_at_node__a0_n3_20,
                             cpd_ambulance_at_node__a0_n4_20,
                             cpd_ambulance_at_node__a0_n5_20,
                             cpd_ambulance_at_node__a0_n6_20,
                             cpd_ambulance_at_node__a0_n7_20,
                             cpd_ambulance_at_node__a0_n8_20,
                             cpd_ambulance_at_node__a1_n0_20,
                             cpd_ambulance_at_node__a1_n1_20,
                             cpd_ambulance_at_node__a1_n2_20,
                             cpd_ambulance_at_node__a1_n3_20,
                             cpd_ambulance_at_node__a1_n4_20,
                             cpd_ambulance_at_node__a1_n5_20,
                             cpd_ambulance_at_node__a1_n6_20,
                             cpd_ambulance_at_node__a1_n7_20,
                             cpd_ambulance_at_node__a1_n8_20,
                             cpd_person_waiting_service__n0_20,
                             cpd_person_waiting_service__n1_20,
                             cpd_person_waiting_service__n2_20,
                             cpd_person_waiting_service__n3_20,
                             cpd_person_waiting_service__n4_20,
                             cpd_person_waiting_service__n5_20,
                             cpd_person_waiting_service__n6_20,
                             cpd_person_waiting_service__n7_20,
                             cpd_person_waiting_service__n8_20,
                             cpd_person_in_ambulance__a0_21,
                             cpd_person_in_ambulance__a1_21,
                             cpd_ambulance_at_node__a0_n0_21,
                             cpd_ambulance_at_node__a0_n1_21,
                             cpd_ambulance_at_node__a0_n2_21,
                             cpd_ambulance_at_node__a0_n3_21,
                             cpd_ambulance_at_node__a0_n4_21,
                             cpd_ambulance_at_node__a0_n5_21,
                             cpd_ambulance_at_node__a0_n6_21,
                             cpd_ambulance_at_node__a0_n7_21,
                             cpd_ambulance_at_node__a0_n8_21,
                             cpd_ambulance_at_node__a1_n0_21,
                             cpd_ambulance_at_node__a1_n1_21,
                             cpd_ambulance_at_node__a1_n2_21,
                             cpd_ambulance_at_node__a1_n3_21,
                             cpd_ambulance_at_node__a1_n4_21,
                             cpd_ambulance_at_node__a1_n5_21,
                             cpd_ambulance_at_node__a1_n6_21,
                             cpd_ambulance_at_node__a1_n7_21,
                             cpd_ambulance_at_node__a1_n8_21,
                             cpd_person_waiting_service__n0_21,
                             cpd_person_waiting_service__n1_21,
                             cpd_person_waiting_service__n2_21,
                             cpd_person_waiting_service__n3_21,
                             cpd_person_waiting_service__n4_21,
                             cpd_person_waiting_service__n5_21,
                             cpd_person_waiting_service__n6_21,
                             cpd_person_waiting_service__n7_21,
                             cpd_person_waiting_service__n8_21,
                             cpd_person_in_ambulance__a0_22,
                             cpd_person_in_ambulance__a1_22,
                             cpd_ambulance_at_node__a0_n0_22,
                             cpd_ambulance_at_node__a0_n1_22,
                             cpd_ambulance_at_node__a0_n2_22,
                             cpd_ambulance_at_node__a0_n3_22,
                             cpd_ambulance_at_node__a0_n4_22,
                             cpd_ambulance_at_node__a0_n5_22,
                             cpd_ambulance_at_node__a0_n6_22,
                             cpd_ambulance_at_node__a0_n7_22,
                             cpd_ambulance_at_node__a0_n8_22,
                             cpd_ambulance_at_node__a1_n0_22,
                             cpd_ambulance_at_node__a1_n1_22,
                             cpd_ambulance_at_node__a1_n2_22,
                             cpd_ambulance_at_node__a1_n3_22,
                             cpd_ambulance_at_node__a1_n4_22,
                             cpd_ambulance_at_node__a1_n5_22,
                             cpd_ambulance_at_node__a1_n6_22,
                             cpd_ambulance_at_node__a1_n7_22,
                             cpd_ambulance_at_node__a1_n8_22,
                             cpd_person_waiting_service__n0_22,
                             cpd_person_waiting_service__n1_22,
                             cpd_person_waiting_service__n2_22,
                             cpd_person_waiting_service__n3_22,
                             cpd_person_waiting_service__n4_22,
                             cpd_person_waiting_service__n5_22,
                             cpd_person_waiting_service__n6_22,
                             cpd_person_waiting_service__n7_22,
                             cpd_person_waiting_service__n8_22,
                             cpd_person_in_ambulance__a0_23,
                             cpd_person_in_ambulance__a1_23,
                             cpd_ambulance_at_node__a0_n0_23,
                             cpd_ambulance_at_node__a0_n1_23,
                             cpd_ambulance_at_node__a0_n2_23,
                             cpd_ambulance_at_node__a0_n3_23,
                             cpd_ambulance_at_node__a0_n4_23,
                             cpd_ambulance_at_node__a0_n5_23,
                             cpd_ambulance_at_node__a0_n6_23,
                             cpd_ambulance_at_node__a0_n7_23,
                             cpd_ambulance_at_node__a0_n8_23,
                             cpd_ambulance_at_node__a1_n0_23,
                             cpd_ambulance_at_node__a1_n1_23,
                             cpd_ambulance_at_node__a1_n2_23,
                             cpd_ambulance_at_node__a1_n3_23,
                             cpd_ambulance_at_node__a1_n4_23,
                             cpd_ambulance_at_node__a1_n5_23,
                             cpd_ambulance_at_node__a1_n6_23,
                             cpd_ambulance_at_node__a1_n7_23,
                             cpd_ambulance_at_node__a1_n8_23,
                             cpd_person_waiting_service__n0_23,
                             cpd_person_waiting_service__n1_23,
                             cpd_person_waiting_service__n2_23,
                             cpd_person_waiting_service__n3_23,
                             cpd_person_waiting_service__n4_23,
                             cpd_person_waiting_service__n5_23,
                             cpd_person_waiting_service__n6_23,
                             cpd_person_waiting_service__n7_23,
                             cpd_person_waiting_service__n8_23,
                             cpd_person_in_ambulance__a0_24,
                             cpd_person_in_ambulance__a1_24,
                             cpd_ambulance_at_node__a0_n0_24,
                             cpd_ambulance_at_node__a0_n1_24,
                             cpd_ambulance_at_node__a0_n2_24,
                             cpd_ambulance_at_node__a0_n3_24,
                             cpd_ambulance_at_node__a0_n4_24,
                             cpd_ambulance_at_node__a0_n5_24,
                             cpd_ambulance_at_node__a0_n6_24,
                             cpd_ambulance_at_node__a0_n7_24,
                             cpd_ambulance_at_node__a0_n8_24,
                             cpd_ambulance_at_node__a1_n0_24,
                             cpd_ambulance_at_node__a1_n1_24,
                             cpd_ambulance_at_node__a1_n2_24,
                             cpd_ambulance_at_node__a1_n3_24,
                             cpd_ambulance_at_node__a1_n4_24,
                             cpd_ambulance_at_node__a1_n5_24,
                             cpd_ambulance_at_node__a1_n6_24,
                             cpd_ambulance_at_node__a1_n7_24,
                             cpd_ambulance_at_node__a1_n8_24,
                             cpd_person_waiting_service__n0_24,
                             cpd_person_waiting_service__n1_24,
                             cpd_person_waiting_service__n2_24,
                             cpd_person_waiting_service__n3_24,
                             cpd_person_waiting_service__n4_24,
                             cpd_person_waiting_service__n5_24,
                             cpd_person_waiting_service__n6_24,
                             cpd_person_waiting_service__n7_24,
                             cpd_person_waiting_service__n8_24,
                             cpd_person_in_ambulance__a0_25,
                             cpd_person_in_ambulance__a1_25,
                             cpd_ambulance_at_node__a0_n0_25,
                             cpd_ambulance_at_node__a0_n1_25,
                             cpd_ambulance_at_node__a0_n2_25,
                             cpd_ambulance_at_node__a0_n3_25,
                             cpd_ambulance_at_node__a0_n4_25,
                             cpd_ambulance_at_node__a0_n5_25,
                             cpd_ambulance_at_node__a0_n6_25,
                             cpd_ambulance_at_node__a0_n7_25,
                             cpd_ambulance_at_node__a0_n8_25,
                             cpd_ambulance_at_node__a1_n0_25,
                             cpd_ambulance_at_node__a1_n1_25,
                             cpd_ambulance_at_node__a1_n2_25,
                             cpd_ambulance_at_node__a1_n3_25,
                             cpd_ambulance_at_node__a1_n4_25,
                             cpd_ambulance_at_node__a1_n5_25,
                             cpd_ambulance_at_node__a1_n6_25,
                             cpd_ambulance_at_node__a1_n7_25,
                             cpd_ambulance_at_node__a1_n8_25,
                             cpd_person_waiting_service__n0_25,
                             cpd_person_waiting_service__n1_25,
                             cpd_person_waiting_service__n2_25,
                             cpd_person_waiting_service__n3_25,
                             cpd_person_waiting_service__n4_25,
                             cpd_person_waiting_service__n5_25,
                             cpd_person_waiting_service__n6_25,
                             cpd_person_waiting_service__n7_25,
                             cpd_person_waiting_service__n8_25,
                             cpd_person_in_ambulance__a0_26,
                             cpd_person_in_ambulance__a1_26,
                             cpd_ambulance_at_node__a0_n0_26,
                             cpd_ambulance_at_node__a0_n1_26,
                             cpd_ambulance_at_node__a0_n2_26,
                             cpd_ambulance_at_node__a0_n3_26,
                             cpd_ambulance_at_node__a0_n4_26,
                             cpd_ambulance_at_node__a0_n5_26,
                             cpd_ambulance_at_node__a0_n6_26,
                             cpd_ambulance_at_node__a0_n7_26,
                             cpd_ambulance_at_node__a0_n8_26,
                             cpd_ambulance_at_node__a1_n0_26,
                             cpd_ambulance_at_node__a1_n1_26,
                             cpd_ambulance_at_node__a1_n2_26,
                             cpd_ambulance_at_node__a1_n3_26,
                             cpd_ambulance_at_node__a1_n4_26,
                             cpd_ambulance_at_node__a1_n5_26,
                             cpd_ambulance_at_node__a1_n6_26,
                             cpd_ambulance_at_node__a1_n7_26,
                             cpd_ambulance_at_node__a1_n8_26,
                             cpd_person_waiting_service__n0_26,
                             cpd_person_waiting_service__n1_26,
                             cpd_person_waiting_service__n2_26,
                             cpd_person_waiting_service__n3_26,
                             cpd_person_waiting_service__n4_26,
                             cpd_person_waiting_service__n5_26,
                             cpd_person_waiting_service__n6_26,
                             cpd_person_waiting_service__n7_26,
                             cpd_person_waiting_service__n8_26,
                             cpd_person_in_ambulance__a0_27,
                             cpd_person_in_ambulance__a1_27,
                             cpd_ambulance_at_node__a0_n0_27,
                             cpd_ambulance_at_node__a0_n1_27,
                             cpd_ambulance_at_node__a0_n2_27,
                             cpd_ambulance_at_node__a0_n3_27,
                             cpd_ambulance_at_node__a0_n4_27,
                             cpd_ambulance_at_node__a0_n5_27,
                             cpd_ambulance_at_node__a0_n6_27,
                             cpd_ambulance_at_node__a0_n7_27,
                             cpd_ambulance_at_node__a0_n8_27,
                             cpd_ambulance_at_node__a1_n0_27,
                             cpd_ambulance_at_node__a1_n1_27,
                             cpd_ambulance_at_node__a1_n2_27,
                             cpd_ambulance_at_node__a1_n3_27,
                             cpd_ambulance_at_node__a1_n4_27,
                             cpd_ambulance_at_node__a1_n5_27,
                             cpd_ambulance_at_node__a1_n6_27,
                             cpd_ambulance_at_node__a1_n7_27,
                             cpd_ambulance_at_node__a1_n8_27,
                             cpd_person_waiting_service__n0_27,
                             cpd_person_waiting_service__n1_27,
                             cpd_person_waiting_service__n2_27,
                             cpd_person_waiting_service__n3_27,
                             cpd_person_waiting_service__n4_27,
                             cpd_person_waiting_service__n5_27,
                             cpd_person_waiting_service__n6_27,
                             cpd_person_waiting_service__n7_27,
                             cpd_person_waiting_service__n8_27,
                             cpd_person_in_ambulance__a0_28,
                             cpd_person_in_ambulance__a1_28,
                             cpd_ambulance_at_node__a0_n0_28,
                             cpd_ambulance_at_node__a0_n1_28,
                             cpd_ambulance_at_node__a0_n2_28,
                             cpd_ambulance_at_node__a0_n3_28,
                             cpd_ambulance_at_node__a0_n4_28,
                             cpd_ambulance_at_node__a0_n5_28,
                             cpd_ambulance_at_node__a0_n6_28,
                             cpd_ambulance_at_node__a0_n7_28,
                             cpd_ambulance_at_node__a0_n8_28,
                             cpd_ambulance_at_node__a1_n0_28,
                             cpd_ambulance_at_node__a1_n1_28,
                             cpd_ambulance_at_node__a1_n2_28,
                             cpd_ambulance_at_node__a1_n3_28,
                             cpd_ambulance_at_node__a1_n4_28,
                             cpd_ambulance_at_node__a1_n5_28,
                             cpd_ambulance_at_node__a1_n6_28,
                             cpd_ambulance_at_node__a1_n7_28,
                             cpd_ambulance_at_node__a1_n8_28,
                             cpd_person_waiting_service__n0_28,
                             cpd_person_waiting_service__n1_28,
                             cpd_person_waiting_service__n2_28,
                             cpd_person_waiting_service__n3_28,
                             cpd_person_waiting_service__n4_28,
                             cpd_person_waiting_service__n5_28,
                             cpd_person_waiting_service__n6_28,
                             cpd_person_waiting_service__n7_28,
                             cpd_person_waiting_service__n8_28,
                             cpd_person_in_ambulance__a0_29,
                             cpd_person_in_ambulance__a1_29,
                             cpd_ambulance_at_node__a0_n0_29,
                             cpd_ambulance_at_node__a0_n1_29,
                             cpd_ambulance_at_node__a0_n2_29,
                             cpd_ambulance_at_node__a0_n3_29,
                             cpd_ambulance_at_node__a0_n4_29,
                             cpd_ambulance_at_node__a0_n5_29,
                             cpd_ambulance_at_node__a0_n6_29,
                             cpd_ambulance_at_node__a0_n7_29,
                             cpd_ambulance_at_node__a0_n8_29,
                             cpd_ambulance_at_node__a1_n0_29,
                             cpd_ambulance_at_node__a1_n1_29,
                             cpd_ambulance_at_node__a1_n2_29,
                             cpd_ambulance_at_node__a1_n3_29,
                             cpd_ambulance_at_node__a1_n4_29,
                             cpd_ambulance_at_node__a1_n5_29,
                             cpd_ambulance_at_node__a1_n6_29,
                             cpd_ambulance_at_node__a1_n7_29,
                             cpd_ambulance_at_node__a1_n8_29,
                             cpd_person_waiting_service__n0_29,
                             cpd_person_waiting_service__n1_29,
                             cpd_person_waiting_service__n2_29,
                             cpd_person_waiting_service__n3_29,
                             cpd_person_waiting_service__n4_29,
                             cpd_person_waiting_service__n5_29,
                             cpd_person_waiting_service__n6_29,
                             cpd_person_waiting_service__n7_29,
                             cpd_person_waiting_service__n8_29,
                             cpd_person_in_ambulance__a0_30,
                             cpd_person_in_ambulance__a1_30,
                             cpd_ambulance_at_node__a0_n0_30,
                             cpd_ambulance_at_node__a0_n1_30,
                             cpd_ambulance_at_node__a0_n2_30,
                             cpd_ambulance_at_node__a0_n3_30,
                             cpd_ambulance_at_node__a0_n4_30,
                             cpd_ambulance_at_node__a0_n5_30,
                             cpd_ambulance_at_node__a0_n6_30,
                             cpd_ambulance_at_node__a0_n7_30,
                             cpd_ambulance_at_node__a0_n8_30,
                             cpd_ambulance_at_node__a1_n0_30,
                             cpd_ambulance_at_node__a1_n1_30,
                             cpd_ambulance_at_node__a1_n2_30,
                             cpd_ambulance_at_node__a1_n3_30,
                             cpd_ambulance_at_node__a1_n4_30,
                             cpd_ambulance_at_node__a1_n5_30,
                             cpd_ambulance_at_node__a1_n6_30,
                             cpd_ambulance_at_node__a1_n7_30,
                             cpd_ambulance_at_node__a1_n8_30,
                             cpd_person_waiting_service__n0_30,
                             cpd_person_waiting_service__n1_30,
                             cpd_person_waiting_service__n2_30,
                             cpd_person_waiting_service__n3_30,
                             cpd_person_waiting_service__n4_30,
                             cpd_person_waiting_service__n5_30,
                             cpd_person_waiting_service__n6_30,
                             cpd_person_waiting_service__n7_30,
                             cpd_person_waiting_service__n8_30,
                             cpd_person_in_ambulance__a0_31,
                             cpd_person_in_ambulance__a1_31,
                             cpd_ambulance_at_node__a0_n0_31,
                             cpd_ambulance_at_node__a0_n1_31,
                             cpd_ambulance_at_node__a0_n2_31,
                             cpd_ambulance_at_node__a0_n3_31,
                             cpd_ambulance_at_node__a0_n4_31,
                             cpd_ambulance_at_node__a0_n5_31,
                             cpd_ambulance_at_node__a0_n6_31,
                             cpd_ambulance_at_node__a0_n7_31,
                             cpd_ambulance_at_node__a0_n8_31,
                             cpd_ambulance_at_node__a1_n0_31,
                             cpd_ambulance_at_node__a1_n1_31,
                             cpd_ambulance_at_node__a1_n2_31,
                             cpd_ambulance_at_node__a1_n3_31,
                             cpd_ambulance_at_node__a1_n4_31,
                             cpd_ambulance_at_node__a1_n5_31,
                             cpd_ambulance_at_node__a1_n6_31,
                             cpd_ambulance_at_node__a1_n7_31,
                             cpd_ambulance_at_node__a1_n8_31,
                             cpd_person_waiting_service__n0_31,
                             cpd_person_waiting_service__n1_31,
                             cpd_person_waiting_service__n2_31,
                             cpd_person_waiting_service__n3_31,
                             cpd_person_waiting_service__n4_31,
                             cpd_person_waiting_service__n5_31,
                             cpd_person_waiting_service__n6_31,
                             cpd_person_waiting_service__n7_31,
                             cpd_person_waiting_service__n8_31,
                             cpd_person_in_ambulance__a0_32,
                             cpd_person_in_ambulance__a1_32,
                             cpd_ambulance_at_node__a0_n0_32,
                             cpd_ambulance_at_node__a0_n1_32,
                             cpd_ambulance_at_node__a0_n2_32,
                             cpd_ambulance_at_node__a0_n3_32,
                             cpd_ambulance_at_node__a0_n4_32,
                             cpd_ambulance_at_node__a0_n5_32,
                             cpd_ambulance_at_node__a0_n6_32,
                             cpd_ambulance_at_node__a0_n7_32,
                             cpd_ambulance_at_node__a0_n8_32,
                             cpd_ambulance_at_node__a1_n0_32,
                             cpd_ambulance_at_node__a1_n1_32,
                             cpd_ambulance_at_node__a1_n2_32,
                             cpd_ambulance_at_node__a1_n3_32,
                             cpd_ambulance_at_node__a1_n4_32,
                             cpd_ambulance_at_node__a1_n5_32,
                             cpd_ambulance_at_node__a1_n6_32,
                             cpd_ambulance_at_node__a1_n7_32,
                             cpd_ambulance_at_node__a1_n8_32,
                             cpd_person_waiting_service__n0_32,
                             cpd_person_waiting_service__n1_32,
                             cpd_person_waiting_service__n2_32,
                             cpd_person_waiting_service__n3_32,
                             cpd_person_waiting_service__n4_32,
                             cpd_person_waiting_service__n5_32,
                             cpd_person_waiting_service__n6_32,
                             cpd_person_waiting_service__n7_32,
                             cpd_person_waiting_service__n8_32,
                             cpd_person_in_ambulance__a0_33,
                             cpd_person_in_ambulance__a1_33,
                             cpd_ambulance_at_node__a0_n0_33,
                             cpd_ambulance_at_node__a0_n1_33,
                             cpd_ambulance_at_node__a0_n2_33,
                             cpd_ambulance_at_node__a0_n3_33,
                             cpd_ambulance_at_node__a0_n4_33,
                             cpd_ambulance_at_node__a0_n5_33,
                             cpd_ambulance_at_node__a0_n6_33,
                             cpd_ambulance_at_node__a0_n7_33,
                             cpd_ambulance_at_node__a0_n8_33,
                             cpd_ambulance_at_node__a1_n0_33,
                             cpd_ambulance_at_node__a1_n1_33,
                             cpd_ambulance_at_node__a1_n2_33,
                             cpd_ambulance_at_node__a1_n3_33,
                             cpd_ambulance_at_node__a1_n4_33,
                             cpd_ambulance_at_node__a1_n5_33,
                             cpd_ambulance_at_node__a1_n6_33,
                             cpd_ambulance_at_node__a1_n7_33,
                             cpd_ambulance_at_node__a1_n8_33,
                             cpd_person_waiting_service__n0_33,
                             cpd_person_waiting_service__n1_33,
                             cpd_person_waiting_service__n2_33,
                             cpd_person_waiting_service__n3_33,
                             cpd_person_waiting_service__n4_33,
                             cpd_person_waiting_service__n5_33,
                             cpd_person_waiting_service__n6_33,
                             cpd_person_waiting_service__n7_33,
                             cpd_person_waiting_service__n8_33,
                             cpd_person_in_ambulance__a0_34,
                             cpd_person_in_ambulance__a1_34,
                             cpd_ambulance_at_node__a0_n0_34,
                             cpd_ambulance_at_node__a0_n1_34,
                             cpd_ambulance_at_node__a0_n2_34,
                             cpd_ambulance_at_node__a0_n3_34,
                             cpd_ambulance_at_node__a0_n4_34,
                             cpd_ambulance_at_node__a0_n5_34,
                             cpd_ambulance_at_node__a0_n6_34,
                             cpd_ambulance_at_node__a0_n7_34,
                             cpd_ambulance_at_node__a0_n8_34,
                             cpd_ambulance_at_node__a1_n0_34,
                             cpd_ambulance_at_node__a1_n1_34,
                             cpd_ambulance_at_node__a1_n2_34,
                             cpd_ambulance_at_node__a1_n3_34,
                             cpd_ambulance_at_node__a1_n4_34,
                             cpd_ambulance_at_node__a1_n5_34,
                             cpd_ambulance_at_node__a1_n6_34,
                             cpd_ambulance_at_node__a1_n7_34,
                             cpd_ambulance_at_node__a1_n8_34,
                             cpd_person_waiting_service__n0_34,
                             cpd_person_waiting_service__n1_34,
                             cpd_person_waiting_service__n2_34,
                             cpd_person_waiting_service__n3_34,
                             cpd_person_waiting_service__n4_34,
                             cpd_person_waiting_service__n5_34,
                             cpd_person_waiting_service__n6_34,
                             cpd_person_waiting_service__n7_34,
                             cpd_person_waiting_service__n8_34,
                             cpd_person_in_ambulance__a0_35,
                             cpd_person_in_ambulance__a1_35,
                             cpd_ambulance_at_node__a0_n0_35,
                             cpd_ambulance_at_node__a0_n1_35,
                             cpd_ambulance_at_node__a0_n2_35,
                             cpd_ambulance_at_node__a0_n3_35,
                             cpd_ambulance_at_node__a0_n4_35,
                             cpd_ambulance_at_node__a0_n5_35,
                             cpd_ambulance_at_node__a0_n6_35,
                             cpd_ambulance_at_node__a0_n7_35,
                             cpd_ambulance_at_node__a0_n8_35,
                             cpd_ambulance_at_node__a1_n0_35,
                             cpd_ambulance_at_node__a1_n1_35,
                             cpd_ambulance_at_node__a1_n2_35,
                             cpd_ambulance_at_node__a1_n3_35,
                             cpd_ambulance_at_node__a1_n4_35,
                             cpd_ambulance_at_node__a1_n5_35,
                             cpd_ambulance_at_node__a1_n6_35,
                             cpd_ambulance_at_node__a1_n7_35,
                             cpd_ambulance_at_node__a1_n8_35,
                             cpd_person_waiting_service__n0_35,
                             cpd_person_waiting_service__n1_35,
                             cpd_person_waiting_service__n2_35,
                             cpd_person_waiting_service__n3_35,
                             cpd_person_waiting_service__n4_35,
                             cpd_person_waiting_service__n5_35,
                             cpd_person_waiting_service__n6_35,
                             cpd_person_waiting_service__n7_35,
                             cpd_person_waiting_service__n8_35,
                             cpd_person_in_ambulance__a0_36,
                             cpd_person_in_ambulance__a1_36,
                             cpd_ambulance_at_node__a0_n0_36,
                             cpd_ambulance_at_node__a0_n1_36,
                             cpd_ambulance_at_node__a0_n2_36,
                             cpd_ambulance_at_node__a0_n3_36,
                             cpd_ambulance_at_node__a0_n4_36,
                             cpd_ambulance_at_node__a0_n5_36,
                             cpd_ambulance_at_node__a0_n6_36,
                             cpd_ambulance_at_node__a0_n7_36,
                             cpd_ambulance_at_node__a0_n8_36,
                             cpd_ambulance_at_node__a1_n0_36,
                             cpd_ambulance_at_node__a1_n1_36,
                             cpd_ambulance_at_node__a1_n2_36,
                             cpd_ambulance_at_node__a1_n3_36,
                             cpd_ambulance_at_node__a1_n4_36,
                             cpd_ambulance_at_node__a1_n5_36,
                             cpd_ambulance_at_node__a1_n6_36,
                             cpd_ambulance_at_node__a1_n7_36,
                             cpd_ambulance_at_node__a1_n8_36,
                             cpd_person_waiting_service__n0_36,
                             cpd_person_waiting_service__n1_36,
                             cpd_person_waiting_service__n2_36,
                             cpd_person_waiting_service__n3_36,
                             cpd_person_waiting_service__n4_36,
                             cpd_person_waiting_service__n5_36,
                             cpd_person_waiting_service__n6_36,
                             cpd_person_waiting_service__n7_36,
                             cpd_person_waiting_service__n8_36,
                             cpd_person_in_ambulance__a0_37,
                             cpd_person_in_ambulance__a1_37,
                             cpd_ambulance_at_node__a0_n0_37,
                             cpd_ambulance_at_node__a0_n1_37,
                             cpd_ambulance_at_node__a0_n2_37,
                             cpd_ambulance_at_node__a0_n3_37,
                             cpd_ambulance_at_node__a0_n4_37,
                             cpd_ambulance_at_node__a0_n5_37,
                             cpd_ambulance_at_node__a0_n6_37,
                             cpd_ambulance_at_node__a0_n7_37,
                             cpd_ambulance_at_node__a0_n8_37,
                             cpd_ambulance_at_node__a1_n0_37,
                             cpd_ambulance_at_node__a1_n1_37,
                             cpd_ambulance_at_node__a1_n2_37,
                             cpd_ambulance_at_node__a1_n3_37,
                             cpd_ambulance_at_node__a1_n4_37,
                             cpd_ambulance_at_node__a1_n5_37,
                             cpd_ambulance_at_node__a1_n6_37,
                             cpd_ambulance_at_node__a1_n7_37,
                             cpd_ambulance_at_node__a1_n8_37,
                             cpd_person_waiting_service__n0_37,
                             cpd_person_waiting_service__n1_37,
                             cpd_person_waiting_service__n2_37,
                             cpd_person_waiting_service__n3_37,
                             cpd_person_waiting_service__n4_37,
                             cpd_person_waiting_service__n5_37,
                             cpd_person_waiting_service__n6_37,
                             cpd_person_waiting_service__n7_37,
                             cpd_person_waiting_service__n8_37,
                             cpd_person_in_ambulance__a0_38,
                             cpd_person_in_ambulance__a1_38,
                             cpd_ambulance_at_node__a0_n0_38,
                             cpd_ambulance_at_node__a0_n1_38,
                             cpd_ambulance_at_node__a0_n2_38,
                             cpd_ambulance_at_node__a0_n3_38,
                             cpd_ambulance_at_node__a0_n4_38,
                             cpd_ambulance_at_node__a0_n5_38,
                             cpd_ambulance_at_node__a0_n6_38,
                             cpd_ambulance_at_node__a0_n7_38,
                             cpd_ambulance_at_node__a0_n8_38,
                             cpd_ambulance_at_node__a1_n0_38,
                             cpd_ambulance_at_node__a1_n1_38,
                             cpd_ambulance_at_node__a1_n2_38,
                             cpd_ambulance_at_node__a1_n3_38,
                             cpd_ambulance_at_node__a1_n4_38,
                             cpd_ambulance_at_node__a1_n5_38,
                             cpd_ambulance_at_node__a1_n6_38,
                             cpd_ambulance_at_node__a1_n7_38,
                             cpd_ambulance_at_node__a1_n8_38,
                             cpd_person_waiting_service__n0_38,
                             cpd_person_waiting_service__n1_38,
                             cpd_person_waiting_service__n2_38,
                             cpd_person_waiting_service__n3_38,
                             cpd_person_waiting_service__n4_38,
                             cpd_person_waiting_service__n5_38,
                             cpd_person_waiting_service__n6_38,
                             cpd_person_waiting_service__n7_38,
                             cpd_person_waiting_service__n8_38,
                             cpd_person_in_ambulance__a0_39,
                             cpd_person_in_ambulance__a1_39,
                             cpd_ambulance_at_node__a0_n0_39,
                             cpd_ambulance_at_node__a0_n1_39,
                             cpd_ambulance_at_node__a0_n2_39,
                             cpd_ambulance_at_node__a0_n3_39,
                             cpd_ambulance_at_node__a0_n4_39,
                             cpd_ambulance_at_node__a0_n5_39,
                             cpd_ambulance_at_node__a0_n6_39,
                             cpd_ambulance_at_node__a0_n7_39,
                             cpd_ambulance_at_node__a0_n8_39,
                             cpd_ambulance_at_node__a1_n0_39,
                             cpd_ambulance_at_node__a1_n1_39,
                             cpd_ambulance_at_node__a1_n2_39,
                             cpd_ambulance_at_node__a1_n3_39,
                             cpd_ambulance_at_node__a1_n4_39,
                             cpd_ambulance_at_node__a1_n5_39,
                             cpd_ambulance_at_node__a1_n6_39,
                             cpd_ambulance_at_node__a1_n7_39,
                             cpd_ambulance_at_node__a1_n8_39,
                             cpd_person_waiting_service__n0_39,
                             cpd_person_waiting_service__n1_39,
                             cpd_person_waiting_service__n2_39,
                             cpd_person_waiting_service__n3_39,
                             cpd_person_waiting_service__n4_39,
                             cpd_person_waiting_service__n5_39,
                             cpd_person_waiting_service__n6_39,
                             cpd_person_waiting_service__n7_39,
                             cpd_person_waiting_service__n8_39);

