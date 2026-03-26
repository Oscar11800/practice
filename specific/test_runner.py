import inspect

def run_tests():
    frame = inspect.currentframe().f_back
    caller_module = frame.f_globals
    
    passed = 0
    failed = 0
    
    for name, func in caller_module.items():
        if name.startswith('test') and callable(func):
            try:
                func()
                print(f"✓ {name}: PASSED")
                passed += 1
            except AssertionError as e:
                print(f"✗ {name}: FAILED{e}")
                failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    return failed == 0


def assert_equal(actual, expected, message=""):
    if actual != expected:
        error_msg = f"\n  Expected: {expected}\n  Actual:   {actual}"
        if message:
            error_msg = f"{message}{error_msg}"
        raise AssertionError(error_msg)
    return True
