# function  total of list 	number


students_data=[	
  {	
    'name':'JohnDoe',	
    'marks':{
       'Math': 90, 
       'English': 90,	
       'Science': 78	
    }
  }
]	

#print(students_data)


def calculate_total_marks(students_data):		
    for student in students_data:		
        total_marks = sum(student['marks'].values())		
        print(f"Total marks for {student['name']}: {total_marks}")		
		
# Example usage		
#calculate_total_marks(students_data)		
students=[	
  {	
    'name':'JohnDoe',	
    'marks':{
       'Math': 90, 
       'English': 90,	
       'Science': 90	
    }
  }
]	


def grade(students):
    
    for student in students:
        total_marks = sum(student['marks'].values())
        num_subjects = len(student['marks'])
        average_marks = total_marks / num_subjects
        
        
        if average_marks >= 90:
            print(f"{student['name']} has an A Grade")
        elif average_marks >= 80:
            print(f"{student['name']} has a B Grade")
        elif average_marks >= 70:
            print(f"{student['name']} has a C Grade")
        else:
            print(f"{student['name']} has a Fail")
        print("")



grade(students)





