#
# import numpy as np
#
# def recu_solution(f, b, a):
#     # Check and handle the padding of b
#     if len(b) > len(a):
#         raise ValueError('Length of b must be less than length of a')
#
#     # Adjust the padding of b to match the length of a
#     b_padded = np.pad(b, (len(a) - len(b), 0), 'constant') if len(b) < len(a) else b
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a))  # Adjust buffer to include the current output
#
#     for n in range(N):
#         # Calculate the feedforward contribution
#         feedforward_contribution = np.sum(b_padded[:min(n + 1, len(b_padded))] * f[n-min(n, len(b_padded)-1):n+1][::-1])
#
#         # Calculate the feedback contribution
#         feedback_contribution = np.sum(a[1:min(n + 1, len(a))] * buffer[1:min(n + 1, len(a))])
#
#         # Compute current output and update buffer[0]
#         buffer[0] = feedforward_contribution - feedback_contribution
#
#         # Store the current output in y
#         y[n] = buffer[0]
#
#         # Shift the buffer for the next iteration
#         if n < N - 1:
#             buffer[1:] = buffer[:-1]
#
#     return y


# import numpy as np
#
#
# def recu_solution(f, b, a):
#     # Check and handle the padding of b
#     if len(b) > len(a):
#         raise ValueError('Length of b must be less than length of a')
#
#     # Adjust the padding of b to match the length of a
#     b_padded = np.pad(b, (len(a) - len(b), 0), 'constant') if len(b) < len(a) else b
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a))
#
#     for n in range(N):
#         # Update buffer
#         buffer[0] = f[n]
#
#         # Calculate the feedback contribution
#         feedback_contribution = np.sum(a[1:] * buffer[1:])
#
#         # Subtract the feedback contribution from buffer[0]
#         buffer[0] -= feedback_contribution
#
#         # Calculate the feedforward contribution and store in y
#         y[n] = np.sum(b_padded * buffer)
#
#         # Shift the buffer for the next iteration
#         if n < N - 1:
#             buffer[1:] = buffer[:-1]
#
#     return y
#

import numpy as np

def recu_solution(signal_input, b_coeffs, a_coeffs):
    # Validate the lengths of b_coeffs and a_coeffs
    if len(b_coeffs) > len(a_coeffs):
        raise ValueError('Length of b_coeffs must be less than length of a_coeffs')

    # Pad b_coeffs if necessary to match the length of a_coeffs
    b_initial = np.pad(b_coeffs, (len(a_coeffs) - len(b_coeffs), 0), 'constant') if len(b_coeffs) < len(a_coeffs) else b_coeffs

    signal_length = len(signal_input)
    output_signal = np.zeros(signal_length)
    buffer = np.zeros(len(a_coeffs))

    for current_sample in range(signal_length):
        # Update the buffer with the current signal input
        buffer[0] = signal_input[current_sample]

        # Calculate the feedback contribution
        feedback_contribution = np.sum(a_coeffs[1:] * buffer[1:])

        # Subtract the feedback contribution from the first element of the buffer
        buffer[0] -= feedback_contribution

        # Calculate the feedforward contribution and store it in the output signal
        output_signal[current_sample] = np.sum(b_initial * buffer)

        # Shift the buffer for the next iteration
        if current_sample < signal_length - 1:
            buffer[1:] = buffer[:-1]

    return output_signal



#### MOST RECENT
"""
# import numpy as np
#
# def recu_solution(f, b, a):
#     # Check and handle the padding of b
#     if len(b) > len(a):
#         raise ValueError('Length of b must be less than length of a')
#
#     # Adjust the padding of b to match the length of a
#     b_padded = np.pad(b, (len(a) - len(b), 0), 'constant') if len(b) < len(a) else b
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a))  # Adjust buffer to include the current output
#
#     for n in range(N):
#         # Calculate the feedforward contribution
#         feedforward_contribution = np.sum(b_padded[:min(n + 1, len(b_padded))] * f[n-min(n, len(b_padded)-1):n+1][::-1])
#
#         # Calculate the feedback contribution
#         feedback_contribution = np.sum(a[1:min(n + 1, len(a))] * buffer[1:min(n + 1, len(a))])
#
#         # Compute current output and update buffer[0]
#         buffer[0] = feedforward_contribution - feedback_contribution
#
#         # Store the current output in y
#         y[n] = buffer[0]
#
#         # Shift the buffer for the next iteration
#         if n < N - 1:
#             buffer[1:] = buffer[:-1]
#
#     return y
"""



# import numpy as np
#
# def recu_solution(f, b, a):
#     # Check if b needs padding and handle accordingly
#     if len(b) > len(a):
#         raise ValueError('Length of b must be less than length of a')
#
#     initial_b = np.pad(b, (len(a) - len(b), 0), 'constant') if len(b) < len(a) else b
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a))  # Adjust buffer to include current output
#
#     for n in range(N):
#         # Calculate current input and feedback
#         current_input = f[n] if n < len(initial_b) else 0
#         feedback = np.sum(a[1:] * buffer[1:])
#
#         # Calculate current output
#         buffer[0] = current_input - feedback
#         y[n] = np.sum(initial_b * buffer)
#
#         # Shift buffer for next iteration
#         buffer[1:] = buffer[:-1]
#
#     return y







# import numpy as np
#
# def recu_solution(f, b, a):
#     # Pad b to match the length of a if necessary
#     if len(b) < len(a):
#         b = np.pad(b, (len(a) - len(b), 0), mode='constant')
#     else:
#         b = not_padded_b
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a)-1)  # Buffer for past outputs, excluding the current output
#
#     for n in range(N):
#         # Calculate the feedforward contribution using np.sum
#         if n < len(b):
#             feedforward_contribution = np.sum(b[:n + 1] * f[n::-1])
#         else:
#             feedforward_contribution = np.sum(b * f[n:n - len(b):-1])
#
#         # Calculate the feedback contribution using np.sum
#         feedback_contribution = 0
#         if n > 0:
#             feedback_contribution = np.sum(a[1:] * np.insert(buffer, 0, y[n-1])[:len(a)-1])
#
#         # Calculate the current output
#         current_output = feedforward_contribution - feedback_contribution
#
#         # Update buffer for next iteration: shift left and add current output
#         buffer = np.insert(buffer, 0, current_output)[:len(a)]
#
#         # Store the current output
#         y[n] = current_output
#
#     return y


#### the best one
'''
# import numpy as np
#
#
# def recu_solution(f, b, a):
#     if len(b) > len(a):
#         raise ValueError("The length of b must be less than or equal to the length of a.")
#
#     if len(b) < len(a):
#         b = np.pad(b, (len(a) - len(b), 0), mode='constant')
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a))  # Buffer for past outputs, excluding the current output
#
#     for n in range(N):
#         # Calculate the feedforward contribution using np.sum
#         if n < len(b):
#             feedforward_contribution = np.sum(b[:n + 1] * f[n::-1])
#         else:
#             feedforward_contribution = np.sum(b * f[n:n - len(b):-1])
#
#         # Calculate the feedback contribution using np.sum
#         feedback_contribution = np.sum(a[1:] * buffer)
#
#         # Calculate the current output
#         current_output = feedforward_contribution - feedback_contribution
#
#         # Update buffer for next iteration: shift left and add current output
#         buffer = np.insert(buffer, 0, current_output)[:len(a) - 1]
#
#         # Store the current output
#         y[n] = current_output
#
#     return y'''





# import numpy as np
#
#
# def recu_solution(f, b, a):
#     if len(b) < len(a):
#         b = np.pad(b, (len(a) - len(b), 0), mode='constant')
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a) - 1)  # Buffer for past outputs, excluding the current output
#
#     for n in range(N):
#         # Calculate the feedforward contribution using np.sum
#         if n < len(b):
#             feedforward_contribution = np.sum(b[:n + 1] * f[n::-1])
#         else:
#             feedforward_contribution = np.sum(b * f[n:n - len(b):-1])
#
#         # Calculate the feedback contribution using np.sum
#         feedback_contribution = np.sum(a[1:] * buffer)
#
#         # Calculate the current output
#         current_output = feedforward_contribution - feedback_contribution
#
#         # Update buffer for next iteration: shift left and add current output
#         buffer = np.insert(buffer, 0, current_output)[:len(a) - 1]
#
#         # Store the current output
#         y[n] = current_output
#
#     return y


# close to best one
'''
# import numpy as np
# 
# def recu_solution(f, b, a):
#     if len(b) < len(a):
#         b = np.pad(b, (0, len(a) - len(b)), mode='constant')
# 
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a) - 1)  # Buffer for past outputs, excluding the current output
# 
#     for n in range(N):
#         # Calculate the feedforward contribution using np.sum
#         feedforward_contribution = np.sum(b[:min(n+1, len(b))] * f[n-min(n, len(b)-1):n+1][::-1])
# 
#         # Calculate the feedback contribution using np.sum
#         feedback_contribution = np.sum(a[1:] * buffer)
# 
#         # Calculate the current output
#         current_output = feedforward_contribution - feedback_contribution
# 
#         # Update buffer for next iteration: shift left and add current output
#         buffer = np.insert(buffer, 0, current_output)[:len(a) - 1]
# 
#         # Store the current output
#         y[n] = current_output
# 
#     return y
'''

# best one

'''
# import numpy as np
#
# def recu_solution(f, b, a):
#     if len(b) < len(a):
#         b = np.pad(b, (0, len(a) - len(b)), mode='constant')
#
#     N = len(f)
#     y = np.zeros(N)
#     buffer = np.zeros(len(a) - 1)  # Buffer for past outputs, excluding the current output
#
#     for n in range(N):
#         # Calculate the feedforward contribution
#         if n < len(b):
#             feedforward_contribution = np.dot(b[:n+1], f[n::-1])
#         else:
#             feedforward_contribution = np.dot(b, f[n:n-len(b):-1])
#
#         # Calculate the feedback contribution
#         feedback_contribution = np.dot(a[1:], buffer)
#
#         # Calculate the current output
#         current_output = feedforward_contribution - feedback_contribution
#
#         # Update buffer for next iteration: shift left and add current output
#         buffer = np.insert(buffer, 0, current_output)[:len(a) - 1]
#
#         # Store the current output
#         y[n] = current_output
#
#     return y'''

# import numpy as np
#
# def recu_solution(f, b, a):
#     # Pad b if its length is less than that of a
#     if len(b) < len(a):
#         b = np.pad(b, (0, len(a) - len(b)), mode='constant')
#
#     def calculate_feedforward_sum(n):
#         # Vectorized computation of feedforward sum
#         valid_indices = np.arange(max(0, n - len(b) + 1), n + 1)
#         return np.sum(b[:len(valid_indices)] * f[n - valid_indices])
#
#     def calculate_feedback_sum(n):
#         # Vectorized computation of feedback sum
#         valid_indices = np.arange(1, min(n + 1, len(a)))
#         return np.sum(a[valid_indices] * y[n - valid_indices])
#
#     N = len(f)
#     y = np.zeros(N)
#
#     for n in range(N):
#         feedforward_sum = calculate_feedforward_sum(n)
#         feedback_sum = calculate_feedback_sum(n)
#         y[n] = feedforward_sum - feedback_sum
#
#     return y


# import numpy as np
#
# def recu_solution(f, b, a):
#     # if len(b) < len(a):
#     #     b=np.pad(b,(len(a)-len(b),0),mode='constant')
#     #  do something to stack on y for your padding
#     def calculate_feedforward_sum(n):
#
#         # Vectorized computation of feedforward sum
#         valid_indices = np.arange(max(0, n - len(b) + 1), n + 1)
#         return np.sum(b[:len(valid_indices)] * f[n - valid_indices])
#
#     def calculate_feedback_sum(n):
#
#         # Vectorized computation of feedback sum
#         valid_indices = np.arange(1, min(n + 1, len(a)))
#         return np.sum(a[valid_indices] * y[n - valid_indices])
#
#     if len(b) >= len(a):
#         raise ValueError("Length of b must be less than length of a")
#
#     N = len(f)
#     y = np.zeros(N)
#
#     for n in range(N):
#         feedforward_sum = calculate_feedforward_sum(n)
#         feedback_sum = calculate_feedback_sum(n)
#         y[n] = feedforward_sum - feedback_sum
#
#     return y


"""
# def recu_solution(f, b, a):
# # Check if len(b) > len(a) and raise an error if true
#     if len(b) > len(a):
#         raise ValueError("The length of b must be less than or equal to the length of a.")
#
#     # Initialize the output signal y with zeros
#     y = np.zeros_like(f)
#
#
#     for k in range(len(f)):
#         y[k] = b[0] * f[k]
#
#     # Compute the recursive part of the output signal based on a and b
#     for i in range(1, min(len(b), k + 1)):
#         y[k] += b[i] * f[k - i] - a[i] * y[k - i]
#
#     return y




# def recu_solution(f, b, a):
#
#     # def calculate_feedforward_sum(n):
#     #     # Feedforward sum adjusted for the current sample
#     #     sum_val = 0
#     #     for i in range(min(n + 1, len(b))):
#     #         sum_val += b[i] * f[n - i]
#     #     return sum_val
#     #
#     # def calculate_feedback_sum(n):
#     #     # Feedback sum adjusted for the current sample
#     #     sum_val = 0
#     #     if n == 0:  # No feedback at the first sample
#     #         return 0
#     #     for j in range(1, min(n, len(a))):
#     #         sum_val += a[j] * y[n - j]
#     #     return sum_val
#
#
#     # def calculate_feedforward_sum(n):
#     #     # Directly return b[0] * f[0] for the first element
#     #     # Handle the first element separately
#     #     if n == 0:
#     #         return b[0] * f[0]  if len(b) > 0 else 0 # Assuming b[0] exists, as len(b) < len(a)
#     #
#     #     # Vectorized computation of feedforward sum
#     #     valid_indices = np.arange(max(0, n - len(b) + 1), n + 1)
#     #     return np.sum(b[:len(valid_indices)] * f[n - valid_indices])
#     #
#     # def calculate_feedback_sum(n):
#     #
#     #     # Skip feedback computation for the first element
#     #     # Skip feedback for the first element
#     #     if n == 0:
#     #         return 0
#     #
#     #     # Vectorized computation of feedback sum
#     #     valid_indices = np.arange(1, min(n + 1, len(a)))
#     #     return np.sum(a[valid_indices] * y[n - valid_indices])
#
#     if len(b) >= len(a):
#         raise ValueError("Length of b must be less than length of a")
#
#     N = len(f)
#     y = np.zeros(N)
#
#     for n in range(N):
#         feedforward_sum = calculate_feedforward_sum(n)
#         feedback_sum = calculate_feedback_sum(n)
#         y[n] = feedforward_sum - feedback_sum
#
#     return y"""


##### do not use

# def recu_soultion(f, b, a):
#     if len(b) > len(a):
#         raise ValueError('Length of b must be less than a')
#
#     if len(b) < len(a):
#         b_padded = np.pad(b, (len(a) - len(b), 0), 'constant')
#
#     else:
#         b_padded = b
#
#     buf = np.zeros(len(a))
#     y = np.zeros_like(f)
#
#     for k in range(len(f)):
#         buf[0] = f[k] - a_contribution(a, buf)
#         y[k] = b_contribution(b_padded, buf)
#         buf[1:] = buf[:-1]
#     return y
#
#
# def a_contribution(a, buf):
#     return np.sum(a[1:] * buf[1:])
#
#
# def b_contribution(b, buf):
#     return np.sum(b * buf)
