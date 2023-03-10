# KivyMD Shimmer Effect

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="bannerShimmer.png" alt="exemplo imagem">

> In this example I show how we can implement a shimmer effect with animation in kivymd.

# 👨‍💻Explain the code

> MainScreen has a list of MDList, containing a custom MDCard (CardListItem) that will receive the real data. This component has a similar Shimmer Widget (CardListItemShimmer) in the same file to be shown during data loading.
~~~python
class CardListItem(MDCard):
    texto = StringProperty()
    foto = StringProperty()


class CardListItemShimmer(MDRelativeLayout):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animate_shimmer()
        
    def animate_shimmer(self):
        anim = Animation(x= 400, duration=1) + Animation(x=-10, duration=.01) 
        anim.repeat = True
        anim.start(self.ids.animatedBar)
~~~

> The kv file has a MDFloatLayout (id: animatedBar), 20% transparent, to loop the widget from left to right, simulating a reflective effect:

~~~~python
<CardListItem>
    radius: 8
    size_hint_y: None
    height: 60
    adaptive_height: True
    md_bg_color: "lightblue"
    spacing: 10
    padding: 10

    FitImage:
        radius: 8
        allow_strech: True
        source: root.foto
        size_hint: None, None
        size: '50dp','50dp'
        pos_hint: {'center_x': 0.5,'center_y': 0.5}

    MDLabel:
        text: root.texto

<CardListItemShimmer>
    adaptive_height: True
    size_hint_y: None
    height: 60
    MDCard:
        id: ctShimmer
        radius: 15
        size_hint_y: None
        height: 60
        adaptive_height: True
        spacing: 10
        padding: 10

        MDWidget:
            radius: 8
            size_hint: None, None
            size: '50dp','50dp'
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            md_bg_color: "lightgray"

        MDBoxLayout:
            orientation: 'vertical'
            spacing:5
            MDWidget:
                radius: 3
                size_hint_x: .5
                md_bg_color: "lightgray"
            MDWidget:
                radius: 3
                md_bg_color: "lightgray"
            MDWidget:
                radius: 3
                md_bg_color: "lightgray"

    MDFloatLayout:
        id: animatedBar
        md_bg_color: 1,1,1,.2
        size_hint: None, None
        width: 30
        height: 50
~~~~

> The MainScreen code. Here has a clock module for simulate a sleep time and than reload data.

~~~~python

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

~~~~

## 💡 For more, please folow me in Youtube.
![](https://i.pinimg.com/originals/bf/a2/b0/bfa2b04f59dc9209c4fa212436e60884.png)
[http://youtube.com/@professorjoaolucio1](http://youtube.com/@professorjoaolucio1)

## 😄 Be one of the contributors <br>

Do you want to be part of this project? Click [HERE](CONTRIBUTING.md) and read how to contribute.

----
💲 Donates ➤
 https://www.paypal.com/donate/?business=KH88E4RQG2R9L&no_recurring=0&currency_code=BRL
----

## 📝 License

This project is under license. See the [LICENSE](LICENSE.md) file for more details.

[⬆ Voltar ao topo](#kivymd-shimmer-effect)<br>