def matrix(number):
    """Returns a 'n x n' matrix, with all element = 0"""
    matrix=[]
    for i in range(number):
        row=[0]*number
        matrix.append(row)
    return matrix


def initial(matrix):
    """Creats live cells in the pre-defined nxn  matrix"""
    matrix[0][1]=1
    matrix[1][1]=1
    matrix[2][1]=1
    return matrix


def alive(cell):
    """Checks if the cell is alive, Returns boolean"""
    if cell==1:
        return True
    else:
        return False

    
def die(next_position, row, col):
    """Kills the cell i.e funtion changes cell's value to 0 and updates matrix"""
    next_position[row][col]=0

    
def live(next_position,row,col):
    """Creates life in the cell i.e function changes cell's value to 1 and updates matrix"""
    next_position[row][col]=1

    
def alive_neighbour(first_position, row, col):
    """Returns the number of neighbouring cells that are alive"""
    size_limit=len(first_position)-1
    alive_mem = 0
    for row_probability in [-1, 0, 1]:

        for col_probability in [-1, 0, 1]:
            next_row = row + row_probability
            next_col = col + col_probability

            if next_row == row and next_col == col:
                continue
            
            if next_row < 0 or next_col < 0 or next_row > size_limit or next_col > size_limit:
                continue
            
            if alive(first_position[next_row][next_col]):
                alive_mem=alive_mem+1
    return alive_mem


def apply_rules(first_position,size):
    """  Applies rules of conway's game of life,and Returns the updated matrix  ."""
    next_position=matrix(size)

    for i in range (size):
        for j in range (size):
            if alive(first_position[i][j]) and alive_neighbour(first_position,i,j) in [2,3]:
                live(next_position,i,j)

            if not alive(first_position[i][j]) and alive_neighbour(first_position,i,j) == 3:
                live(next_position,i,j)

            if alive(first_position[i][j]) and alive_neighbour(first_position,i,j) < 2:
                die(next_position,i,j)

            if alive(first_position[i][j]) and alive_neighbour(first_position,i,j) > 3:
                die(next_position,i,j)

    return next_position


def display(count,size,first_position):
    """Displays the Matrix in a formatted fashion """
    print(f"Gen {count}\n")
    for i in range(size):
        for j in range(size):
            print("{:4}".format(first_position[i][j]),end=' ')
        print("\n")

        
def main():
    """Runs Conway's Game of Life in an infinte loop """
    size=3
    first_position=initial(matrix(size))
    count =0
    while True:
        display(count,size,first_position)
        time.sleep(1)
        first_position=apply_rules(first_position,size)
        count+=1

if __name__=='__main__':
    import time
    main()
