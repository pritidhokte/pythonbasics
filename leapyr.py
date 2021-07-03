yr = int(input("enter year"))
if ((yr%4)==0) and ((yr%100)==0) and  ((yr%400)==0) :


        print(f"{yr}year is leap")
else:
        print("not leap year")