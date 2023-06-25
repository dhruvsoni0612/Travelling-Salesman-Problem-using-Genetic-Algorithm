import random
import pygame
import sys
import math
import time
import matplotlib.pyplot as plt

def initialize_game():
    global num_cities
    num_cities = int(input("Enter the number of cities: "))
    
def main():
    pygame.init()
    popNum = 5000
    font = pygame.font.Font('freesansbold.ttf', 15)
    WIDTH = 600
    HEIGHT = 600
    PERCENTAGE = 0.5  # How much of the current population to crossover for the next generation

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Travelling Salesman Problem")

    class City:
        def __init__(self, x, y, i):
            self.x = x
            self.y = y
            self.num = i
            self.text = font.render(str(self.num), False, (255, 255, 255))

        def display(self):
            pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 5)

        @classmethod
        def place_city(cls):
            running = True
            city_placed = False
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        city = cls(mouse_pos[0], mouse_pos[1], len(cities))
                        cities.append(city)
                        city_placed = True
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                if city_placed:
                    break
                screen.fill((0, 0, 0))
                for city in cities:
                    city.display()
                    screen.blit(city.text, (city.x - 20, city.y - 20))

                # Draw axes with coordinates
                pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))
                pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

                # Add coordinate text
                for x in range(-WIDTH // 2, WIDTH // 2 + 1, 50):
                    text = font.render(str(x*2), False, (255, 255, 255))
                    screen.blit(text, (x + WIDTH // 2 - 10, HEIGHT // 2 + 10))
                for y in range(-HEIGHT // 2, HEIGHT // 2 + 1, 50):
                    text = font.render(str(y*2), False, (255, 255, 255))
                    screen.blit(text, (WIDTH // 2 + 10, y + HEIGHT // 2 - 10))

                pygame.display.update()

    # Dynamically create the cities based on the user input
    cities = []
    for i in range(num_cities):
        City.place_city()

    totalNum = len(cities)

    class Route:
        def __init__(self):
            self.distance = 0
            self.cityPath = random.sample(list(range(totalNum)), totalNum)

        def display(self):
            for i, cityNum in enumerate(self.cityPath):
                pygame.draw.line(screen, (0, 0, 255), (cities[self.cityPath[i]].x, cities[self.cityPath[i]].y),
                                 (cities[self.cityPath[i - 1]].x, cities[self.cityPath[i - 1]].y))

        def calcDistance(self):
            distance = 0
            for i, cityNum in enumerate(self.cityPath):
                distance += math.sqrt((cities[self.cityPath[i]].x - cities[self.cityPath[i - 1]].x) ** 2 +
                                     (cities[self.cityPath[i]].y - cities[self.cityPath[i - 1]].y) ** 2)
            self.distance = distance
            return distance

    population = [Route() for _ in range(popNum)]

    # Sorts the population on the basis of the fitness function, i.e., the distance of the route
    def sortPop(population):
        population.sort(key=lambda x: x.distance, reverse=False)
        return population

    '''
    Takes the top PERCENTAGE of the population for a particular generation and 
    produces a new population replacing the non-essential members with new ones
    '''

    def crossover(population):
        updatedPop = []
        updatedPop.extend(population[:int(popNum * PERCENTAGE)])

        for _ in range(popNum - len(updatedPop)):
            index1 = random.randint(0, len(updatedPop) - 1)
            index2 = random.randint(0, len(updatedPop) - 1)
            while index1 == index2:
                index2 = random.randint(0, len(updatedPop) - 1)
            parent1 = updatedPop[index1]
            parent2 = updatedPop[index2]
            p = random.randint(0, totalNum - 1)
            child = Route()
            child.cityPath = parent1.cityPath[:p]
            notInChild = [x for x in parent2.cityPath if not x in child.cityPath]
            child.cityPath.extend(notInChild)
            updatedPop.append(child)
        return updatedPop

    running = True
    counter = 0

    best = random.choice(population)

    minDistance = best.calcDistance()

    distances = []

    clock = pygame.time.Clock()
    while True:
        best.display()
        if counter >= popNum - 1:
            break
        clock.tick(60)
        pygame.display.update()
        screen.fill((0, 0, 0))
        for city in cities:
            city.display()
            screen.blit(city.text, (city.x - 20, city.y - 20))
        for element in population:
            element.calcDistance()

        population = sortPop(population)
        population = crossover(population)

        for element in population:
            if element.distance < minDistance:
                minDistance = element.calcDistance()
                best = element
            elif element.distance == minDistance:
                counter += 1

        distances.append(minDistance)  # Store the minimum distance at each generation

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

    print("The minimum distance is: {}".format(minDistance))
    print("A feasible path: {}".format(best.cityPath))
    best.display()
    pygame.display.update()
    time.sleep(5)

    # Plotting distance vs generation
    generations = list(range(len(distances)))
    plt.plot(generations, distances)
    plt.xlabel('Generation')
    plt.ylabel('Distance')
    plt.title('Distance vs Generation')
    plt.show()


if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))
    main()
