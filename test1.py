# Import the necessary libraries
import asyncio
import time

# Define sample datasets
data1 = [5, 2, 3, 1, 4]
data2 = [50, 30, 10, 20, 40]
data3 = [500, 300, 100, 200, 400]

# Define an asynchronous function to process data with a delay
async def process_data(data, delay):
    # Simulate a delay using asyncio.sleep
    await asyncio.sleep(delay)
    # Return the sum of the data
    return sorted(data)

# Define the main asynchronous function
async def main():
    # Record the current time to measure the execution time
    start = time.time()
    
    # Concurrently process the three datasets with different delays
    # and collect the results in the 'results' variable
    results = await asyncio.gather(
        process_data(data1, 2),  # Process data1 with a 2-second delay
        process_data(data2, 3),  # Process data2 with a 3-second delay
        process_data(data3, 1)   # Process data3 with a 1-second delay
    )
    
    # Print the elapsed time and the results of the three tasks
    print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data1, data2, data3: {results}")

# Run the main asynchronous function using asyncio.run
asyncio.run(main())