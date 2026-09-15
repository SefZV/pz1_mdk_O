class Timeup:
    def __init__(self, first=0):
        self.first = first
    
    @property
    def first(self):
        return self.__first
    
    @first.setter
    def first(self, value):
        if value < 0:
            raise ValueError("Число не может быть одинаковым")
        self.__first = value
    
    
    def read(self):
        try:
            self.first = int(input("Введите количество секунд: "))
        except ValueError:
            print("Ошибка введите число")
    
    def display(self):
        print(f"Всего секунд: {self.first}")
        
    def to_hourse_minutes_seconds(self):
        total = self.first
        
        hourse = total // 3600
        remaindex = total % 3600
        minutes = remaindex // 60
        seconds = remaindex % 60
        
        return f"Всего часов {hourse} минут {minutes} секунд {seconds}"
    

if __name__ == "__main__":
    z = Timeup()
    z.read()
    z.display()
    
    print(z.to_hourse_minutes_seconds())
        
    