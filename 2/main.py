MAX_COURSE_PRICE = 100
courses = []

def get_manager_validation(course_price, ask_nicely):
    max_price = MAX_COURSE_PRICE
    if ask_nicely:
        max_price+=20
    return course_price.isdigit() and int(course_price) <= max_price


def main():
    print("Welcome to the Course Registration System")
    while True:
        course_name = input("Enter a course name: ")
        course_price = input("Enter a course price: ")

        if get_manager_validation(course_price, ask_nicely=False):
            courses.append(course_name)
        else:
            print("Course is too expensive, trying to ask nicely...")
            if get_manager_validation(course_price, ask_nicely=True):
                print("Success!")
                courses.append(course_name) 
            else:
                print("Sorry, but the course is too expensive!")
            
        print("Courses: ", courses, "\n")


if __name__ == '__main__':
    main()