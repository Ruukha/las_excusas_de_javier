from player import Player
from npc import Npc

# El mapa es un esquema relacional; lugar: [N, S, E, O]
map = {
    'habitación': (['baño', None, 'comedor', None], "Pequeña, desordenada, donde paso la mayor parte del día."),
    'baño': ([None, 'habitación', None, None], "Pequeño pero acogedor."),
    'comedor': (['cocina', None, 'entradita', 'habitación'], "Bastante espacioso, aun no recogí las cajas vacias de pizza de ayer."),
    'cocina': ([None, 'comedor', None, None], "Una cocina normal aunque algo caótica."),
    'entradita': ([None, 'calle', None, 'comedor'], "Pequeña y estrecha, con un mueble en el que suelo dejar las llaves y la cartera."),
    'calle': (['entradita', 'tram', 'calle2', 'bus'], "Se respira un aire fresco que me motiva a no llegar tarde hoy también.."),
    'calle2': ([None, None, 'entrada al campus', 'calle'], "Me estoy acercando al campus, aunque me estoy cansando ya de caminar."),
    'entrada al campus': ([None, None, 'centro del campus', 'calle2'], ""),
    'centro del campus': (['facultad', 'cafetería', 'parque', 'entrada al campus'], "La mejor universidad de la zona, la verdad no se ni como me aceptaron."),
    'cafetería': ([None, None, None, 'centro del campus'], "Lleno de gente de todo el campus. Esta el camarero."),
    'facultad': (['bar', 'centro del campus', None, None]),
    'parque': (['centro del campus', None, None, None], "El parque es tan verde y encantador como siempre, dan ganas de quedarse aqui y no ir a clase. Hay una chica."),
    'bar': ([None, 'facultad', None, None]),
    'clase': ([None, None, None, None], "Me espera Faraon, que se imaginaba que podria llegar tarde."),
    'bus': ([None, None, None, None], "Tras esperar al bus, finalmente llega, lleno de gente."),
    'tram': ([None, None, None, None], "Tras esperar al tram, finalmente llega, lleno de gente.")
}
javier = Player(map, 'habitación')
faraon = Npc('clase', {
    'tarde':
    {"": """
"Por qué llegas tarde esta vez?"
    1. Un amigo estaba enfermo y necesitaba ayuda.
    2. El bus/tram falló y no llegué a tiempo.
    3. Dormí más de la cuenta y no pude levantarme.
    4. Faraón dame una alegria por favor que llevo 18 años sin tener ninguna.
""",
     "1": """
"Y seguro que no tenía a nadie más, invéntate una excusa mejor a la próxima."
""",
     "2": """
"Haberte despertado antes, gandul."
""",
     '3': """
"Al menos eres sincero, pero nos veremos en la recuperación."
""",
     '4': """
"Que sean otros 18 años más."
"""
},
    'juan':
    {'': """
"Llegas tan tarde que ni una buena excusa me vale."
    1. Déjame explicartelo; hace unos días que voy bien de tiempo,
       así que suelo pasar a por un café antes de entrar a clase.
       Ahí es donde conocí a Juan, que me suele atender. Es un chico
       tan maravilloso que hasta me ha hecho darme cuenta de que soy
       gay, y hoy se ha levantado atrevido y se ha puesto a flirtear
       conmigo. Al final, nos hemos quedado ahí hablando demasiado rato,
       y se me ha hecho tarde, pero se ha hasta ofrecido a venir
       conmigo para que veas que no es una excusa, y que el amor
       lo puede todo.
""",
     '1': """
"Eso es muy bonito, me alegro mucho por tí, pero a mí que me cuentas,
has llegado tarde igual. Id a un hotel o algo que en esta clase no entras
hasta la recuperación."
Bueno, ya había asumido que iba a ir a la recuperación igualmente, al menos
así me puedo quedar más rato con Juan.
"""
},
    'pronto':
    {'': "Llegas pronto. Faraón te deja pasar al examen, aunque te mira sorprendido. No está acostumbrado a que llegues pronto"}
})
chica = Npc('parque', {
    'normal':
    {
        '': """
Te acercas a la chica del parque, que está entretenida con unos gatos.
No se da cuenta de tu presencia, así que te planteas qué decirle;
    1. Que monos los gatitos
    2. Sabes hacia dónde está la facultad de ingeniería?
    3. *Quedarse en silencio*
    4. *Irse*
""",
        '1': """
"Sii, se me acercan cuando llevo comida."
    1. 
    2. 
    3. 
""",

        '2': """
"Sí, sigue todo recto hacia el norte."
""",

        '3': """
"Necesitas algo?"
"""
    }
})
nahuel = Npc('facultad', {})
ayuda = """
Acciones       Descripcion
 ayuda          Muestra esta lista
 norte          Si es posible, iré al norte
 sur            Si es posible, iré al sur
 este           Si es posible, iré al este
 oeste          Si es posible, iré al oeste
 coger          Coger un objeto o transporte
 hablar         Hablas con el personaje de esa sala (si hay)
 salir          Saldrás de la partida
"""

# bucle del juego
def start():
    print("""
Llevas unos meses estudiando ingeneria de IA en la universidad. Todos los dias intentas llegar a tiempo, pero siempre pasa algo que te lo impide.
Faraon siempre dice lo mismo; "Tienes mas cuentos que Calleja", y es probable que no acepte mas excusas.
Sabiendo que el dia siguiente tienes el examen final de logica, la asignatura de Faraon, te preparas la alarma y te vas a dormir, aunque algo tarde.
""", end='')
    print(ayuda)
    
    while True:
        javier.describe()

        if javier.pos == 'bus':
            "Solo puedes coger el bus"
        elif javier.pos == 'tram':
            pass

        accion = input('Acción: ').lower()
        if accion in ['norte', 'sur', 'este', 'oeste']:
            javier.move(accion)
        elif 'coger' in accion:
            if javier.pos == 'entradita':
                if 'coger' in accion:
                    javier.inv.append('cartera')
            if javier.pos in ['bus', 'tram']:
                if 'cartera' in javier.inv:
                    print("Pagas un viaje y vas hacia el campus")
                    javier.pos = 'entrada al campus'
                else:
                    print("No tienes dinero y el conductor te tira.")
                    javier.pos = 'calle'
        elif 'hablar' in accion:
            if javier.pos in Npc.locs:
                for npc in Npc.npcs:
                    if javier.pos == npc.pos:
                        npc.hablar()
                        break
        elif 'ayuda' in accion:
            print(ayuda, end='')
        elif 'salir' in accion:
            break

        print()

start()