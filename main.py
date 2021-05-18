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
    #print('Calls per hour')
    #print(calls_per_hour)
    call_minutes = (AHT_secs / 60) * calls_per_hour
    #print('Call minutes')
    #print(call_minutes)
    call_hours = int(call_minutes / 60)
    
    # raw # of agents required = N
    N = int(call_hours) + 1
    #print(N)
    
    factorial = 1
    for i in range(1, N + 1):
        factorial = factorial * i
    powers = call_hours**N
    X_Num = powers / factorial * (N / (N - call_hours))
    #print(factorial)
    #print(powers)
    #print(X_Num)


    
    import math
    denom = 0
    for i in range(N):
        if i == 0:
            denom = 1
        else:
            denom += (call_hours**i) / (math.factorial(i))

    #print(denom)
    
    prob = X_Num / (denom + X_Num)
    #print(prob)
    
    
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
          print(str(queue_nm) + " Projected Service Level: " + "{:.0%}".format(SL_calc) +
              " Using " + str(N) + " Agents, w/ ASA of " + str(ASA) + " seconds.")
          print("Calls answered immediately: " + "{:.0%}".format(prob))


#erlang_func(50,12,420,0.8,30,.25,.85,'PRJ100114 Duke Inound My Home Energy Report')
#erlang_func(20,12,420,0.8,30,.25,.85,'Combined Gates Under 10 Daily')
#erlang_func(1,13,420,0.8,30,.25,.85,'PRJ100798 FPLES Commercial Surge Sheild Inbound')
erlang_func(100,.5,180,0.8,20,.30,.85,'PRJ100799 FPLES Residential Surge Shield Inbound')
#erlang_func(8,13,540,0.8,30,.25,.85,'PRJ101335 Georgia Power Inbound Services')
#erlang_func(4,8,480,0.8,30,.25,.85,'PRJ101337 Nipsco APS Enrollment Services')
#erlang_func(5,13,420,0.8,30,.25,.85,'PRJ101338 Gulf Power Inbound Services')
#erlang_func(1,9,300,0.8,30,.25,.85,'PRJ102138 EnergyHub Potomac EV Programs')


