import random

x,px,py,px2,py2 = 0,0,0,0,0
matrix = [[0,0,0],[0,0,0],[0,0,0]]

# generate 9 unique numbers (0 to 8) and insert these numbers into matrix 
z = random.sample(range(0,9),9)

matrix[0] = [(z[0]), (z[1]), (z[2])]
matrix[1] = [(z[3]), (z[4]), (z[5])]   
matrix[2] = [(z[6]), (z[7]), (z[8])]
    

# print random matrix
print(matrix[0], matrix[1], matrix[2], sep="\n")
print ("")

# check win
def check_win():
    if matrix[0] == [1,2,3] and matrix[1] == [4,5,6] and matrix[2] == [7,8,0]:
        print ("you won")
        exit ()

# the game 
def main():
    
    check_win()
    print ("type number")
    x = int (input())

# check position of "0"
    for pozx,j in enumerate(matrix):
        for pozy,l in enumerate(j):
            if l==0:
                px = int(pozx)
                py = int(pozy)
                

# check position of moved number
    for pozx2,j in enumerate(matrix):
        for pozy2,l in enumerate(j):
            if l==x:
                px2 = int(pozx2)
                py2 = int(pozy2)
                
# check if the moved number is on the right place  (if we can use it)
    if (px == px2 or py == py2) and ((py+1 or py-1 == py2) or (px+1 or px-1 == px2)):
            matrix[px2][py2] = 0
            matrix[px][py] = x
            print(matrix[0], matrix[1], matrix[2], sep="\n")
            print ("")
        
    else:
        print ("wrong move, try again")
        print(matrix[0], matrix[1], matrix[2], sep="\n")
        
while __name__ == "__main__":
    main()






    



