from player import Player
from npc import Npc, Event

def init():
    # Creación del mapa
    # El mapa es un esquema relacional; lugar: {[N, S, E, O], desc}
    map = {
        'habitación': {'dir': ['baño', None, 'comedor', None], 'desc': "pequeña, desordenada, donde paso la mayor parte del día."},
        'baño': {'dir': [None, 'habitación', None, None], 'desc': "pequeño pero acogedor."},
        'comedor': {'dir': ['cocina', None, 'entradita', 'habitación'], 'desc': "bastante espacioso. Aun no recogí las cajas vacias de pizza de ayer."},
        'cocina': {'dir': [None, 'comedor', None, None], 'desc': "una cocina normal, aunque algo caótica."},
        'entradita': {'dir': [None, 'calle', None, 'comedor'], 'desc': "pequeña y estrecha, con un mueble en el que suelo dejar las llaves y la cartera."},
        'calle': {'dir': ['entradita', 'tram', 'calle2', 'bus'], 'time': [0, 0, 5, 0], 'desc': "se respira un aire fresco que me motiva a no llegar tarde hoy también."},
        'calle2': {'dir': [None, None, 'entrada al campus', 'calle'], 'time': [0, 0, 5, 5], 'desc': "me estoy acercando al campus, aunque me estoy cansando ya de caminar."},
        'entrada al campus': {'dir': [None, None, 'centro del campus', 'calle2'], 'desc': ""},
        'centro del campus': {'dir': ['facultad', 'cafetería', 'parque', 'entrada al campus'], 'desc': "la mejor universidad de la zona, la verdad no sé ni cómo me aceptaron."},
        'cafetería': {'dir': ['centro del campus', None, None, None], 'desc': "lleno de gente de todo el campus. Está el camarero."},
        'facultad': {'dir': ['bar', 'centro del campus', None, 'clase'], 'desc': "es donde está tu clase. Ves a Nahuel saludándote."},
        'parque': {'dir':[None, None, None, 'centro del campus'], 'desc': "el parque es tan verde y encantador como siempre, dan ganas de quedarse aquí y no ir a clase. Hay una chica."},
        'bar': {'dir': [None, 'facultad', None, None], 'desc': ""},
        'clase': {'dir': [None, None, None, None], 'desc': "me espera Faraon, que se imaginaba que podría llegar tarde."},
        'bus': {'dir': [None, None, 'calle', None], 'desc': "estás en la parada del bus."},
        'tram': {'dir': ['calle', None, None, None], 'desc': "estás en la parada del tram."}
    }

    # Creación de eventos
    despertador = Event('habitación', {
        'normal':
        {
            '': {'message': """
    Suena el despertador. Que haces?
        1. Levantarte
        2. Posponer el despertador
    """},
            '1': {'message': """
    Apagas el despertador y te levantas. Empieza tu día.
""", 'end': True},
            '2': {'message': """
    Te quedas dormido hasta que vuelva a sonar.
    """, 'time': 5, 'repeat': True}
        }
    })
    ducha = Event('baño', {
        'normal':
        {
            '': {'message': """
    Deberías de darte una ducha.
        1. Con agua fría
        2. Con agua caliente
        3. No ducharme
    """},
            '1': {'message': """
    El agua fría te hace salir de la ducha más rápido.
    """, 'time': 10, 'end': True},
            '2': {'message': """
    Estabas tan a gusto bajo el agua caliente que se te pasa el tiempo.
    """, 'time': 30, 'end': True},
            '3': {'message': """
    Te pones algo de desodorante, esperando que no lo noten tus compañeros.
""", 'end': True}
        }
    })
    bus = Event('bus', {
        'normal':
        {
            '': {'message': """
    Quieres esperar al bus?
        1. Sí
        2. No
    """},
            '1': {'message': """
    Tras esperar un poco al bus, finalmente llega.
    """, 'time': 10, 'end': True},
            '2': {'message':"""
    """, 'end': True, 'return': 'bus'}
        }
    })
    tram = Event('tram', {
        'normal':
        {
            '': {'message': """
    Quieres esperar al tram?
        1. Sí
        2. No
    """},
            '1': {'message': """
    Tras esperar un poco al tram, finalmente llega.
    """, 'time': 10, 'end': True},
            '2': {'message':"""
    """, 'end': True}
        }
    })

    # Creación de personajes
    javier = Player(map, 'habitación')
    faraon = Npc('clase', {
        'tarde':
        {'': {'message': """
    "Por qué llegas tarde esta vez?"
        1. Un amigo estaba enfermo y necesitaba ayuda.
        2. El bus/tram falló y no llegué a tiempo.
        3. Dormí más de la cuenta y no pude levantarme.
        4. Faraón dame una alegria por favor que llevo 18 años sin tener ninguna.
    """},
         '1': {'message': """
    "Y seguro que no tenía a nadie más, invéntate una excusa mejor a la próxima."
    BAD ENDING: No haces el examen
    """, 'ending': True},
         '2': {'message': """
    "Haberte despertado antes, gandul."
    BAD ENDING: No haces el examen
    """, 'ending': True},
         '3': {'message': """
    "Al menos eres sincero, despiértate más pronto para la recuperación."
    BAD ENDING: No haces el examen
    """, 'ending': True},
         '4': {'message': """
    "Que sean otros 18 años más."
    BAD ENDING: No haces el examen
    """, 'ending': True}
    },
        'juan':
        {'': {'message': """
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
    """},
         '1': {'message': """
    "Eso es muy bonito, me alegro mucho por tí, pero a mí que me cuentas,
    has llegado tarde igual. Id a un hotel o algo que en esta clase no entras
    hasta la recuperación."
    Bueno, ya había asumido que iba a ir a la recuperación igualmente, al menos
    así me puedo quedar más rato con Juan.
    Además, Juan, sintiéndose culpable de hacerte llegar tarde al examen (como si
    no fueses ya tarde de por sí), te anima a estudiar y apruebas en la recuperación.
    GOOD ENDING: Juan
    """, 'ending': True}
    },
        'pronto':
        {'': {'message': """
    Llegas pronto. Faraón te deja pasar al examen, aunque te mira sorprendido. No está acostumbrado a que llegues pronto
    """, 'end': True}}
    })
    chica = Npc('parque', {
        'normal':
        {
            '': {'message': """
    Te acercas a la chica del parque, que está entretenida con unos gatos.
    No se da cuenta de tu presencia, así que te planteas qué decirle;
        1. Que monos los gatitos
        2. Sabes hacia dónde está la facultad de ingeniería?
        3. *Quedarse en silencio*
        4. *Irse*
    """},
            '1': {'message': """
    "Sii, se me acercan cuando llevo comida."
        1. 
        2. 
        3. 
    """},

            '2': {'message': """
    "Sí, sigue todo recto hacia el norte."
    """},

            '3': {'message': """
    "Necesitas algo?"
    """}
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

    eventos = {'despertador': despertador, 'ducha': ducha, 'bus': bus, 'tram': tram}
    personajes = {'faraon': faraon, 'chica': chica, 'nahuel': nahuel, 'ayuda': ayuda}
    return javier, map, eventos, personajes

def select_chat(player, npc, npcs):
    if npc == npcs['faraon']:
        if 'juan' in player.conditions:
            return 'juan'
        time = player.time
        if time < 30:
            return 'pronto'
        else:
            return 'tarde'
    else:
        return 'normal'
        
# bucle del juego
def start():
    player, map, eventos, npcs = init()
    print("""
Llevas unos meses estudiando ingeneria de IA en la universidad. Todos los dias intentas llegar a tiempo, pero siempre pasa algo que te lo impide.
Faraón, tu profesor, siempre dice lo mismo; "Tienes mas cuentos que Calleja", y es probable que no acepte más excusas.
Sabiendo que el día siguiente tienes el examen final de lógica, la asignatura de Faraón, repasas el temario y te vas a dormir, aunque algo tarde.
El examen es a las 9am, así que programas el despertador para las 8:30am.
""", end='')
    print(npcs['ayuda'])
    
    while True:
        player.describe()

        # Manejo de eventos
        if player.pos in Event.locs:
            for event in Event.npcs:
                if player.pos == event.pos and event not in player.conditions:
                    ret = player.hablar(event, select_chat(player, event, npcs))
                    player.conditions.append(event)
                    if ret:
                        player.conditions.append(ret)
                    break

        # Manejo de acciones
        accion = input('Acción: ').lower()
        if accion in ['norte', 'sur', 'este', 'oeste']:
            player.move(accion)
        elif 'coger' in accion:
            #AQUI hacer este trozo de código como eventos, diferentes chats para los ifs y seleccionar_chat para elegirlos
            if player.pos == 'entradita':
                if 'coger' in accion:
                    player.inv.append('cartera')
            if player.pos in ['bus', 'tram']:
                if 'bus' in player.conditions and player.pos == 'bus' or 'tram' in player.conditions and player.pos == 'tram':
                    print('Ya ha pasado.')
                    continue
                elif 'cartera' in player.inv:
                    print("Pagas un viaje y vas hacia el campus")
                    player.pos = 'entrada al campus'
                else:
                    print("No tienes dinero y el conductor te tira.")
                    player.pos = 'calle'
                player.conditions.append(player.pos)
        elif 'hablar' in accion:
            if player.pos in Npc.locs:
                for npc in Npc.npcs:
                    if player.pos == npc.pos:
                        if player.hablar(npc, select_chat(player, npc, npcs)):
                            return 0
                        break
            else:
                print("No hay nadie con quien hablar aquí.")
        elif 'ayuda' in accion:
            print(npcs['ayuda'], end='')
        elif 'salir' in accion:
            break

        print()

start()