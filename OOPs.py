class Car:
    def detail(instance):
        print(f"Brand : {instance.Brand} , Model : {instance.Model} ")
class HybridCar(Car):
    def choice(instance):
        print(f"Fuel Choices :{instance.fuel1} or {instance.fuel2} ")
hc = HybridCar()
hc.Brand="Toyota"
hc.Model="Camry 2023"
hc.fuel1="petrol"
hc.fuel2="diesel"
hc.detail()
hc.choice()