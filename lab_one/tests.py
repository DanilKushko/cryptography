import unittest
import logging
from diffie_hellman import (decimal_to_binary,
                            fast_module_exp,
                            miller_test,
                            generate_prime,
                            g_mod_P,
                            diffie_hellman,
                            is_prime_trial_division)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DiffieHelmanTests(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(5), '101')
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(25), '11001')

    def test_fast_module_exp(self):
        self.assertEqual(fast_module_exp(2, 3, 5), 3)
        self.assertEqual(fast_module_exp(2, 4, 7), 2)
        self.assertEqual(fast_module_exp(3, 3, 10), 7)
        self.assertEqual(fast_module_exp(5, 0, 3), 1)

    def test_is_prime_trial_division(self):
        self.assertFalse(is_prime_trial_division(0))
        self.assertFalse(is_prime_trial_division(1))
        self.assertTrue(is_prime_trial_division(2))
        self.assertTrue(is_prime_trial_division(17))
        self.assertFalse(is_prime_trial_division(25))
        self.assertTrue(is_prime_trial_division(97))

    def test_miller_test(self):
        self.assertFalse(miller_test(0))
        self.assertFalse(miller_test(1))
        self.assertTrue(miller_test(2))
        self.assertTrue(miller_test(17))
        self.assertFalse(miller_test(25))
        self.assertTrue(miller_test(97))

    def test_generate_prime(self):
        Q, P = generate_prime()
        self.assertTrue(is_prime_trial_division(Q))
        self.assertTrue(is_prime_trial_division(P))
        logger.info(f'Простые числа - Q: {Q}, P: {P}')

    def test_g_mod_P(self):
        Q, P = generate_prime()
        g = g_mod_P(Q, P)
        self.assertTrue(1 < g < P)
        logger.info(f'g сгенерирован: {g}')

    def test_diffie_hellman(self):
        Q, P = generate_prime()
        Q, P, g, Xa, Xb, Ya, Yb, Zab, Zba = diffie_hellman(Q, P)
        self.assertEqual(
            fast_module_exp(Ya, Xb, P),
            fast_module_exp(Yb, Xa, P)
        )
        logger.info(f'Q: {Q},'
                    f'P: {P},'
                    f'g: {g},'
                    f'Xa: {Xa},'
                    f'Xb: {Xb},'
                    f'Ya: {Ya},'
                    f'Yb: {Yb},'
                    f'Zab: {Zab},'
                    f'Zba: {Zba}')


if __name__ == '__main__':
    unittest.main()
