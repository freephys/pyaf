import pandas as pd
import numpy as np

import sys, os, traceback

import AutoForecast.Bench.GenericBenchmark as ben


class cYahoo_Tester(ben.cGeneric_Tester):

    '''
   
    '''
        
    def __init__(self , tsspec, bench_name):
        super().__init__(tsspec, bench_name);
        pass;

