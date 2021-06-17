import exceptions

class DRCViolation(Exception):
    """Design parameter should meet DRC requirements"""

class IncorrectInputError(Exception):
    """Input is incorrect data"""

class IncorrectDesignSpaceInformation(Exception):
    """Information about Design Space is incorrect"""

class IncompleteFunctionOperation(Exception):
    """Function's operation is incomplete"""

class UnsatisfiableDesignConstraints(Exception):
    """Design constraints are too tight"""