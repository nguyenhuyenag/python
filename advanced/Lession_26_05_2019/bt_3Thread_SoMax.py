import threading
import random
import os
class SumThread(threading.Thread):
    def __init__(self, lo, hi,list_nums):
        threading.Thread.__init__(self)
        self.lo=lo
        self.hi=hi
        self.list_nums=list_nums
        self.Max=0
    def run (self):
        self.TimMax()

    def TimMax(self):
        i= self.lo
        self.Max=self.list_nums[i]
        while i<self.hi:
            if self.Max<self.list_nums[i]:
                self.Max= self.list_nums[i]
            i+=1
        return

    def get_max(self):
         return self.Max

    def print_list(self):
        str_list=""
        i=self.lo
        while i< self.hi:
            str_list+=str(self.list_nums[i])+ ";"
            i+=1
        return str_list

def Tim_Max(list_number, n_threads):
    max=0
    so_pt=len(list_number)
    list_threads=[]

    i=0
    while i< n_threads:
        lo= int ((i*so_pt)/n_threads)
        hi= int ((i+1)* so_pt/n_threads)
        thread=SumThread(lo,hi,list_number)
        list_threads.append(thread)
        list_threads[i].start()
        i+=1
    j=0
    while j<n_threads:
        list_threads[j].join()
        max =list_threads[j].get_max()
        print("Thread ",j+1,":",list_threads[j].print_list())
        print("- Max cua thread ",j+1,+ max)
        j+=1
    return max
os.system('cls')
if __name__=="__main__":
    list_number=[]
    n= int(input("Nhap so  phan tu:\t"))
    i= 0

    while i<n:
        list_number.append(random.randrange(10))
        i+=1
    print ("List:",list_number )
    n_threads= int(input("Nhap vao so thread:\t"))  
    max= Tim_Max(list_number,n_threads);
   
 
    