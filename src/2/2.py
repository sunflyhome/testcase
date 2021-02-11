class class2:
    def __init__(self):
        self.textfile="2.txt"
        self.resultfile="2_result.txt"
    def generateNumbers(self):
        import random
        f = open(self.textfile, "a")
            
        for loop in range (0,5000000):
            f.write(str(random.randint(-214783648, 2147483647))+"\n")
        f.close()
    #32 bit , 5M numbers to 160M size file. 
    #no memory issue to do in-mem sorting
    def sortFile(self):
        f = open(self.textfile)
        nums = []
        for num in f:
            nums.append(num)
        f.close()
        nums.sort()
        outfile = open(self.resultfile, "w")
        for num in nums:
            outfile.writelines(num)
           
        outfile.close()

mytest2=class2()
#mytest2.generateNumbers()
mytest2.sortFile()