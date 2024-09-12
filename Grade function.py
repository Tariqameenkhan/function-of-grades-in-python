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
calculate_total_marks(students_data)		







