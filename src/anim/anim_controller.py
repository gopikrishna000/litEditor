class AnimController:
    def __init__(self, widget, initial_blend, anim_time, updater_func):
        self.widget = widget
        self.updater_func = updater_func
        self.anim_rate = 1 / anim_time

        self.blend = initial_blend
        self.target = initial_blend

        self.animating = False
        self.updater_func(initial_blend)

    def animate_to(self, value):
        self.target = value
        if self.animating:
            return
        self.animating = True

        def animate():
            delta = self.target - self.blend
            self.blend = self.blend + delta * self.anim_rate * 100

            if not (0.1 > delta > -0.1):
                self.widget.after(100, animate)
            else:
                self.blend = self.target
                self.animating = False
            self.updater_func(self.blend)

        animate()
