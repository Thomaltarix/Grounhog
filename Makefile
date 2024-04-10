##
## EPITECH PROJECT, 2022
## Pong
## File description:
## Math project
##

SRC	=	groundhog.py

NAME =	groundhog

.PHONY: all clean fclean re tests_run

all: $(NAME)

$(NAME):
		cp $(SRC) $(NAME)
		chmod +x $(NAME)

clean:

fclean:
		rm $(NAME)

re: fclean all

tests_run:
