#!/usr/bin/env python3
import pytest

import d1_p1_v2
import d2_p1_v1

def test_d1_p1_v2_t1():
    elven_bread = d1_p1_v2.process_data(d1_p1_v2.read_file("d1-p1-test.txt"))
    max_val = max(elven_bread)
    assert max_val == 24000


def test_d1_p1_v2_t2():
    elven_bread = d1_p1_v2.process_data(d1_p1_v2.read_file("d1-p1-input.txt"))
    max_val = max(elven_bread)
    assert max_val == 71780

def test_d2_p1_v2_t1():
    t = d1_p1_v2.process_data(d1_p1_v2.read_file("d2-p1-test.txt"))
    assert t == 15


def test_d2_p1_v2_t2():
    elven_bread = d1_p1_v2.process_data(d1_p1_v2.read_file("d1-p1-input.txt"))
    max_val = max(elven_bread)
    assert max_val == 71780
