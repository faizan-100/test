def main():
  outfile = open('data.txt', 'w')

  name = input("What is your name: ")

  outfile.write(name)

  outfile.close()

main()

