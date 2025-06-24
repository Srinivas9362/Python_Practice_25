# ✅ 1. What It Does
# This code defines a decorator named log. When you apply @log to a function (e.g., extract()), it:

# Wraps the original function

# Adds logging behavior before the original function runs

# Then calls the actual function itself




def log(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def extract():
    print("Extracting data...")

@log
def extract_sales_data():
    # Call API or read CSV
    pass

@log
def transform_sales_data():
    # Clean and process
    pass

@log
def load_sales_to_snowflake():
    # Push to DWH
    pass


extract()



def logging(a):
    def wrapper(*args):
        print(f"Executing {a.__name__} function")
        return a(*args)
    return wrapper


@logging
def sum(a,b):
    print("The sum of a and b is : ", a+b)

@logging
def name(a):
    print(a)


@logging
def stream_lines(file_path):
    with open(file_path) as f:
        for line in f:
            yield line


sum(4,10)


name(20)

stream_lines('D:\datasets/customer_orders.csv')


# 🧠 3. Why This Is Useful in Data Engineering
# In production data pipelines, you may have:

# 10s or 100s of functions (extract_data, transform_sales, load_to_db)

# You want automatic logs before each task runs

# You want centralized behavior (like logging, timing, error-catching)

# Using decorators:

# You avoid repeating print() or log.info() calls everywhere

# You can modify all function behavior in one place