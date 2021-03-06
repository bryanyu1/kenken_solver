# Constants
puz1=Puzzle(4,[[4,2,'a','a'],
               ['b', Guess('c',3),'a',4],
               ['b', Guess('c',1),Guess('c',4),2],
               [1,Guess('c',4),Guess('c',2),3]],
            [['c',96,'*'],['b',5,'+'],['a',3,'*']])

puz2=Puzzle(4,[[4,2,'a','a'],['b',3,'a',4],['b',1,4,2],
               [1,4,2,3]],[['b',5,'+'],['a',3,'*']])
    
puzzle1 = Puzzle(4, [['a','b','b','c'],
                     ['a','d','e','e'],
                     ['f','d','g','g'],
                     ['f','h','i','i']],
                 [['a',6,'*'],
                  ['b',3,'-'],
                  ['c',3,'='],
                  ['d',5,'+'],
                  ['e',3,'-'],
                  ['f',3,'-'],
                  ['g',2,'/'],
                  ['h',4,'='],
                  ['i',1,'-']])

puzzle2=Puzzle(6,[['a','b','b','c','d','d'],
                  ['a','e','e','c','f','d'],
                  ['h','h','i','i','f','d'],
                  ['h','h','j','k','l','l'],
                  ['m','m','j','k','k','g'],
                  ['o','o','o','p','p','g']],
               [['a',11,'+'],
                ['b',2,'/'],
                ['c',20,'*'],
                ['d',6,'*'],
                ['e',3,'-'],
                ['f',3,'/'],
                ['g',9,'+'],
                ['h',240,'*'],
                ['i',6,'*'],
                ['j',6,'*'],
                ['k',7,'+'],
                ['l',30,'*'],
                ['m',6,'*'],
                ['o',8,'+'],
                ['p',2,'/']])

puzzle1partial=Puzzle(4, [['a','b','b','c'],
                          ['a',2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

puzzle1partial2=Puzzle(4, [[Guess('a',2),'b','b','c'],
                          ['a',2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

puzzle1partial3=Puzzle(4, [[Guess('a',2),'b','b','c'],
                          [Guess('a',3),2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

puzzle1soln = Puzzle(4, [[2,1,4,3],[3,2,1,4],
                         [4,3,2,1],[1,4,3,2]], [])
                
puzzle2soln = Puzzle(6,[[5,6,3,4,1,2],
                      [6,1,4,5,2,3],
                      [4,5,2,3,6,1],
                      [3,4,1,2,5,6],
                      [2,3,6,1,4,5],
                      [1,2,5,6,3,4]], [])


puzzle3 = Puzzle(2,[['a','b'],['c','b']],[['b',3,'+'],
                                          ['c',2,'='],
                                          ['a',1,'=']])

puzzle3partial = Puzzle(2,[['a',Guess('b',1)],
                           ['c',Guess('b',2)]],
                          [['b',3,'+'],
                           ['c',2,'='],
                           ['a',1,'=']])

puzzle3partial2=Puzzle(3,[['a',Guess('b',1),'f'],
                         ['c',Guess('b',3),'f'],
                         ['d','d','d']],
                      [['b',2,'+'],
                       ['c',2,'='],
                       ['a',1,'='],
                       ['d',4,'+']])
                  
puzzle3soln = Puzzle(2,[[1,2],[2,1]],[])  

puzzle3c1 = Puzzle(2,[['a','b'],['c','b']],[['c',2,'='],
                                           ['b',3,'+'],
                                           ['a',1,'=']])

puzzle6 = Puzzle(6,[['a','a','b','b','b','d'],
                    ['a','a','c','b','e','d'],
                    ['f','g','g','i','e','d'],
                    ['f','h','i','i','l','l'],
                    ['f','k','k','l','l','n'],
                    ['m','m','m','n','n','n']], 
                 [['a',13,'+'],
                  ['b',180,'*'],
                  ['c',2,'='],
                  ['d',9,'+'],
                  ['e',20,'*'],
                  ['f',15,'+'],
                  ['g',6,'*'],
                  ['h',3,'='],
                  ['i',11,'+'],
                  ['k',2,'/'],
                  ['l',9,'+'],
                  ['m',8,'+'],
                  ['n',18,'+']])

puzzle6solution = Puzzle(6,[[1,4,3,5,2,6],
                            [3,5,2,6,4,1],
                            [4,6,1,3,5,2],
                            [5,3,6,2,1,4],
                            [6,2,4,1,3,5],
                            [2,1,5,4,6,3]], [])

puzzle4fun = Puzzle(4,[['a','a','a','a'],
                       ['a','a','a','a'],
                       ['a','a','a','a'],
                       ['a','a','a','a']], 
                    [['a',331776,"*"]])

puzzle4funsolution = Puzzle(4,[[1,2,3,4],
                               [2,1,4,3],
                               [3,4,1,2],
                               [4,3,2,1]], 
                            [])   
    
# Testing KenKen Solver
# print(solve_kenken(puz1))
# print(solve_kenken(puz2))
# print(solve_kenken(puzzle1))
# print(solve_kenken(puzzle2))

# Testing KenKen Visualizer
# animate_puzzle(puz1,speed = 2)
# animate_puzzle(puz2,speed = 2)
# animate_puzzle(puzzle1,speed = 2)
# animate_puzzle(puzzle2,speed = 2)
