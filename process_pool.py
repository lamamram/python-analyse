from multiprocessing import Pool, cpu_count, current_process

def worker(task):
    return f"{task} done by {current_process().name}"


if __name__ == "__main__":
    with Pool(processes=cpu_count() - 2) as pool:
        # apply : un traitement sur un process et retour synchrone (bloquant)
        first_call = pool.apply(worker, args=("task n°1",))
        print(first_call)
        async_call = pool.apply_async(worker, args=("task n°2",))
        print("meanwhile...")

        # répartition de 5 traitements avec 5 paramètres différent sur 5 process et retour synchrone
        five_calls = pool.map(worker, [f"task_{i}" for i in range(3, 8) ])
        print(five_calls)
        # pool.map_async
        # pour les fonctions de plusieurs paramètres
        # pool.starmap(worker, [(, , ), (, , ), (, , )])
        # la pool n'accepte plus de lancer aucun call
        pool.close()
        # attente de la fin des process asynchrones si close
        pool.join()
        print(async_call.get())