# my_dict = {
#     "name":"keshab aryal",
#     "age":24,
#     "gender":"male",
#     "is_married":"false"
# }

# print((my_dict.items())[0])



# keys_of_dict = ["name","age","gender","sex"]
# value_of_dict = ["kb",23,"male"]

# my_intro = dict.fromkeys(keys_of_dict,value_of_dict)
# print(my_intro)



student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def status(x):
    remark = ""
    if x<=70:
        remark = "Fail"
    elif x>71 and x<=80:
        remark = "Acceptable"
    elif x>81 and x<=90:
        remark = "Exceeds"
    else:
        remark = "Outstanding"
        
    return remark
        
# names = list(student_scores.keys())
# values = list(map(status,list(student_scores.values())))

# for key,value in zip(names,values):
#     student_grades[key] = value
    
# print(student_grades)
print(str(student_scores))