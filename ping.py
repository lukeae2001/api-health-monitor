import requests
import time

def measure_request_latency(url: str) -> float:
    """
    Measures the latency of a single GET request to a specified URL.
    
    This function sends a HTTP GET request and calculates the total time elapesef from just before sending the request to just after receiving the response headers.
    
    Args:
        url: The full URL to send the GET request to
        
    Returns:
        The total request latency in milliseconds, or -1.0 if an error occurs.
    """
    try:
    
        #Record the time just before the request is sent
        start_time = time.time()

        #A timeout ie crucial to prevent the script from hanging indefinitely
        response = requests.get(url, timeout=10)

        #This will raise an exception for 4xx/5xx server errors
        response.raise_for_status()

    except requests.exceptions.RequestException as e:

        #This catches any network-related errors (e.g., DNS failure, connection refused)
        print(f"Error checking {url}: {e}")
        return -1.0 #Return a clear error indicator
    
    finally:

        #This block ensures end_time is always recorded, even if an error occurs
        end_time = time.time()

    duration_ms = (end_time - start_time) * 1000
    return duration_ms

# The __name__ == "__main__" block allows this script to be both runnable on its own
# and importable as a module by other scripts without running this test code.
if __name__ == "__main__":
    target_url = "https://google.com"
    latency = measure_request_latency(target_url)

    if latency != -1.0:
        # The :.2f formats the number to two clean decimal places
        print(f"Response from {target_url} took: {latency:.2f} ms")
