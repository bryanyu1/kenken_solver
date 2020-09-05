import copy

class Puzzle:
    '''
    Fields:
            size: Nat 
            board: (listof (listof (anyof Str Nat Guess))
            constraints: (listof (list Str Nat (anyof '+' '-' '*' '/' '='))))
    '''
    
    def __init__(self, size, board, constraints):
        self.size=size
        self.board=board
        self.constraints=constraints
        
    def __eq__(self, other):
        return (isinstance(other,Puzzle)) and \
            self.size==other.size and \
            self.board == other.board and \
            self.constraints == other.constraints
    
    def __repr__(self):
        s='Puzzle(\nSize='+str(self.size)+'\n'+"Board:\n"
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.board[i][j],Guess):
                    s=s+str(self.board[i][j])+' '
                else:
                    s=s+str(self.board[i][j])+' '*7
            s=s+'\n'
        s=s+"Constraints:\n"
        for i in range(len(self.constraints)):
            s=s+'[ '+ self.constraints[i][0] + '  ' + \
                str(self.constraints[i][1]) + '  ' + self.constraints[i][2]+ \
                ' ]'+'\n'
        s=s+')'
        return s    

class Guess:
    '''
    Fields:
            symbol: Str 
            number: Nat
    '''        
    
    def __init__(self, symbol, number):
        self.symbol=symbol
        self.number=number
        
    def __repr__(self):
        return "('{0}',{1})".format(self.symbol, self.number)
    
    def __eq__(self, other):
        return (isinstance(other, Guess)) and \
            self.symbol==other.symbol and \
            self.number == other.number        

class Posn:
    '''
    Fields:
            y: Nat 
            y: Nat
    '''         
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def __eq__(self,other):
        return (isinstance(other, Posn)) and \
            self.x==other.x and \
            self.y == other.y 
    
class BorderedFrame(tkinter.Frame):
  def __init__(self, master,
               bordercolor=None,
               borderleft=0,
               bordertop=0,
               borderright=0,
               borderbottom=0,
               interiorwidget=tkinter.Frame,
               **kwargs):
    tkinter.Frame.__init__(self, master, background=bordercolor, bd=0, highlightthickness=0)

    self.interior = interiorwidget(self, **kwargs)
    self.interior.pack(padx=(borderleft, borderright), pady=(bordertop, borderbottom))

## read_puzzle(fname) reads information from fname file and returns the info as 
##   Puzzle value.
## read_puzzle: Str -> Puzzle

def read_puzzle(fname):
    f = open(fname,"r")
    new_puz = f.readlines()
    new_puz_list1 = []   
    new_puz_list2 = []        
    f.close()
    for i in new_puz[1:]:
        for x in list(i):
            if ord(x) != 10 and x != " ":
                if x.isdigit():
                    new_puz_list1.append(int(x)) 
                else:
                    new_puz_list1.append(x)
        new_puz_list2.append(new_puz_list1) 
        new_puz_list1 = []
    new_puzzle = Puzzle(int(new_puz[0][0]), \
                        new_puz_list2[:int(new_puz[0][0])], \
                        new_puz_list2[int(new_puz[0][0]):])
    return new_puzzle

## print_sol(puz, fname) prints the Puzzle puz in fname file
## print_sol: Puzzle Str -> None

def print_sol(puz,fname):
    w = open(fname,"w")
    for i in puz.board:
        str_list = list(map(str,i))
        w.writelines("  ".join(str_list) + "  " + "\n")
    w.close()

## guess_counter(puz) returns the number of Guesses in the Puzzle (puz) 
## that have the same symbol as the first constraint of puz. 
## guess_counter: Puzzle -> Nat

def guess_counter(puz): 
    guess_count = 0
    for i in range(len(puz.board)):
        for x in range(len(puz.board)):
            if puz.constraints != [] and isinstance(puz.board[i][x],Guess) \
               and puz.board[i][x].symbol == puz.constraints[0][0]:
                guess_count += 1
            elif puz.constraints != [] and \
                 puz.constraints[0][0] == puz.board[i][x]:
                guess_count += 1
    return guess_count

## find_blank(puz) returns the position of the first blank
## space in puz, or False if no cells are blank.  If the first constraint has
## only guesses on the board, find_blank returns 'guess'.  
## find_blank: Puzzle -> (anyof Posn False 'guess')

def find_blank(puz):
    guess_num = guess_counter(puz)
    guesses = 0
    for x in range(len(puz.board)):
        for y in range(len(puz.board)):
            if puz.constraints != [] and isinstance(puz.board[x][y],Guess) \
               and puz.board[x][y].symbol == puz.constraints[0][0]:
                guesses += 1
                if guess_num == guesses:
                    return "guess"
            elif puz.constraints != [] and \
                 puz.constraints[0][0] == puz.board[x][y]:
                return Posn(y,x)
    return False

## used_in_row(puz, pos) returns a list of numbers used in the same 
## row as (x,y) position, pos, in the given puz.  
## used_in_row: Puzzle Posn -> (listof Nat)

def used_in_row(puz,pos):
    unsorted_list = []
    for i in puz.board[pos.y]:
        if isinstance(i,Guess):
            unsorted_list.append(i.number)
        elif not(isinstance(i,str)):
            unsorted_list.append(i)      
    sorted_list = sorted(unsorted_list)
    return sorted_list

## used_in_col(puz, pos) returns a list of numbers used in the same 
## column as (x,y) position, pos, in the given puz.  
## used_in_col: Puzzle Posn -> (listof Nat)

def used_in_col(puz,pos):
    unsorted_list = []
    col_puz = [] 
    for i in puz.board:
        col_puz.append(i[pos.x])    
    for i in col_puz:
        if isinstance(i,Guess):
            unsorted_list.append(i.number)
        elif not(isinstance(i,str)):
            unsorted_list.append(i)      
    sorted_list = sorted(unsorted_list)
    return sorted_list

##available_vals(puz,pos) returns a list of valid entries for the (x,y)  
## position, pos, of the consumed puzzle, puz.  
## available_vals: Puzzle Posn -> (listof Nat)

def available_vals(puz,pos):
    new_list = []
    not_poss_list = used_in_row(puz,pos) + used_in_col(puz,pos)
    for i in range(puz.size):
        new_list.append(i + 1)
    poss_list = list(filter(lambda x: not(x in not_poss_list),new_list))
    return poss_list

## place_guess(brd,pos,val) fills in the (x,y) position, pos, of the board, 
## brd,with the a guess with value, val
## place_guess: (listof (listof (anyof Str Nat Guess))) Posn Nat 
##              -> (listof (listof (anyof Str Nat Guess)))

def place_guess(brd,pos,val):
    res = copy.deepcopy(brd) 
    res[pos.y][pos.x] = Guess(res[pos.y][pos.x],val)
    return res

# fill_in_guess(puz, pos, val) fills in the pos Position of puz's board with 
# a guess with value val
# fill_in_guess: Puzzle Posn Nat -> Puzzle

def fill_in_guess(puz, pos, val):
    res=Puzzle(puz.size, copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    tmp=copy.deepcopy(res.board)
    res.board=place_guess(tmp, pos, val)
    return res

## guess_valid(puz) determines if the guesses in puz satisfy their constraint
## guess_valid: Puzzle -> Bool

def guess_valid(puz):
    guess_num_list = []
    change_num = 0
    for i in puz.board:
        for x in i:
            if isinstance(x,Guess):
                guess_num_list.append(x.number)
    if guess_num_list == []: 
        return False
    if len(guess_num_list) == 1 and puz.constraints[0][2] == "=": 
        if guess_num_list[0] == puz.constraints[0][1]:
            return True
    elif puz.constraints[0][2] == "+":
        if sum(guess_num_list) == puz.constraints[0][1]:
            return True 
    elif len(guess_num_list) == 2 and puz.constraints[0][2] == "-":
        if guess_num_list[0] - guess_num_list[1] \
               == puz.constraints[0][1] or \
           guess_num_list[1] - guess_num_list[0] \
               == puz.constraints[0][1]:
                return True
    elif len(guess_num_list) == 2 and puz.constraints[0][2] == "/":
        if guess_num_list[0] / guess_num_list[1] \
               == puz.constraints[0][1] or \
           guess_num_list[1] / guess_num_list[0] \
               == puz.constraints[0][1]:
                return True
    elif puz.constraints[0][2] == "*":
        mult_num = 1
        for x in guess_num_list:
            mult_num = mult_num * x
        if mult_num == puz.constraints[0][1]:
            return True    
    return False

## apply_guess(puz) converts all guesses in puz into their corresponding numbers
## and removes the first contraint from puz's list of constraints
## apply_guess: Puzzle -> Puzzle

def apply_guess(puz):  
    res = Puzzle(puz.size,copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    current1 = 0
    current2 = 0
    for i in res.board:
        for x in i:
            if isinstance(x,Guess): 
                res.board[current1][current2] = \
                    res.board[current1][current2].number
            current2 += 1
        current1 += 1
        current2 = 0
    res.constraints = res.constraints[1:]
    return res

## neighbours(puz) returns a list of next puzzles after puz in
## the implicit graph
## neighbours: Puzzle -> (listof Puzzle)

def neighbours(puz):
    tmp = Puzzle(puz.size,copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    puzzle_list = [] 
    to_fill = find_blank(tmp)
    if to_fill == "guess" and guess_valid(tmp):
        guess_applying = apply_guess(tmp)
        puzzle_list.append(guess_applying)
    elif isinstance(to_fill,Posn):
        poss_list = available_vals(tmp,to_fill)
        for i in poss_list:
            guess_filling = fill_in_guess(tmp,to_fill,i)
            puzzle_list.append(guess_filling)
    return puzzle_list
    
## solve_kenken(orig) finds the solution to a KenKen puzzle,
## orig, or returns False if there is no solution.  
## solve-kenken: Puzzle -> (anyof Puzzle False)

def solve_kenken(orig):
    to_visit=[]
    visited=[]
    to_visit.append(orig)
    while to_visit!=[] :
        if find_blank(to_visit[0])==False:
            return to_visit[0]
        elif to_visit[0] in visited:
            to_visit.pop(0)
        else:
            nbrs = neighbours(to_visit[0])
            new = list(filter(lambda x: x not in visited, nbrs))
            new_to_visit=new + to_visit[1:] 
            new_visited= [to_visit[0]] + visited
            to_visit=new_to_visit
            visited=new_visited     
    return False
