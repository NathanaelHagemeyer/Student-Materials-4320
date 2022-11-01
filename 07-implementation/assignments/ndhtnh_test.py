import pytest
import System
import json
import Staff
import Student
import Professor


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

### --------------< ndhtnh Tests >------------- ###

#Test 1: test that the login function creates the proper user
def test_check_user_login(grading_system):
    grading_system.login(username2, '123454321')
    if grading_system.users[username2]['role'] != 'student':
        assert False

    #if grading_system.usr.


#Test 2: test that the check_password function correctly detects matching passwords
def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False


def test_change_grade(grading_system):
    testVal = 72
    grading_system.login(profUser, profPass)
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', testVal)

    grades = grading_system.usr.check_grades('yted91', 'software_engineering')

    for grade in grades:
        if grade[0] == 'assignment1':
            assert grade[1] == testVal


def test_create_assignment(grading_system):
    #insert test assignment
    grading_system.login(profUser, profPass)
    grading_system.usr.create_assignment('assignment3', '04/01/20', 'software_engineering')
    #grading_system.reload_data()

    #look in the proper course for that assignment
    grading_system.login('yted91', 'imoutofpasswordnames')
    assignments = grading_system.usr.view_assignments('software_engineering')
    foundAssignment = False
    for assignment in assignments:
        if assignment[0] == 'assignment3' and assignment[1] == '04/01/20':
            foundAssignment = True

    assert foundAssignment


def test_add_student(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.add_student('akend3', 'software_engineering')

    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('software_engineering')
    assert assignment[0] #An assignment exists!


def test_drop_student(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.drop_student('akend3', 'software_engineering')

    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('software_engineering')
    for assignment in assignments:
        assert False



def test_submit_assignment(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    grading_system.usr.submit_assignment('software_engineering', 'assignment1', 'TEST', '1/5/20')

    grades = grading_system.usr.check_grades('yted91', 'software_engineering')

    assert grades[0] == "N/A"


def test_check_ontime(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    assert grading_system.usr.check_ontime('1/5/20', '1/6/20')
    assert (grading_system.usr.check_ontime('1/7/20', '1/6/20')) is False


def test_check_grades(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')

    grades = grading_system.usr.check_grades('yted91')
    assert grades[0] == 3
    assert grades[1] == 5


def test_view_assignments(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')

    assignments = grading_system.usr.view_assignments('software engineering')
    assert assignment[0] == '1/1/20'
    assert assignment[0] == '2/1/20'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem