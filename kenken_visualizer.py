# Append to bottom of kenken.py

import time
import tkinter

def draw_board(puz, root):
    cells = []
    for r in range(puz.size):
        row = []
        for c in range(puz.size):
          # Draw borders for each of the cages
          if r == 0 or puz.board[r][c] != puz.board[r-1][c]:
            bordertop = 1
          else:
            bordertop = 0

          if c == 0 or puz.board[r][c-1] != puz.board[r][c]:
            borderleft = 1
          else:
            borderleft = 0

          label = BorderedFrame(root, width=8, height=4,
                                bordercolor='#000000',
                                borderleft=borderleft,
                                bordertop=bordertop,
                                interiorwidget=tkinter.Label,
                                font=('Arial', 14))
          label.grid(row=r, column=c)
          row.append(label)

        cells.append(row)
        
        # Add labels for each constraint
        for constr in puz.constraints:
            placed = False
            for r in range(puz.size):
                if placed:
                    break

                for c in range(puz.size):
                    if puz.board[r][c] != constr[0]:
                        continue
                    placed = True
                    cstr = str(constr[1])
                    if constr[2] != '=':
                        op = constr[2]
                        if op == '*':
                            op = '\u00d7'
                        if op == '/':
                            op = '\u00f7'
                        cstr += ' ' + op

                    label = tkinter.Label(text=cstr,
                                          bg='#ffffff',
                                          font=('Arial', 12))
                    label.place(x=96 * c + 5, y=96 * r + 5)
                    break

    return cells

def update_board(cells, puz):
  for r in range(puz.size):
    for c in range(puz.size):
      if isinstance(puz.board[r][c], Guess):
        new_str = str(puz.board[r][c].number)
      else:
        new_str = str(puz.board[r][c])

      if new_str != cells[r][c].interior['text']:
        cells[r][c].interior['bg'] = '#ccccff'
      cells[r][c].interior['text'] = new_str

def colour_cells(cells, colour):
  for r in range(len(cells)):
    for c in range(len(cells)):
      cells[r][c].interior['bg'] = colour

def animate_puzzle_run(puz, speed):
    root = tkinter.Tk()
    root.lift()

    # Draw the initial board
    cells = draw_board(puz, root)
    update_board(cells, puz)

    to_visit = []
    visited = []
    to_visit.append(puz)
    while to_visit!=[] :
        if find_blank(to_visit[0])==False:
            colour_cells(cells, '#ccffcc')
            break
        elif to_visit[0] in visited:
            to_visit.pop(0)
        else:
            # Draw the new board, colouring updated cells blue
            update_board(cells, to_visit[0])
            root.update_idletasks()
            root.update()

            # Wait to allow the cells to flash colour and then reset
            time.sleep(0.5 / speed)
            colour_cells(cells, '#ffffff')
            root.update_idletasks()
            root.update()
            time.sleep(0.5 / speed)
    
            # Generate new neighbours
            nbrs = neighbours(to_visit[0])
            new = list(filter(lambda x: x not in visited, nbrs))
            new_to_visit = new + to_visit[1:]
            new_visited = [to_visit[0]] + visited
            to_visit = new_to_visit
            visited = new_visited

    # If no solution was found, colour everything red
    if len(to_visit) == 0:
        colour_cells(cells, '#ffcccc')

    root.mainloop()

def animate_puzzle(puz, speed = 2):
    # Catch exceptions when the animation is interrupted
    import _tkinter
    try:
        animate_puzzle_run(puz, speed)
    except _tkinter.TclError:
        pass
