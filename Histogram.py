import numpy as np

NO_OF_BINS = 100  # Better performance needs higher [NO_OF_BINS]
NO_OF_SAMPLES = 10000  # Number of random samples to be used in analysis
NO_OF_MOMENTS = 30  # Define Number of moments
START_POINT = -1  # Start point on real line for UD
STOP_POINT = 3  # Stop point on real line for UD
bin_width = (STOP_POINT - START_POINT) / NO_OF_BINS  # Value of differential

t_new = np.linspace(START_POINT, STOP_POINT, NO_OF_BINS)  # Construct the horizontal axis
x_new = np.random.uniform(START_POINT, STOP_POINT, NO_OF_SAMPLES)  # Generate the random numbers

bin_idx = np.zeros(NO_OF_SAMPLES)  # Store the indices of the bins on real line
hist_count = np.zeros(NO_OF_BINS)  # Store the histogram occurrences
pdf = np.zeros(NO_OF_BINS)  # Store the values of PDF
cdf = np.zeros(NO_OF_BINS)  # Store the values of CDF

for i in range(0, NO_OF_SAMPLES):  # Iterate through the generated random numbers
    for j in range(0, NO_OF_BINS):  # Iterate through the bins
        if x_new[i] > t_new[j]:  # Decide the 'order' of the bins that fits the random number
            bin_idx[i] = j  # Assign the order for the bin storage

for j in range(0, NO_OF_BINS):  # Iterate through the bins
    for k in range(0, NO_OF_SAMPLES):  # Iterate through the generated random numbers
        if j == bin_idx[k]:  # Decide whether the bins store the correct labels
            hist_count[j] = hist_count[j] + 1  # Construct the histogram

pdf = hist_count / NO_OF_SAMPLES  # PDF is the normalized version of histogram

cdf[0] = pdf[0]  # CDF, PDF integrated out initialized with zero starting from the first sample of PDF
for k in range(1, NO_OF_BINS):  # Iterate through the bins
    cdf[k] = pdf[k] + cdf[k - 1]  # Integrate the PDF

estimated_mean = 0  # Initialized the mean storage
for k in range(0, NO_OF_BINS):  # Iterate through the bins
    estimated_mean = estimated_mean + t_new[k] * pdf[k]  # Estimate the mean

true_mean = 0  # Initialized the true mean storage
for k in range(0, NO_OF_SAMPLES):  # Iterate through the random number array
    true_mean = true_mean + x_new[k] / float(len(x_new))  # Obtain the true mean

estimated_variance = 0  # Initialized the variance storage

for k in range(0, NO_OF_BINS):  # Iterate through the bins
    estimated_variance = estimated_variance + (t_new[k] ** 2) * pdf[k]  # Estimate the variance

true_variance = 0  # Initialized the true variance storage
for k in range(0, NO_OF_SAMPLES):  # Iterate through the random number array
    true_variance = true_variance + (x_new[k] ** 2) / float(len(x_new))  # Obtain the true variance

estimated_x3 = 0  # Initialized the x3 storage
for k in range(0, NO_OF_BINS):  # Iterate through the bins
    estimated_x3 = estimated_x3 + (t_new[k] ** 3) * pdf[k]  # Estimate the x3

true_x3 = 0  # Initialized the true x3 storage
for k in range(0, NO_OF_SAMPLES):  # Iterate through the random number array
    true_x3 = true_x3 + (x_new[k] ** 3) / float(len(x_new))  # Obtain the true x3

moment_array = np.zeros(NO_OF_MOMENTS)
for m in range(0, NO_OF_MOMENTS):
    for k in range(0, NO_OF_BINS):
        moment_array[m] = moment_array[m] + (t_new[k] ** m) * pdf[k]

new_array = np.zeros(NO_OF_MOMENTS)  #First degree derivative
for t in range(0, NO_OF_MOMENTS - 1):
    new_array[t] = moment_array[t + 1] - moment_array[t] #Derivative of the array

factorial_input = int(input("Enter number to calculate factorial:"))
factorial_output = 0
if not (factorial_input < 0):#Factorial must be greater than 0
    factorial_output = 1#Give 1 if factorial is 0 or 1
    for i in range(1, factorial_input+1):
        factorial_output = factorial_output * i

derivative_input = int(input("Enter number to calculate derivative array:"))
number_of_array_input = int(input("which number of array?:"))
def n_th_order_difference(array, order): #Calculate nth order difference of given input

    length_of_input = len(array) # Check whether given order can be calculated or not
    if order >= length_of_input:  # Right hand side is 'm', thus order can be 'm-1' at max.
        raise ValueError("For an array with length 'm', order can not be greater than 'm-1'!")

    if order == 0:
        return array # Return the array itself if order is 0

    diff = [array[i+1] - array[i] for i in range(length_of_input-1)]  # First order difference
    for n in range(order-1):  # Repeat the difference order-1 times to get nth order difference
        diff = [diff[i+1] - diff[i] for i in range(len(diff) - 1)]
    return diff

print("-" * 21,"REPORT", "-" * 21)
print("-" * 50)
print("NO_OF_BINS =", NO_OF_BINS)
print("NO_OF_SAMPLES =", NO_OF_SAMPLES)
print("NO_OF_MOMENTS =", NO_OF_MOMENTS)
print("START_POINT =", START_POINT)
print("STOP_POINT =", STOP_POINT)
print("-" * 50)
print("Estimated mean =", estimated_mean)
print("True mean =", true_mean)
print("Error in mean estimation = ", abs(estimated_mean - true_mean))
print("-" * 50)
print("Estimated variance ", estimated_variance)
print("True variance =", true_variance)
print("Error in variance =", abs(estimated_mean - true_mean))
print("-" * 50)
print("Number of operations to obtain mean with PDF = ", len(t_new))
print("Number of operations to obtain mean without PDF = ", len(x_new))
print("Performance improvement = ", 1.0 - float(len(t_new)) / float(len(x_new)))
print("-" * 50)
print("Estimated x3 =", estimated_x3)
print("true_x3 =", true_x3)
print("Estimated x3 error = ", abs(estimated_x3 - true_x3))
print("-" * 50)
print("Factorial Output = ", factorial_output)
print("-" * 50)
print("moment_array =", moment_array)
print("Moment array first derivative = ", new_array)
print("-" * 50)
for n in range(derivative_input):
    print("moment array ", number_of_array_input,  "value =", moment_array[number_of_array_input])
    print("n_th_order_difference(moment_array, n)", number_of_array_input,  "value =", n_th_order_difference(moment_array, n)[number_of_array_input])
    print(f'Number of Derivative = {n}')
    print("Our Derivative =", n_th_order_difference(moment_array, n))
    print("Numpy test Derivative =", np.diff(moment_array, n))
    print("Difference between 2 derivative  = ", n_th_order_difference(moment_array, n) - np.diff(moment_array, n))
    print('*' * 50)
