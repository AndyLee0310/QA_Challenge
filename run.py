import sys
import pytest
from module import allure_operate

if __name__ == '__main__':

    pytest_args = ['--log-cli-level=INFO', '-v']

    # Get the `-k` parameter (if available)
    test_filter = sys.argv[sys.argv.index('-k') + 1] if '-k' in sys.argv else ''
    if test_filter:
        pytest_args += ['-k', test_filter]

    # Get the `-m` parameter (if available)
    mark_filter = sys.argv[sys.argv.index('-m') + 1] if '-m' in sys.argv else ''
    if mark_filter:
        pytest_args += ['-m', mark_filter]

    # Run pytest
    pytest.main(pytest_args)

    # Generate the allure report
    allure_operate.output_allure_html_report()
