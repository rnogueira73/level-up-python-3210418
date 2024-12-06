def index_all(lists,toBeFound):
    indexList = []
    for i in range(len(lists)):
        if lists[i]==toBeFound:
            indexList.append([i])
        else:
            element = lists[i]
            for j in range(len(element)):
                if element[j]==toBeFound:
                  indexList.append([i,j])
                else:
                  subelement = element[j]
                  if isinstance(subelement,int):
                     if subelement == toBeFound:
                        indexList.append([i,j])
                  else:
                    for x in range(len(subelement)):
                      if subelement[x]==toBeFound:
                        indexList.append([i,j,x])
    return indexList

def index_all_opt(lists,toBeFound):
   indexList = []
   print("Inicia el programa")
   #print(f"lista con {indexList}")
   for index, value in enumerate(lists):
      print(f"Index: {index}")
      print(f"{value} es igual a {toBeFound}: {value==toBeFound}")
      if value == toBeFound:
        indexList.append([index])
        print(f"lista elementos con {indexList}")
      elif isinstance(lists[index], list):
        for i in index_all_opt(lists[index], toBeFound):
          print(i)
          indexList.append([index] + i)
          print(f"lista recursiva con {indexList}")
   print(f"regreso esta lista con {indexList}") 
   return indexList

# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    #print(index_all_opt(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all_opt(example, [1, 2, 3]))  # [[0, 0], [1]]
    # print(index_all_opt(example, 3))  
    # print(index_all_opt(example, 1))  
    # print(index_all_opt(example, 0))  
