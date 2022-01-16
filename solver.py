import time

def calcul(n,w,b,target,delay):
    def __output__(w):
        Out_ = []
        for n1 in n:
            for n2 in w:
                x = float(n1)*n2+b
                Out_.append(x)
                break
        pass
        return sum(Out_)
        del Out_[:]
        
    def fail_safe(W_list):
        w_set = set(W_list)
        contains_dupe = len(W_list) != len(w_set)
        if contains_dupe == True:
            return W_list[len(W_list)-1]
        
        else:
            del W_list[:len(W_list)-5]
            return False
        
        del w_set[:]
        
    def algorithm(W):
        new_w = [float(str(i)+".0"+str(i)) for i in range(0, len(W))]
        prog = 0.001
        div_state = 0
        count = 0
        W_list = []
        
        while True:
            my_logic = __output__(new_w)
            FS = fail_safe(W_list)
            
            if FS != False:
                return FS
                break
            else:
                W_list.append(str(new_w))
            
            if count > 26000:
                count = 0
                div_state += 10
                prog = prog/int(div_state)
            
            if 0> n[0]:
                if my_logic> target:
                    for i in range(len(new_w)):
                        new_w[i] += float(prog)
                
                elif my_logic < target:
                    for i in range(len(new_w)):
                        w[i] -= float(prog)
                
                elif my_logic == target:
                    break
                    
            else:
                if my_logic > target:
                    for i in range(len(new_w)):
                        new_w[i] -= float(prog)
                        
                elif my_logic < target:
                    for i in range(len(new_w)):
                        new_w[i] += float(prog)

                elif my_logic == target:
                    break
                
            count += 1                        
            time.sleep(delay)
            
        return new_w
                        
    return algorithm(w)

start = time.time()
print(calcul([4], [1.1,2,-2,1], 1, 7, 0))
end = time.time()
print("Returning time: ", end-start)
