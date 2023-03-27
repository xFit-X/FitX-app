import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.models import ( Customer, Staff )
from App.controllers import ( create_customer, get_available_listings, get_all_customers, create_staff, get_all_staff, login, create_game, get_all_games, list_game )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_customer('bob', 'bobpass')
    create_staff('rob', 'robpass')
    create_game("Frogger", 1232)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
customer_cli = AppGroup('customer', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@customer_cli.command("create", help="Creates a customer")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_customer(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@customer_cli.command("list", help="Lists customers in the database")
def list_user_command():
    print(get_all_customers())

@customer_cli.command("login", help="Lists customers in the database")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def list_user_command(username, password):
    res = login(username, password)
    if res:
        print(f'{username} logged in!')
    else:
        print('login unsuccessful!')



app.cli.add_command(customer_cli) # add the group to the cli

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='Staff object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@staff_cli.command("create", help="Creates a staff user")
@click.argument("username", default="bob")
@click.argument("password", default="bobpass")
def create_user_command(username, password):
    create_staff(username, password)
    print(f'{username} created!')


@staff_cli.command("list", help="Lists the staff in the database")
def list_user_command():
    print(get_all_staff())


app.cli.add_command(staff_cli) # add the group to the cli

'''
Game Commands
'''

game_cli = AppGroup('game', help='Game object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@game_cli.command("create", help="Creates a game")
@click.argument("title", default="frogger")
@click.argument("rating", default="teens")
@click.argument("platform", default="NSW")
@click.argument("boxart", default="https://image.com/pic.png")
@click.argument("genre", default="platform")
def create_game_command(title, rating, platform, boxart, genre):
    create_game(title, rating, platform, boxart, genre)
    print(f'{title} created!')

@game_cli.command("list", help="Lists games in the database")
def list_game_command():
    print(get_all_games())


app.cli.add_command(game_cli)


'''
Listing Commands
'''

list_cli = AppGroup('listing', help='Game Listing commands') 

@list_cli.command("list", help="Lists the available listings in the database")
def get_listings_command():
    print(get_available_listings(None))

@list_cli.command("create", help="Lets a user list a game for rental")
def list_game_command():
    print(get_all_customers())
    userId = input('Enter a userId: ')
    print(get_all_staff())
    staffId = input('Enter a staffId: ')
    print(get_all_games())
    gameId = input('Enter a gameId: ')
    res = list_game(staffId, userId, gameId)
    if res:
        print('Game added to user!')
    else :
        print("error add game to user")

@list_cli.command("remove", help="Delists a game")
def delist_game_command():
    print(get_all_staff())
    staffId = input('Enter a staffId: ')
    print(get_available_listings())
    listingId = input('Enter a listingId: ')
    res = delist_game(staffId, listingId)
    if res:
        print('Game un listed')
    else :
        print("Error removing listing bad ID or unauthorized")

app.cli.add_command(list_cli)
