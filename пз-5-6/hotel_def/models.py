from django.db import models

class Room(models.Model):
    number = models.CharField('Номер комнаты', max_length=10, unique=True)
    price_per_night = models.DecimalField('Цена за ночь', max_digits=10, decimal_places=2)
    floor = models.PositiveIntegerField('Этаж')
    
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
    
    
    def __str__(self):
        return f"Номер {self.number}"
    

class Guest(models.Model):
    fio = models.CharField('Имя Фамилия Отчество', max_length=150)
    passport = models.CharField('Паспорт', max_length=30, unique=True)
    phone = models.CharField('Номер телефона', max_length=20, unique=True)
    email = models.EmailField('Почта', unique=True)
    
    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
        
    def __str__(self):
        return f" ФИО: {self.fio}"
    
class Services(models.Model):
    name = models.CharField('Услуга', max_length=20, unique=True)
    price = models.DecimalField('Цена за услугу', max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
          
    def __str__(self):
        return f"{self.name}"
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name =  'bookings')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name = 'guests')
    services = models.ManyToManyField(Services, blank=True, related_name='bookings')
    date_arrival = models.DateField('Дата заезда')
    date_departure = models.DateField('Дата выезда')
    
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        
    def __str__(self):
        return f"Бронь {self.guest.fio} на номер {self.guest.phone}"
    


# Create your models here.
