if __name__ == '__main__':
    s = input('STRING: ')
    vg = ['A','E','I','O','U']
    list_c = list()
    list_v = list()
    qt = dict()
    first = s[0]
    c = 1
    str_c = str()
    str_v = str()

    if first in vg:
        str_v = s
        str_c = s[1:len(s)]
    else:
        str_c = s
        str_v = s[1:len(s)]
    
    for i in s:
        if i in vg:
            list_v.append(i)
  
    for i in s:
        if i not in vg:
            list_c.append(i)
    
    for i in s:
        if i in qt:
            qt[i] += 1
        else:
            qt[i] = 1
 
    class pos:
        def __init__(self,s,i):
            self.i = i
            self.ct = 1
            self.psb = list()
            self.st = s.index(self.i) #pendente
            print(self.st)
            self.ps = s[self.st:self.st+self.ct]
        
        def possb(self):
            i = self.i
            ct = self.ct
            psb = self.psb
            st = self.st
            ps = self.ps
            lps = 0
        
            while st+ct <= len(s):
                cps = ''.join(ps)
                psb.append(cps)
                ct += 1
                st = s.index(i)
                ps = s[st:st+ct]
                cps = ''.join(ps)
                lps = len(ps)+len(ps)

            return psb #parte
            
    
    total_c = list()
    total_v = list()
    c_main = list()
    v_main = list()
    lnsc = len(str_c)
    lnsv = len(str_v)
    cif = 0
    

    for i in list_c:
        c_part = pos(str_c,i).possb()
        c_main.extend(c_part)

    
    for i in c_main:
        while lnsc < len(c_main):
            if i == c_main[lnsc]:
                if len(i)+len(i)>=len(s):
                    if i != s:
                        cif += 1
                        if cif > 1:
                            del c_main[lnsc]
                            cif = 0
            lnsc +=1
        lnsc = len(s)-1

     
    for i in list_v:
        v_part = pos(str_v,i).possb()
        v_main.extend(v_part)

    for i in v_main:
        while lnsv < len(v_main):
            if i == v_main[lnsv]:
                if len(i)+len(i)>=len(s):
                    if i != s:
                        cif += 1
                        if cif > 1:
                            del v_main[lnsv]
                            cif = 0
            lnsv +=1
        lnsv = len(s)-1
