import heapq

import wikipediaapi

# Wikipedia-API-Objekt erstellen mit spezifischem User-Agent
wiki = wikipediaapi.Wikipedia(
    language='de',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='MeinBot/1.0'
)



# Dijkstra-Algorithmus zur Berechnung des kürzesten Pfads zwischen zwei Wikipedia-Artikeln
def dijkstra_shortest_path(start_article, end_article):
    print(f"Starte Dijkstra von '{start_article}' nach '{end_article}'...")

    # Priority Queue für den Dijkstra-Algorithmus
    priority_queue = [(0, start_article)]
    # Dictionary zur Speicherung der kürzesten Entfernungen
    shortest_distances = {start_article: (0, None)}  # (Entfernung, Vorgänger)

    while priority_queue:
        current_distance, current_article = heapq.heappop(priority_queue)

        print(f"Betrachte Artikel: '{current_article}', Entfernung: {current_distance}")

        # Ziel erreicht, breche die Schleife ab
        if current_article == end_article:
            break

        # Abrufen der internen Verlinkungen des aktuellen Artikels über Wikipedia-API
        wiki_page = wiki.page(current_article)
        if not wiki_page.exists():
            continue

        print(f"Links gefunden'{wiki_page.links}'")

        links = [str(link).lower() for link in wiki_page.links]

        for link in links:
            new_distance = current_distance + 1  # Annahme: Jede Verlinkung hat Entfernung 1

            print(f"Prüfe Verlinkung zu '{link}', Neue Entfernung: {new_distance}")

            # Aktualisieren der kürzesten Entfernung, falls ein kürzerer Pfad gefunden wird
            if link not in shortest_distances or new_distance < shortest_distances[link][0]:
                shortest_distances[link] = (new_distance, current_article)
                heapq.heappush(priority_queue, (new_distance, link))

    # Aufbau des kürzesten Pfades von end_article zu start_article
    shortest_path = []
    current = end_article
    while current is not None:
        shortest_path.append(current)
        current = shortest_distances[current][1]  # Vorgänger des aktuellen Artikels

    shortest_path = shortest_path[::-1]  # Umkehrung des Pfades, um von start_article zu end_article zu gehen

    return shortest_path


def main():
    start_article = input("Bitte geben Sie den Startartikel ein: ").strip()
    end_article = input("Bitte geben Sie den Zielartikel ein: ").strip()

    shortest_path = dijkstra_shortest_path(start_article, end_article)

    print(f"\nKürzester Pfad von '{start_article}' nach '{end_article}':")
    if shortest_path:
        print(' -> '.join(shortest_path))
    else:
        print(f"Kein Pfad gefunden von '{start_article}' nach '{end_article}'.")


if __name__ == "__main__":
    main()
