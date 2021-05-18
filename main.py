import pandas as pd
#CSV must contain following headers (QueueName as obj, Calls as int, Hours as int, AHT as int, SL as float64, AnsTime as int, MaxOcc as float64, Shrinkage as float 64, FTE as float64)
#result will write to FTE_Results.csv file
#Read in input
df = pd.read_csv("erlangtest.csv")
#verify types
print(df.dtypes)
#ErlangC Calc
def erlang_func(
    num_calls,
    hours,
    AHT_secs,
    SL,
    ans_time_secs,
    max_occ,
    shrinkage,
    queue_nm
):
    #explanation of calc at # https://www.callcentrehelper.com/erlang-c-formula-example-121281.htm
    calls_per_hour = num_calls / hours 
    call_minutes = (AHT_secs / 60) * calls_per_hour   
    call_hours = int(call_minutes / 60)   
    # raw # of agents required = N
    N = int(call_hours) + 1
    factorial = 1
    for i in range(1, N + 1):
        factorial = factorial * i
    powers = call_hours**N
    X_Num = powers / factorial * (N / (N - call_hours))
    import math
    denom = 0
    for i in range(N):
        if i == 0:
            denom = 1
        else:
            denom += (call_hours**i) / (math.factorial(i))
    prob = X_Num / (denom + X_Num)
    exponent = 2.71828**-((N - call_hours) * (ans_time_secs / AHT_secs))
    SL_calc = 1 - (prob * exponent)
    if SL_calc > SL:
        print(SL_calc, N)
    while SL_calc < SL:
        N += 1
        factorial = 1
        for i in range(1, N + 1):
            factorial = factorial * i
        powers = call_hours**N
        X_Num = powers / factorial * (N / (N - call_hours))
        import math
        denom = 0
        for i in range(N):
            if i == 0:
                denom = 1
            else:
                denom += (call_hours**i) / (math.factorial(i))
        prob = X_Num / (denom + X_Num)
        exponent = 2.71828**-((N - call_hours) * (ans_time_secs / AHT_secs))
        SL_calc = (1 - (prob * exponent))
        if SL_calc > SL:
          ASA = round((prob * AHT_secs) / (N - call_hours), 2)
          N = int(N / (1 - (shrinkage / 100)))
          return N
          #N is the FTE required
#update FTE column with FTE required
for i in df:
  df['FTE'] = df.apply(lambda x: erlang_func(x.Calls, x.Hours, x.AHT, x.SL, x.AnsTime, x.MaxOcc, x.Shrinkage, x.QueueName), axis=1)
#print results
print(df)
#save results
df.to_csv('FTE_Results.csv')