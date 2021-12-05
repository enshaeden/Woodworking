from __main__ import *


def convert_to_cm(input_inches):
	float_inches = float(input_inches)
	cm_base = float(2.54)
	cm_value = float_inches * cm_base
	return cm_value


def convert_to_inches(input_cm):
	cm_value = float(input_cm)
	cm_base = float(2.54)
	inches_value = cm_value / cm_base
	return inches_value
