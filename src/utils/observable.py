"""classes helpful for implementing Observer Pattern

Example usage:
    observable = Observable()

    # this lambda will be called for every dispatch call
    observable.observe(lambda value: print(value))

    # somewhere else
    observable.dispatch("Changed Value")
"""


class Observable:
    def __init__(self, initial_value):
        self.observers = list()
        self.value = initial_value

    def observe(self, observer):
        observer(self.value)
        self.observers.append(observer)

    def dispatch(self, value):
        self.value = value

        for observer in self.observers:  # notify observers
            observer(self.value)
