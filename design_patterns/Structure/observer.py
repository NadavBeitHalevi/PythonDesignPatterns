from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(temperature: float, humidity: float, pressure: float) -> None:
        pass    

class ISubject(ABC):
    @abstractmethod
    def register_observer(observer: IObserver):
        pass

    @abstractmethod
    def remove_observer():
        pass
    
    @abstractmethod
    def notify_observers():
        pass

class WeatherStation(ISubject):
    def __init__(self):
        self.observers = [IObserver]
        self.temp = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    # implement the interface
    def register_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            if isinstance(observer, IObserver):
                observer.update(temperature=self.temp, humidity=self.humidity, pressure=self.pressure)
    
    def set_measurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

class ConsoneDisplay(IObserver):

    def __init__(self):
        print('Console Display initialized')

    def update(self, temperature: float, humidity: float, pressure: float):
        print('-------------------')
        print('Weather Station updated')
        print(f'Temperature: {temperature}, Humidity: {humidity}, Pressure: {pressure}')
        print('stay tuned for more updates...')
        print('-------------------')

if __name__ == '__main__':
    ws: ISubject = WeatherStation()
    console_display: IObserver = ConsoneDisplay()

    ws.register_observer(console_display)

    ws.set_measurements(80, 65, 30.4)