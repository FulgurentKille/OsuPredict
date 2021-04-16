def convert_circle(circle):
    if len(circle) != 3:
        raise TypeError('Is not a circle')
    return circle


def convert_slider(slider):
    if len(slider) != 5:
        raise TypeError('Is not a slider')

    # On produit le cercle de début du slider
    liste_points = [{
        'Offset': slider['Offset'],
        'x': slider['x'],
        'y': slider['y']
    }]

    # TODO: Déterminer le slider à partir du point de départ et de ListePointsBezier

    # On produit tous les cercles restants du slider
    cpt = 1
    for point in slider['ListePointsBezier']:
        pos = point.split(':')
        offset = slider['Offset'] + (cpt / len(slider['ListePointsBezier'])) * slider['DureeSlider']
        liste_points.append({
            'Offset': round(offset),
            'x': pos[0],
            'y': pos[1]
        })
        cpt += 1

    return liste_points


def convert_spinner(spinner):
    if len(spinner) != 4:
        raise TypeError('Is not a spinner')
    return {'Offset': spinner['Offset'], 'x': spinner['x'], 'y': spinner['y']}


def convert_element(element):
    if len(element) == 3:
        return [convert_circle(element)]
    elif len(element) == 4:
        return [convert_spinner(element)]
    elif len(element) == 5:
        return convert_slider(element)
    else:
        raise TypeError('Is not a circle, a slider or a spinner')
