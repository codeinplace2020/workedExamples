import sys

def main():
  n = int(input("number of disks?"))
  # initialize our three towers
  one = []
  two = []
  three = []
  # start with all disks in our first tower
  for i in range(n, 0, -1):
    one.append(i)
  towers = [one, two, three]
  print("starting towers:")
  print_towers(towers)

  moves = solve(n, 0, 1, 2, towers)
  print("finishing towers: \n", one, two, three)

def print_move(source, destination, aux, towers):
  print ("moving disk from tower {} to tower {}".format(source, destination))
  print_towers(towers)

def print_towers(towers):
  for i in range(len(towers)):
    print("tower {}: {}".format(i, towers[i]))
  print()

def solve(n, source, destination, aux, towers):
  if n == 1:
    # remove from top of source tower
    disk_to_move = towers[source].pop()
    # add to destination tower
    towers[destination].append(disk_to_move)
    print_move(source, destination, aux, towers)

  else:
    solve(n-1, source, aux, destination, towers)
    # remove from top of source tower
    disk_to_move = towers[source].pop()
    # add to destination tower
    towers[destination].append(disk_to_move)
    print_move(source, destination, aux, towers)
    solve(n-1, aux, destination, source, towers)

if __name__ == "__main__":
  main()
