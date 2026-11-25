import requests
import time
def retry(times = 3 , delay = 2):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for  atempt in range(times+1):
                try:
                    return func(*args,**kwargs)

                    

                except requests.RequestException():
                    if atempt == times:
                        raise 
                    print(f"Attempt {atempt+1} failed. Retrying in {delay} seconds...")
                

                    
                    time.sleep(delay)

        return wrapper

    return decorator




def chech_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        res_time = end_time - start_time
        print(f"Execution time: {res_time:.4f} seconds")
        return result
    return wrapper



                