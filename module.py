def del_col(f_arr:list, a:int):
    #create new list without "a" column form list "f_arr" 
    n_arr = []
    for i in range(len(f_arr)):
        if i != a:
            n_arr.append(f_arr[i])
    return n_arr
    

def add_col(f_arr_fst:list, f_arr_scnd:list, a: int, b:int, num_col_fst:int, num_col_scnd:int):
    #create new list with "b" column from "f_arr_scnd" adding it to list "f_arr_fst" after var "a"
    #if var "a" less or eq 0, then colum add as first colum in new list
    #if var "a" more then number of columns in list "f_arr_fst", 
    # then column will be added as the last column in new list
    n_arr=[]
    i = j = 0
    if  b>num_col_scnd:
        b=num_col_scnd-1
    else:
        b-=1    

    while i <= len(f_arr_fst)+len(f_arr_fst)/num_col_fst:
        c = i%(num_col_fst+1) #column
        r = i//(num_col_fst+1) #row

        if c==0 and a<=0:
            n_arr.append( f_arr_scnd[r+b] )
        elif c==num_col_fst and a>=num_col_fst:
            n_arr.append(r+b)
        elif a>0 and a<num_col_fst+1:
            n_arr.append(r+b)
        else:
            n_arr.append( f_arr_fst[j] )
            j+=1
        i+=1
        
