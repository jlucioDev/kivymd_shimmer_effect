from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivymd.uix.relativelayout import MDRelativeLayout

# Widget to loading real data
class CardListItem(MDCard):
    texto = StringProperty()
    foto = StringProperty()


# Widget to Shimmer Effect
class CardListItemShimmer(MDRelativeLayout):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animate_shimmer()
        
    def animate_shimmer(self):
        # Transparent bar animation (left to right transition)
        anim = Animation(x= 400, duration=1) + Animation(x=-10, duration=.01) 
        anim.repeat = True
        anim.start(self.ids.animatedBar)
