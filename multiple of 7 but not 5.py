def main():

  new_list = []

  for i in range (0,101):
    if i % 7 == 0 and i % 5 != 0:
      new_list.append(i)
  print(new_list)

main()
