#Haider Bokhari
#7 April 2019
#This program is to hold student information using 2 different classes. One class to hold personal information such as Name, birthday, address, and one is to hold course information such as course name, year, mark, and average.

#Class to hold student's personal information
class Student:
    """Class to hold personal information about the student such as name, address, email, and birthday"""
    
    #Function to initialise variables.
    def __init__(self, FirstName, LastName, Address, Email, Birthday):
        """Function to initialize variables"""
        self.FN=FirstName
        self.LN=LastName
        self.Add=Address
        self.Email=Email
        self.BDay=Birthday
        
    #Definition to edit student personal information
    def EditInfo(self):
        """Function which allows user to edit personal information of the student"""
        #Give user option on what to edit
        Option = int(input('What information do you wish to edit? \n1.First Name \n2.Last Name \n3.Address \n4.Email \n5.Birthday'))
        New = (raw_input('Enter new information.'))
        
        #Depending on which option the user picks, edit the information.
        if (Option==1):
            self.FN = New
        elif (Option==2):
            self.LN = New
        elif (Option==3):
            self.Add = New
        elif (Option==4):
            self.Email = New
        elif (Option==5):
            self.BDay = New        
            
        #Print student information at the end so that user can confirm it
        print "First Name: LastName: Address:   Email:     Birthday:"
        print self.FN, '   ', self.LN, ':', self.Add, ':',self.Email, ':',self.BDay
     
#Class to hold student's course information   
class Gradebook:
    """Gradebook class to hold specific student information such as call thier courses/marks"""
    
    #Function to initialize values
    def __init__(self, name, mark, yr, avrg, med):
        """Function to initialize all values"""
        
        #Add variables to lists so that more can be added/removed when needed.
        self.courseName = [name]
        self.Marks = [mark]
        self.year = [yr]
        self.average = [avrg]
        self.median = [med]
            
    #Function to add information to gradebook
    def Add(self):
        """Function to add student information to gradebook"""
        
        #Ask user for input, and store it in the previously created lists
        x= (raw_input('What course do you wish to add?'))
        self.courseName.append(x)
        z= int(input('What is the student\'s mark in this course?'))
        self.Marks.append(z)
        z= int(input('What year did the student take this course?'))
        self.year.append(z)        
        z= float(input('What is the class average for this course?'))
        self.average.append(z)
        z= float(input('What is the class median for this course?'))
        self.median.append(z)
        print 'Course successfully added!'
    
    #Function to remove information from gradebook
    def Remove(self):
        """Function to remove student information from gradebook"""
        
        #Ask user for input
        x= (raw_input('What course do you wish to remove?'))
        #Find index of the input
        ind=self.courseName.index(x)
        #Remove all related item in the index
        del self.courseName[ind]
        del self.Marks[ind]
        del self.year[ind]
        del self.average[ind]
        del self.median[ind]
        print 'Course successfully removed!'
    
    #Function to view course mark given name and year
    def View(self):
        """View a single course mark given course name and school year"""
        
        #Ask user for course name and year
        x= (raw_input('What course mark do you wish to see?'))
        y= int(input('What year was the course in?'))
        
        #Loop through course name list
        for c in self.courseName:
            #Find course index
            ind=self.courseName.index(c)
            #If course names match, and years match at the same index, then print the mark for that course.
            if x == c and y==self.year[ind]:
                print 'The mark for that course is', self.Marks[ind]
             
    #Function to view all gradebook information   
    def All(self):
        """View all gradebook information"""
        
        #Print a header
        print 'Course: Mark:  Year: Average: Median:'
        #X loops through all the indexes in the list
        for x in range(0, len(self.courseName)):
            #Print all information at specific index
            print self.courseName[x], "   ", self.Marks[x],"  ", self.year[x], "   ", self.average[x], "   ", self.median[x]
           
    def Edit(self):
        """Function which allows user to edit information of the student"""
        Option = int(input('What information do you wish to edit? \n1.Course Name \n2.Marks \n3.Year \n4.Average \n5.Median'))
        New = (raw_input('Enter new information.'))
        editing = (raw_input('For what course do you want to edit the information for?'))
        for r in range(0, len(self.courseName)):
            if self.courseName[r] == editing:
                ind=r

        #Depending on which option the user picks, edit the information at given index.        
        if (Option==1):
            self.courseName[ind] = New
        elif (Option==2):
            self.Marks[ind] = New
        elif (Option==3):
            self.year[ind] = New
        elif (Option==4):
            self.average[ind] = New
        elif (Option==5):
            self.median[ind] = New
            