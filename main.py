"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	
	# TODO
  if n <= 1:
    return n
  return a * simple_work_calc(n // b, a, b) + n
  
  pass
    
	

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 30
  assert work_calc(20, 3, 2) == 129
  assert work_calc(30, 4, 2) == 347
  
  assert work_calc(1, 3, 2) == 1
  assert work_calc(5, 4, 3) == 29
  assert work_calc(6, 5, 2) == 61


def work_calc(n, a, b, f):
	
	if n <= 1:
    return f(n)
  return a * work_calc(n // b, a, b, f) + f(n)
  pass

def span_calc(n, a, b, f):
	
	if n <= 1:
    return 0
  return max(span_calc(n // b, a, b, f),            int(math.log(n, b))) + 1
  pass

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: n*n) == 420
  assert work_calc(30, 3, 2, lambda n: n) == 441

  assert work_calc(5, 2, 2, lambda n: n) == 17
  assert work_calc(15, 3, 2, lambda n: n*n) == 966
  assert work_calc(7, 4, 3, lambda n: n) == 46

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	result = []
  for n in input_sizes:
		# compute W(n) using current a, b, f
    result = []
    for n in sizes:
      result.append((n,work_fn1(n),work_fn2(n)))
    return result
	
def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
# create work_fn1
  work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: 1)

# create work_fn2
  work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n*n)
  res = compare_work(work_fn1,work_fn2)
  print(res)

def test_compare_span():
	# curry span_calc to create multiple span
  # functions that can be passed to compare_work
    
    # create span_fn1
    span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)

    # create span_fn2
    span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n*n)

    res = compare_work(span_fn1, span_fn2)
    print(res)

