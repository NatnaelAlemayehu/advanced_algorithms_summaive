def gradingStudents(gradelist):
    roundedgrades = []
    for a in gradelist:
        if a < 38: 
            roundedgrades.append(a)
        else:
            proximitytoNextMultipleofFive= 10 - ((a % 5) + 5)
            if proximitytoNextMultipleofFive < 3:
                nextMultipleofFive = a + proximitytoNextMultipleofFive
                roundedgrades.append(nextMultipleofFive)
            else:
                roundedgrades.append(a)        
    return roundedgrades

print(gradingStudents([73,67,38,33]))

