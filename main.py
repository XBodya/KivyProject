from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.gridlayout import GridLayout

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

from kivy.uix.widget import Widget

from kivy.uix.textinput import TextInput

from kivy.uix.label import Label

from kivy.core.window import Window

from random import randint

from random import random

only_string_answer_to_user = None

only_bool_var_focus_on_input = False

what_quetion_is_queue = None

true_answer = False

Window.clearcolor = (.92, .32, .28, 1)

background_color = [.92, .35, .36, 1]

def on_focus(instance, value):

    global only_bool_var_focus_on_input

    only_bool_var_focus_on_input = bool(value)


def on_text(instance, value):

    global only_string_answer_to_user

    only_string_answer_to_user = value


def get_div_of_div(same_digit):

    lst_div_of_div = [i for i in range(1, same_digit) if not same_digit % i]

    if lst_div_of_div and len(lst_div_of_div) > 1:

        return lst_div_of_div[randint(1, len(lst_div_of_div) - 1)]

    else:

        return 1


class DigitWindApp(App):

    def build(self):

        self.quetion = ""
        
        self.view_quetion = Label(text=' ', font_size=55, halign="right", valign="center", size_hint=(1, .4))

        self.view_verdict = Label(text='_', font_size=40, halign="right", valign="center", size_hint=(.4, .5))

        self.ok_answer = Label(text='_', font_size=30, halign="right", valign="center", size_hint=(.4, .5))

        self.void = Label(text='', font_size=20, halign="right", valign="center", size_hint=(.4, .5))

        user_answer = TextInput(text="Ответ вводить здесь!", multiline=False, focus=False)

        user_answer.bind(focus=on_focus, text=on_text)

        all_btn_of_menu_all_layout = AnchorLayout()

        all_btn_of_box = BoxLayout(orientation='horizontal')

        all_btn_grid = GridLayout(cols=1, size_hint=[.7, 1])


        all_btn_grid.add_widget(Button(text="Ответить", on_press=self.check_quetion))

        all_btn_grid.add_widget(Button(text="Пропустить/Следующий", on_press=self.skip_quetion))

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(self.void)

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(self.ok_answer)

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(self.view_quetion)

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(self.view_verdict)

        all_btn_grid.add_widget(Widget())

        all_btn_grid.add_widget(user_answer)


        all_btn_grid.add_widget(Button(text='Сложение', on_press=self.generate_sum))

        all_btn_grid.add_widget(Button(text='Вычитание', on_press=self.generate_dis))

        all_btn_grid.add_widget(Button(text='Умножение', on_press=self.generate_pow))

        all_btn_grid.add_widget(Button(text='Деление', on_press=self.generate_div))

        all_btn_of_box.add_widget(all_btn_grid)

        all_btn_of_menu_all_layout.add_widget(all_btn_of_box)


        return all_btn_of_menu_all_layout

    def generate_sum(self, isinstance):
        global true_answer

        global what_quetion_is_queue

        digit_one_sum = randint(1, 999)

        digit_two_sum = randint(1, 999)

        self.quetion += (str(digit_one_sum) + " + " + str(digit_two_sum))

        true_answer = digit_one_sum + digit_two_sum

        what_quetion_is_queue = 0

        self.update_quetion()

    def generate_dis(self, isinstance):
        global true_answer

        global what_quetion_is_queue

        digit_one_dis = randint(1, 999)
        
        digit_two_dis = randint(1, digit_one_dis)

        self.quetion += (str(digit_one_dis) + " - " + str(digit_two_dis))

        true_answer = digit_one_dis - digit_two_dis

        what_quetion_is_queue = 1
        
        self.update_quetion()

    def generate_pow(self, isinstance):
        global true_answer

        global what_quetion_is_queue
        
        digit_one_pow = randint(1, 50)

        digit_two_pow = randint(1, digit_one_pow // 2)
        
        self.quetion += (str(digit_one_pow) + " X " + str(digit_two_pow))

        true_answer = digit_one_pow * digit_two_pow

        what_quetion_is_queue = 2

        self.update_quetion()

    def generate_div(self, isinstance):
        global true_answer

        global what_quetion_is_queue

        digit_one_div = randint(1, 100)

        digit_two_div = randint(1, digit_one_div)

        digit_two_div = get_div_of_div(digit_one_div)

        self.quetion += (str(digit_one_div) + " ÷ " + str(digit_two_div))

        true_answer = digit_one_div // digit_two_div

        what_quetion_is_queue = 3

        self.update_quetion()


    def update_quetion(self):

        self.view_quetion.text = self.quetion

        self.quetion = ""

        self.view_verdict.text = "_"

        self.ok_answer.text = "_"

    def check_quetion(self, isinstance):
        global true_answer

        global only_bool_var_focus_on_input

        global only_string_answer_to_user

        if str(only_string_answer_to_user).strip() == str(true_answer):

            self.view_verdict.text = 'Верно! :)'

            self.ok_answer.text = "Ответ:" + str(true_answer)

        elif str(only_string_answer_to_user).strip() != str(true_answer) and true_answer:

            self.view_verdict.text = "Неверно! :("
            
            self.ok_answer.text = "Ответ:" + str(true_answer)

        else:

            pass


    def skip_quetion(self, isinstance):
        global what_quetion_is_queue

        global true_answer

        if what_quetion_is_queue == 0:

            digit_one_sum = randint(1, 999)

            digit_two_sum = randint(1, 999)

            self.quetion += (str(digit_one_sum) + " + " + str(digit_two_sum))

            true_answer = digit_one_sum + digit_two_sum

            what_quetion_is_queue = 0

            self.update_quetion()


        elif what_quetion_is_queue == 1:

            digit_one_dis = randint(1, 999)
        
            digit_two_dis = randint(1, digit_one_dis)

            self.quetion += (str(digit_one_dis) + " - " + str(digit_two_dis))

            true_answer = digit_one_dis - digit_two_dis

            what_quetion_is_queue = 1
        
            self.update_quetion()

        elif what_quetion_is_queue == 2:

            digit_one_pow = randint(1, 50)

            digit_two_pow = randint(1, digit_one_pow // 2)
        
            self.quetion += (str(digit_one_pow) + " X " + str(digit_two_pow))

            true_answer = digit_one_pow * digit_two_pow

            what_quetion_is_queue = 2

            self.update_quetion()


        elif what_quetion_is_queue == 3:

            digit_one_div = randint(1, 100)

            digit_two_div = randint(1, digit_one_div)

            digit_two_div = get_div_of_div(digit_one_div)

            self.quetion += (str(digit_one_div) + " ÷ " + str(digit_two_div))

            true_answer = digit_one_div // digit_two_div

            what_quetion_is_queue = 3

            self.update_quetion()

        else:

            pass



DigitWindApp().run()