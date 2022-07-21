# %%
from multiprocessing import Process
import os
from time import sleep

# toutes les variables présentes dans le parent
# avant le lancement d'un worker
# sont disponibles pour le worker
CONSTANT = 10

def worker(n, m):
    print(f"PID du worker: {os.getpid()}")
    print(CONSTANT)
    for i in range(n + m, 0, -1):
        print(i)
        sleep(0.5)

def routine():
    print("do ya things")
    sleep(0.5)

# dans jupyter le code qui lancent des workers
# doit se trouver dans le bloc __main__
if __name__ == "__main__":
    print(f"PID du parent: {os.getpid()}")
    # création de l'objet processus
    p = Process(target=worker, args=(5, 4), name="countdown")
    # lancement du processus
    p.start()

    ## choix 1: attendre la fin du worker
    # p.join()

    ## choix 2: attendre la fin du worker jusqu'à un timeout
    # p.join(3)
    # envoi du signal SIGTERM (15) au process pour terminaison soft
    # p.terminate()
    # p.kill()
    # p.join()

    ## choix 3: exécuter des routines tant que le worker tourne
    while p.is_alive():
        routine()
    
    print(f"worker {p.name} ended with code {p.exitcode}")
    # libération mémoire => uniqument si le worker est terminé
    p.close()
# %%
