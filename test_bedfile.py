#!/usr/bin/env python3

import pytest
import os.path
from peak_parser import Bedfile

filepath = os.path.join("data", "peaks", "chr1-5_GEM_events.narrowPeak_fus3")

def test_open_file():
	''' check that we can open & read the file '''
	thefile = Bedfile(path=filepath)

def test_peaks():
	''' check that we read the correct number of peaks '''
	thefile = Bedfile(path=filepath)
	assert len(thefile.peaks) == 3266

