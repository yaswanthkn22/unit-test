import unittest
import matches_per_year
import matches_won_eachteam_year as mwey
import extras_perteam
import top_10_economical_bowlers as eco_bowlers

class Testipl(unittest.TestCase):
    """Doc"""


    def test_matches_per_year(self):
        """ Doc"""
        result = matches_per_year.matches_per_year()
        req =matches_per_year.result
        self.assertDictEqual(result, req)

    def test_matches_won_eachteam_eachyear(self):
        """Doc """
        result = mwey.matches_won_eachyear_eachteam()
        result_req = mwey.result_req
        self.assertDictEqual(result, result_req)

    def test_extras_eachteam(self):
        """ Doc"""
        result = extras_perteam.extras_eachteam()
        req_result = extras_perteam.req_result
        self.assertDictEqual(result,req_result)

    def test_top_10_economical_bowlers(self):
        """ Doc"""
        result = eco_bowlers.economical_bowlers()
        req_result = eco_bowlers.req_result
        self.assertDictEqual(result, req_result)

    def test_top_10_economical_bowlers_notequal(self):
        """ Doc"""
        result = eco_bowlers.economical_bowlers()
        req_result = eco_bowlers.req_result.popitem()
        self.assertIsNot(result, req_result)



if __name__=='__main__':
    unittest.main()
