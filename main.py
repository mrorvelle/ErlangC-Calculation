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
    
    calls_per_hour = num_calls / hours
    call_minutes = (AHT_secs / 60) * num_calls
    call_hours = int(call_minutes / 60)
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
          print(str(queue_nm) + " Projected Service Level: " + "{:.0%}".format(SL_calc) +
              " Using " + str(N) + " Agents")



# Input your variables here!
erlang_func(250, 1, 180, .9, 20, .85, .25, "queue 353")
erlang_func(2000, 1, 180, .8, 20, .85, .25, "queue 34")
