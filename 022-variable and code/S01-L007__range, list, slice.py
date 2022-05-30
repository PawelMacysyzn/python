color_list = ["red", "orange", "green", "violet", "blue", "yellow"]

color_list_3 = color_list[:3]  # ["red", "orange", "green"}

color_list_5 = color_list[:5]  # ["red", "orange", "green", "violet", "blue"]


def get_list_of_colors(list, n_colors):
    return list[:n_colors]


for inx in range(1, len(color_list) + 1):
    print(get_list_of_colors(color_list, inx))

# --------------------------------------------------------

text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

print(text[text.index('(') + 1:text.index(')')])
