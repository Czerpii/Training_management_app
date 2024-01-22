from django.db import models


#validation functions
def validate_phone_number():
    pass


#models
class Address(models.Model):
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=200)
    building_numb = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.city}, {self.zip_code}, {self.street} {self.building_numb}"

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.company_name
    

class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    photo = models.ImageField(blank=True,
                              upload_to='participant_photos/',
                              default='participant_photos/default.jpg',)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
