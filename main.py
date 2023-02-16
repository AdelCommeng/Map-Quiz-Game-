import turtle,pandas

screen=turtle.Screen()
screen.title("Canada Game")

image="Canada.gif"
screen.addshape(image)
turtle.shape(image)

#A function to locate the coordinates of the Provinces/Territories.
# def get_mouse_click_coor(x, y):
# #     print(x, y)
# #
# # turtle.onscreenclick(get_mouse_click_coor)
# # turtle.mainloop()

data=pandas.read_csv("13_provinces_and_territories.csv")

data_column=data["provinces_territories"]
data_list=data_column.to_list()

guessed_provinces_territories=[]
while len(guessed_provinces_territories) < 13:
    the_province=turtle.Turtle()
    the_province.color("Black")
    the_province.hideturtle()
    the_province.penup()
    answer_province=turtle.textinput(title=f"{len(guessed_provinces_territories)}/13 Provinces correct", prompt="What's another province?").title()
    if answer_province == "Exit":
        break
    for province in data_list:

        if answer_province ==province:
            guessed_provinces_territories.append(answer_province)
            print("Got it!")
            the_coordinates=data[data["provinces_territories"] == answer_province]
            the_province.goto(int(the_coordinates.x), int(the_coordinates.y))
            the_province.write(answer_province)
            data_list.remove(answer_province)



#If you gave up and type "Exit":
#Create a file of the Provinces/Territories you didn't guess right.
provinces_and_territories_to_learn= pandas.DataFrame(data_list)
provinces_and_territories_to_learn.to_csv("provinces_and_territories_to_learn.csv")

