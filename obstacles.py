import random
from game_state import state_game, state_menu, state_start, state_finished, state_running

terrain_types = ["ground", "grass"]

# On définit les différents types d'obstacles
obstacle_types = ["tree", "rock", "bush", "other_obstacle"]

terrain = [[0 if i in [0, 13] else None for i in range(14)] for j in range(20)]

# On définit les nombres minimum et maximum d'objets par ligne 
min_obstacles_per_line = 2
max_obstacles_per_line = 8  # Augmentez ce nombre pour augmenter la difficulté


for i in range(20):
    count_obstacles = 0
    for j in range(1, 13):
        if terrain[i][j] is None:
            if random.randint(1, 5) in [1, 2, 3] and count_obstacles <= max_obstacles_per_line:
                terrain[i][j] = obstacle_types[random.randint(0, 3)]
                count_obstacles += 1

for i in range(20):
    for j in range(1, 13):
        print(terrain[i][j])
    print("\n")

# On créé un dictionnaire pour stocker les types d'objets par ligne
obstacles_by_line = {}




terrain = [["" for _ in range(12)] for _ in range(14)]
cpt = 0
for line in terrain: 
    if cpt % 2 != 0:
         line = "grass" 

#print(terrain)

         


# def add_obstacles():  
#     # On vérifie l'état de la partie
#     if(state_game == state_start):
#         # On s'assure de ne pas mettre d'obstacles sur les 3 premières lignes au lancement du jeu 
#         for line in range(3, 13):
#             # On vérifie que les lignes sont bien des lignes d'herbe avant de mettre des obstacles
#             if(line is "grass"): 
#                 #On définit le nombre d'obstacles générés aléatoirement par ligne 
#                 nb_obstacles_herbe = random.randint(min_obstacles_per_line, max_obstacles_per_line)
#                 obstacles_on_line = random.sample(obstacle_types, nb_obstacles_herbe)
#                 # On stocke les obstacles pour cette ligne
#                 obstacles_by_line[line] = obstacles_on_line
#     elif state_game == state_running:
#         if(terrain[13] is "grass"):
#                 #On définit le nombre d'obstacles générés aléatoirement par ligne 
#                 nb_obstacles_herbe = random.randint(min_obstacles_per_line, max_obstacles_per_line)
#                 obstacles_on_line = random.sample(obstacle_types, nb_obstacles_herbe)
#                 # On stocke les obstacles pour cette ligne
#                 obstacles_by_line[terrain[13]] = obstacles_on_line








