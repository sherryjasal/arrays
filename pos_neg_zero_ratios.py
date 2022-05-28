##Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
##Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    length = len(arr)
    pos_count = 0;
    neg_count = 0;
    zero_count = 0;
    for num in arr:
        if (num > 0):
            pos_count +=1;          
        elif (num < 0):
            neg_count +=1;   
        elif (num == 0):
            zero_count +=1;
    print("{:.6f}".format((pos_count/length)))    
    print("{:.6f}".format((neg_count/length)))
    print("{:.6f}".format((zero_count/length)))
    
    #lessons learnt: always use counter for count
    # printing in decimals "{:.6f}".format()
