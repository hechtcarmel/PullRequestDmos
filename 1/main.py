

MAX_COURSE_PRICE = 100
courses = []

def get_manager_validation(course_price):
    return course_price.isdigit() and int(course_price) <= MAX_COURSE_PRICE

def main():
    print("Welcome to the Course Registration System")
    while True:
        course_name = input("Enter a course name: ")
        course_price = input("Enter a course price: ")

        if get_manager_validation(course_price):
            courses.append(course_name)
        else:
            print("Sorry, but the course is too expensive!")
            
        print("Courses: ", courses, "\n")


if __name__ == '__main__':
    main()