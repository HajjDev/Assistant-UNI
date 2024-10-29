# Ceci est un fichier dédier aux tests des fonctions présentent dans assitant.py

from assistant import *

def test_file_exists():
    assert file_exists("all-words.dat") == True, "Test 1"
    assert file_exists("text.txt") == False, "Test 2"
    assert file_exists("readme.txt") == True, "Test 3"
    assert file_exists("readme4.txt") == False, "Test 4"

test_file_exists()

def test_sum():
    assert sum([3, 0, 8, 10, 20]) == 31, 'Test 1'
    assert sum([3, -10, 20, 8, 10]) == 31, 'Test 2'
    assert sum([1]) == 1, 'Test 3'
    assert sum([2, -2]) == 0, 'Test 4'
    assert sum([5, 0, 10]) == 15, 'Test 5'
    
test_sum()

def test_avg():
    assert avg([3, 0, 8, 10, 20]) == 6.2, 'Test 1'
    assert avg([3, -10, 20, 8, 10]) == 6.2, 'Test 2'
    assert avg([1]) == 1, 'Test 3'
    assert avg([2, -2]) == 0, 'Test 4'
    assert avg([5, 0, 10]) == 5, 'Test 5'

test_avg()