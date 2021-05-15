"""classes helpful for implementing Observer Pattern

Example usage:
    observable = Observable()

    class something(Lifecycle):
        def __init__(self):
            # this lambda will be called for every dispatch call
            observable.observe(self,lambda value: print(value))

    # somewhere else
    observable.dispatch("Changed Value)
"""


class Lifecycle:
    def __init__(self):
        self.active = True

    def dispose(self):
        self.active = False


class Observable:
    def __init__(self, initial_value):
        self.observers = list()
        self.value = initial_value

    def observe(self, lifecycle, observer):
        if lifecycle.active:
            observer(self.value)
            self.observers.append((lifecycle, observer))

    def dispatch(self, value):
        self.value = value

        self.observers = [tup for tup in self.observers if tup[0].active]  # remove inactive observers

        for tup in self.observers:  # notify active observers
            tup[1](self.value)
