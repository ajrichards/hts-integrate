import unittest,getopt,sys,os
from htsint import Configure

## parse inputs                                                                                                                      
try:
    optlist, args = getopt.getopt(sys.argv[1:],'v')
except getopt.GetoptError:
    print(getopt.GetoptError)
    print(sys.argv[0] + "-v")
    print("... the verbose flag (-v) may be used")
    sys.exit()

VERBOSE = False
RUNALL = False

for o, a in optlist:
    if o == '-v':
        VERBOSE = True

## ensure config is setup
config = Configure()

if config.log['dbname'] == '':
    raise Exception("Config file is not setup")

## Database tests
from .DatabaseTest import *
DatabaseTestSuite = unittest.TestLoader().loadTestsFromTestCase(DatabaseTest)
DatabaseSuite = unittest.TestSuite([DatabaseTestSuite])

## GeneOntology tests
from .GeneOntologyTest import *
GeneOntologyTestSuite = unittest.TestLoader().loadTestsFromTestCase(GeneOntologyTest)
GeneOntologySuite = unittest.TestSuite([GeneOntologyTestSuite])

## Blast Tests
from .BlastTest import *
BlastTestSuite = unittest.TestLoader().loadTestsFromTestCase(BlastTest)
BlastSuite = unittest.TestSuite([BlastTestSuite])

from .BlastMapperTest import *
BlastMapperTestSuite = unittest.TestLoader().loadTestsFromTestCase(BlastMapperTest)
BlastMapperSuite = unittest.TestSuite([BlastMapperTestSuite])

