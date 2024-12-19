
def enrollment_stats(data:list) -> list:
    """
    Calculate all of the student enrollment values, all of the tuition fees
    """

    students = [dat[1] for dat in data]
    tuition_fee = [dat[2] for dat in data]

    return students, tuition_fee

    
def mean(x:list) -> float:
    """
    Return mean of list
    """
    return sum(x)/len(x)



def median(x:list) -> float:
    """
    Return meadian of list
    """

    sorted_x = sorted(x)

    mid, mod = divmod(len(x), 2)

    if mod == 0:
        return (sorted_x[mid-1] + sorted_x[mid])/2
    else:
        return  sorted_x[mid] 



universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students, tuition_fees = enrollment_stats(universities)



print("*"*30)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition_fees):,}\n")

print(f"Students mean: {mean(students):,.2f}")
print(f"Students median: {median(students):,}\n")

print(f"Tuition mean: $ {mean(tuition_fees):,.2f}")
print(f"Tuition median: $ {median(tuition_fees):,}")
print("*"*30)