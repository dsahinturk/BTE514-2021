import math

def basics():
    assert sum([i for i in range(9)]) == 45, "Dogrusu 45"

# Run with pytest --disable-pytest-warnings Ders09/BasicTests.py
def test_avg():
    count = 30
    assert sum([i for i in range(count)])/count == 4.5, "Dogrusu 4.5"

# Run with pytest --disable-pytest-warnings Ders09/BasicTests.py
def test_stdev():
    count = 10
    epsilon = 0.001
    avg = sum([i for i in range(count)])/count
    stdev = math.sqrt(sum([(i-avg)**2 for i in range(count)]))/count
    assert math.fabs(stdev-0.908) < epsilon, "diff is "+str(math.fabs(stdev-0.908))