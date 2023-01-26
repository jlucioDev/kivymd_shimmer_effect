from View.base_screen import BaseScreenView
from View.MainScreen.components.card_listItem import CardListItem, CardListItemShimmer
from kivy.clock import Clock # Necessary for counting the time between transitions.

class MainScreenView(BaseScreenView):
  

    def on_enter(self):
        self.reload()

    def reload(self):

        self.ids.lst.clear_widgets()

        # Insert 15 widgets (card Shimmer) to simulate shimmer
        for i in range(15):
            self.ids.lst.add_widget(CardListItemShimmer())

        #Clock to simulate progress. 1s by step
        Clock.schedule_interval(self.simulate_shimmer, 1)


    count = 0
    def simulate_shimmer(self, *args):
        #print(f"contando: {self.I}")
        self.count +=1
        if self.count == 5:
            Clock.unschedule(self.simulate_shimmer)
            self.load_real_data()
            self.count = 0

    
    def load_real_data(self):

        self.ids.lst.clear_widgets()
        j = 0
        for i in range(35):
            
            j = j+1 if j < 8 else 1     # To load 8 images regardless of list size ;-)

            self.ids.lst.add_widget(CardListItem(texto= f"Text Example {j}", foto= f'./assets/images/{j}.jpeg'))
            




    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    
    
