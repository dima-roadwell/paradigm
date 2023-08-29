# Шаблон Наблюдатель:
# Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений. Создайте класс NotificationSystem (наблюдаемый объект), 
# который будет иметь методы для добавления наблюдателей и уведомления о событиях. 
# Создайте несколько наблюдателей, реагирующих на уведомления.

class Observer:
    def update(self, message):
        pass

class CurObserver(Observer):
    def update(self, message):
        print("Notice: ", message)

class NotificationSystem:
    _observers = []

    def appand_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


nots = NotificationSystem()

observer1 = CurObserver()
observer2 = CurObserver()

nots.appand_observer(observer1)
nots.appand_observer(observer2)

nots.notify("Payment is success")