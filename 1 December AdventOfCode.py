

### 01/12/2022

def FindElfMostCal(CaloriesPerElfFile):
    #Open n read Files
    File = open(CaloriesPerElfFile, "r")
    text = File.read()
    text = text.split("\n\n")
    #print(text)
    #Turn into List for ease of data usage
    #Desired List: AND [ elf1,elf2,elf3], where elf1 = [Cal1,Cal2,Cal3]... OR [[Cal1,Cal2,Cal3],[Cal1], [Cal1,Cal2,Cal3]...]
    for pos, str in enumerate(text):
        if "\n" in str:
            text[pos] = [int(str) for str in text[pos].split("\n")] #texto[pos] = texto[pos].split("\n")
        else:
            text[pos]= [int(text[pos])]
    File.close()
    # Process - answer the problem => Elf with the most Calories in the meals they brought
    elfWithMostCalories = 0 # Saving the position of the elf with most Calories
    mostCalories = 0 # Saving the number of most calories to compare
    for posi, elfMeals in enumerate(text):
        #print(elfMeals)
        SumMeals = 0 # Summation of meals for each elf
        for position, string in enumerate(elfMeals):
            SumMeals += string
        if SumMeals > mostCalories:
            mostCalories = SumMeals
            elfWithMostCalories = posi
    print(f"Elf with Most Calories: nr{elfWithMostCalories+1}" ) # +1 to start at nr1 (there's no number 0 elf.)
    print(f"{mostCalories}")




if __name__ == "__main__":
    CaloriesPerElfFile = "1 Dec 2022 CaloriesElfo.txt"
    FindElfMostCal(CaloriesPerElfFile)