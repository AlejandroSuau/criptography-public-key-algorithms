import unittest

from public_key_algorithms import *

class FrequencyTestIndividualBits(unittest.TestCase):

    def test_basic_sobs_frequency_test_individual_bits_1(self):
        # calculate Sobs from frequency individual bits test
        sequency = [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
        sobs_result = 0.774596669241
        self.assertAlmostEqual(frequency_test_individual_bits_NITS(sequency), sobs_result)
        
        
    def test_basic_sobs_frequency_test_individual_bits_2(self):
        # calculate Sobs from frequency individual bits test
        sequency = [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0]
        sobs_result = 0.5
        self.assertAlmostEqual(frequency_test_individual_bits_NITS(sequency), sobs_result)

class BurstTest(unittest.TestCase):
    def test_basic_burst_test(self):
        # calculate Vn burst test
        sequency = [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
        result = 9
        self.assertEqual(burst_test(sequency), result)       

class LFSROutputStringSequence(unittest.TestCase):

    def test_basic_LFSR_output_sequence_1(self):
        # calculate LFSR output sequence
        xor_pattern = [1, 1]
        initial_stat = [1, 1]
        output_len = 4
        output_result = "1101"
        self.assertEqual(LFSR_output_string(xor_pattern, initial_stat, output_len), output_result)
     
        
    def test_basic_LFSR_output_sequence_2(self):
        # calculate LFSR output sequence
        xor_pattern = [1, 0, 0, 0, 0, 1]
        initial_stat = [1, 1, 0, 0, 1, 0]
        output_len = 13
        output_result = "0100111000101"
        self.assertEqual(LFSR_output_string(xor_pattern, initial_stat, output_len), output_result)
        
    def test_basic_LFSR_output_sequence_3(self):
        # calculate LFSR output sequence
        xor_pattern = [0, 0, 1, 1]
        initial_stat = [0, 0, 0, 1]
        output_len = 8
        output_result = "10001001"
        self.assertEqual(LFSR_output_string(xor_pattern, initial_stat, output_len), output_result)
    
    def test_basic_LFSR_output_sequence_4(self):
        # calculate LFSR output sequence
        xor_pattern = [1, 0, 0, 0, 0, 1]
        initial_stat = [1, 1, 0, 0, 0, 1]
        output_len = 12
        output_result = "100011000010"
        self.assertEqual(LFSR_output_string(xor_pattern, initial_stat, output_len), output_result)
        
class TriviumZOutput(unittest.TestCase):

    def test_basic_trivium_z_output_1(self):
        # calculate trivium z output
        stat_register_A = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1,
                           0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1,
                           0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0,
                           0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0,
                           1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0,
                           0, 1, 0, 0, 1, 0, 1, 1]
        stat_register_B = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0,
                           0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0,
                           1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 
                           0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1,
                           0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1]
        stat_register_C = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1,
                           1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1,
                           0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1,
                           0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0,
                           1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
                           0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1,
                           1, 1, 1, 1, 0, 1, 0, 1, 0]
        z_solution = 0
        self.assertEqual(Trivium_z_output(stat_register_A, stat_register_B, stat_register_C), z_solution)
        
    def test_basic_trivium_z_output_2(self):
        # calculate trivium z output
        stat_register_A = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
                           0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1,
                           1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1,
                           1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0,
                           0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0,
                           1, 0, 0, 0, 1, 0, 1, 0]
        stat_register_B = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1,
                           0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0,
                           1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
                           1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1,
                           0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0]
        stat_register_C = [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
                           0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1,
                           1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1,
                           1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1,
                           1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1,
                           1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0,
                           0, 1, 0, 0, 1, 1, 1, 0, 0]
        z_solution = 0
        self.assertEqual(Trivium_z_output(stat_register_A, stat_register_B, stat_register_C), z_solution)
        
class AddRoundKey(unittest.TestCase):

    def test_basic_add_round_key_1(self):
        # calculate add round key matrix
        key = "BB6A5E2AB9066495EFAF30E57E798546"
        text = "5B60A8A1A9895EE98AE2AC0EB39CA541"
        solution = "E0 10 65 CD"
        xor_matrix = add_round_key(key, text)
        self.assertEqual(' '.join(xor_matrix[0]), solution)
        
    def test_basic_add_round_key_2(self):
        # calculate add round key matrix
        key = "b692cf0b643dbdf1be9bc5006830b3fe"
        text = "9df7393c287fc1aa91786c2500a6c6a5"
        solution = "2B 4C 2F 68"
        xor_matrix = add_round_key(key, text)
        self.assertEqual(' '.join(xor_matrix[0]), solution)
        
if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [FrequencyTestIndividualBits,
                           LFSROutputStringSequence, TriviumZOutput, AddRoundKey,
                           BurstTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)
