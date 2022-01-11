def bonAppetit(bill, k, b):
    # Write your code here
    real = (sum(bill) - bill[k]) / 2
    if real - b == 0:
        print("Bon Appetit")
    else:
        print(int(b-real))
