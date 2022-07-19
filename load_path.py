# n'importe quel module est un obbjet python
# => possède des attributs magiques
import os

if __name__ == "__main__":
    print(__name__)
    # print(__file__)
    PROJECT_DIR = os.path.dirname(__file__)
    print(PROJECT_DIR)