'''
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the
 sequence (n is the input paramter).
 
 Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...
 
 You will need to figure out the rule of the series to complete this.
 
 Rules
 
 - You need to round the answer to 2 decimal places and return it as String.
 - If the given value is 0 then it should return "0.00".
 - You will only be given Natural Numbers as arguments.
 
 Examples (Input --> Output)
 n
 1 --> 1 --> "1.00"
 2 --> 1 + 1/4 --> "1.25"
 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
 '''
#My Solution:
def series_sum(n):
    if n == 0:
        return '0.00'
    else:
        sum = 0;
        for i in range(n):
            sum += 1 / (1 + i * 3)
        return format(sum, '.2f')
        
#Solution 2:
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

#Solution 3:
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum

#Solution 4:
def series_sum(n):
    a=0
    for i in range(n):
        a+=1/(3*i+1)
    return "{:.2f}".format(a)