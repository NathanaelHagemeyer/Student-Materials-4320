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
    #grading_system.reload_data()

    grades = grading_system.usr.check_grades('yted91', 'software_engineering')
    #print(grades)
    for grade in grades:
        if grade[0] == 'assignment1' and grade[1] != testVal:
            assert False


def test_create_assignment(grading_system):
    #insert test assignment
    grading_system.login(profUser, profPass)
    grading_system.usr.create_assignment('assignment3', '04/01/20', 'software_engineering')
    #grading_system.reload_data()

    #look in the proper course for that assignment
    grading_system.login('yted91', 'imoutofpasswordnames')
    assignments = grading_system.usr.view_assignments('cloud_computing')
    foundAssignment = False
    for assignment in assignments:
        if assignment[0] == 'assignment3' and assignment[1] == '04/01/20':
            foundAssignment = True

    assert foundAssignment


def test_add_student(grading_system):

    assert True


def test_drop_student(grading_system):
    assert True


def test_submit_assignment(grading_system):
    assert True


def test_check_ontime(grading_system):
    assert True


def test_check_grades(grading_system):
    assert True


def test_view_assignments(grading_system):
    assert True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem