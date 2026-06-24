# User Stories

## User Story 01

As a student, I want to be able to **see all course numbers** that are offered so that I can see all of my options in one place.

## Acceptance Criteria
1. The program reads courses information from the input file.
2. The main menu provides an option to view all available courses.
3. The program displays all the offered course numbers.
4. Each course number should be displayed only once.
5. The course numbers should be visible while the student is selecting courses.


## User Story 02

As a student, I want to be able to **enter the amount of courses** I would like to register for so I can keep track of how many class I am in.

 ## Acceptance Criteria

1. The main menu provides an option to create a schedule.
2. The program prompts the student to enter the number of courses they want to register for.
3. If the input from the user is not an positive integer, the program should produce an error message.
4. The program prompts the user to enter input again after invalid input.
5. An empty numbered list is created and visual to the user.
6. The user can add or remove courses from the list.


## User story 03

As a student, I want to **enter distinct course numbers** so that I can create my schedule.

## Acceptance Criteria
1. The program prompts the student to enter course number.
2. The program verifies that the course number entered exists.
4. The program adds valid course numbers and information to the user's schedule
5. The schedule list is updated for the user to see.
6. The program should prevent a user from entering the same course number multiple times.
7. If no course matches the entered number, then the program must produce an error message.


## User Story 04

As a student, I want to view my generated schedule so that I know which course sections I should register for.

## Acceptance Criteria
1. The main menu should have the option to view the generated schedule.
2. The schedule displays the course number for each selected course.
3. The schedule displays the section number for each selected course.
4. The schedule displays the meeting days for each selected course.
5. The schedule displays the meeting start and end times for each selected course.
6. The schedule should display all requested courses successfully scheduled in the generated schedule.

## User Story 05

As a student, I want to be notified when no valid schedule can be found so that I know I need to select different courses.

## Acceptance Criteria 

1. The program determines whether a valid schedule exists.
2. The program checks all selected courses when generating a schedule.
3. If no valid schedule exists, the program displays a notification message.
4. The notification message informs the student that a schedule could not be found.
5. The program does not display a schedule when no valid schedule exists.

