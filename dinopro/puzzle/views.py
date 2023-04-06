from django.shortcuts import render


def index(requests):
    """
    Представление главной страницы.
    """

    return render(requests, "puzzle/index.html")


def puzzle_game(requests):
    """
    Представление, отображающее страницу с игрой.
    """

    return render(requests, "puzzle/game.html")
