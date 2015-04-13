import re
import glob

metadata = {}
questions = {}
solutions = {}

for filename in glob.glob("*.md"):
    with open(filename, "r") as f:
        lines = f.readlines()
        isAnswer = False
        question = ""
        previous_line = ""
        questionCount = 0
        next_line = ""
        
        for i in range(0, len(lines)):
            line = lines[i]

            if (next_line.startswith("===")):
                isAnswer = line.lower == "answer"
            
            elif (next_line.startswith("---")):
                topic = line
                questionCount = 0
        
            elif (re.match('^\d.', line)):
                print question
                print line
                question = line
                questionCount += 1
    
            elif (not re.match('(-|=)', line)):
                print line
                question += line
            else:
                print "DISCARDED?: " + line

def multiply(a, b):
    return a * b

def test_numbers_3_4():
    assert multiply(3,4) == 12 
      
def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 
