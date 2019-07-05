class School:
  def __init__(self, name, roster={}):
    self.name = name
    self.roster = roster

  def add_student(self, student_name, grade):
    if grade in self.roster.keys():
      self.roster[grade].append(student_name)
    else:
      self.roster[grade] = [student_name]

  def grade(self, grade):
    return self.roster[grade] 

  def sort_roster(self):
    new_roster = self.roster
    for key in new_roster:
      new_roster[key].sort()
    return new_roster  
   