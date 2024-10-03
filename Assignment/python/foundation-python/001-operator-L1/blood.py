class BloodDonor:
    def __init__(self, name: str, blood_group: str):
      self.name=name
      self.blood_group=blood_group
      
    
    def can_donate(self, receiver_blood_group: str):
      print(self.name,self.blood_group,receiver_blood_group)
      if self.blood_group==receiver_blood_group:
        return"Good to go"
      elif self.blood_group=="O+":
        return"Good to go"
      elif receiver_blood_group=="AB+":
        return"Good to go"
      else:
        return"Not way to proceed"
donor=BloodDonor("rishabh","A+")      
result=donor.can_donate("AB+")
print(result)