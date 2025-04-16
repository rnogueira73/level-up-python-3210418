import csv

def merge_csv(inputfiles,mergefile):
  fieldnamesNew = []
  for file in inputfiles:
    with open(file,'r',encoding='utf-8') as inputfile:
      fieldnames = csv.DictReader(inputfile).fieldnames
      fieldnamesNew.extend(f for f in fieldnames if f not in fieldnamesNew)

  for file in inputfiles:
    with open(mergefile,'w',encoding='utf-8') as outputfile:
        writer = csv.DictWriter(outputfile, fieldnames=fieldnamesNew)
        writer.writeheader()
        for file in inputfiles:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)
                  
  return


if __name__ == '__main__':
  merge_csv(['alumnos_teorico.csv','alumnos_laboratorio.csv'],'all_students.csv')