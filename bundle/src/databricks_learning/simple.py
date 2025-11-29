def square_sum(nums):
    """Simple function: returns sum of squares (easy to test)."""
    return sum(x*x for x in nums)


def square_sum_runner(argv=None):
    # simple entrypoint called from Databricks job
    # For demo, compute and print
    data = [1, 2, 3, 4]
    print("sum of squares:", square_sum(data))
