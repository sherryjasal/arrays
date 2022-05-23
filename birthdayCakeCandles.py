##cake will have one candle for each year of their total age. 
##They will only be able to blow out the tallest of the candles. 
## Count how many candles are tallest.

def birthdayCakeCandles(candles):
    count = 0
    max_candles = max(candles)
    for i in candles:
        if i == max_candles:
            count +=1
    return count

## Lessons learnt: find max first from the list and declare it outside the loop and then use counter
