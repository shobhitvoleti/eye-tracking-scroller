import cv2
import sys
import numpy as np
import unittest
import math
import webcam as wbc
import nod_scroll as ns
class TestsEyetracker(unittest.TestCase):
    def test_check_if_detecting_eyes_of_one_person(self):
        image=cv2.imread('testim1.jpg')
        eyec=wbc.call_for_eyecoords(image)
        self.assertAlmostEqual(eyec[0],151,delta=1)
        self.assertAlmostEqual(eyec[1],211,delta=1)

    def test_check_if_detecting_eyes_of_imp_person_in_group(self):
        image=cv2.imread('testim2.jpg')
        eyec=wbc.call_for_eyecoords(image)
        self.assertAlmostEqual(eyec[0],516,delta=1)
        self.assertAlmostEqual(eyec[1],140,delta=1)

    def test_check_if_correct_object_type_passed(self):
        with self.assertRaises(Exception) as context:
            wbc.call_for_eyecoords("asssdd")
        self.assertTrue('Object not recognized by cv2, not an array!' in context.exception)

class TestsNodandScroll(unittest.TestCase):
    def test_check_if_correct_directive_for_scrollingup(self):
        directive=ns.scroll_pdf(250,[220,380,360,400,390,415])
        self.assertEqual(directive,1)

    def test_check_if_correct_directive_for_staying(self):
        directive1=ns.scroll_pdf(250,[220,180,260,270,290,275])
        self.assertEqual1(directive1,0)
        directive2=ns.scroll_pdf(250,[220,240,260,270,200])
        self.assertEqual1(directive2,0)
        directive3=ns.scroll_pdf(250,[490,400,460,320,290])
        self.assertEqual1(directive3,0)
        directive4=ns.scroll_pdf(250,[80,160,180,200,240])
        self.assertEqual1(directive4,0)

    def test_check_if_correct_directive_for_scrollingdown(self):
        directive=ns.scroll_pdf(250,[260,200,160,110,100,75])
        self.assertEqual(directive,-1)

    def test_check_if_correct_directive_for_turning_to_next_page(self):
        directive=ns.next_page(250,[220,380,360,400,390,415])
        self.assertEqual(directive,1)

    def test_check_if_correct_directive_for_staying_on_current_page(self):
        directive1=ns.next_page(250,[220,180,260,270,290,275])
        self.assertEqual1(directive1,0)
        directive2=ns.next_page(250,[220,240,260,270,200])
        self.assertEqual1(directive2,0)
        directive3=ns.next_page(250,[490,400,460,320,290])
        self.assertEqual1(directive3,0)
        directive4=ns.next_page(250,[80,160,180,200,240])
        self.assertEqual1(directive4,0)

    def test_check_if_correct_directive_for_turning_to_previous_page(self):
        directive=ns.next_page(250,[260,200,160,110,100,75])
        self.assertEqual(directive,-1)



    #def test_check
if __name__== "__main__":
    unittest.main()
