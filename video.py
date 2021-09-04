import pygame
from constants import WIDTH, HEIGHT
import cv2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Состояния приложения:
START = 'START'
PLAY  = 'PLAY'
QUIT  = 'QUIT'


# отрисовка и обработка стартового экрана
def start_screen():
    # Задаем шрифт для отображения надписи
    font = pygame.font.SysFont('Arial', 20)
    # Надпись
    line = 'ПРОБЕЛ: Начать просмотр/Пауза/Снять с паузы. ESC: закончить'
    # Создаем объект Surface с надписью
    start_surf = font.render(line, True, WHITE, BLACK)

    clock = pygame.time.Clock()
    FPS = 25

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    return PLAY
        screen.fill(BLACK)
        screen.blit(start_surf, [10, 10])
        pygame.display.flip()
        clock.tick(FPS)
    return QUIT

# RGB
# BGR

# отрисовка и обработка видеоплеера
def play_movie():
    # полное имя файла с видео:
    filename = 'intro.mp4'

    # VideoCapture - класс для захвата видео из файла или с камеры
    # Создаем новый объект VideoCapture, используя файл filename.
    cap = cv2.VideoCapture(filename)

    # Захватываем, декодирует и получаем следующий видеокадр.
    # Первый возвращаемый аргумент принимает значение False, если захват не удался
    # Второ аргумеент принимает захваченное изображение
    ret, img = cap.read()
    print(ret)
    if not ret:
        # Ошибка: прочитать видео не удалось
        print("Can't read stream")
        return QUIT
    # Изменяем изображение кадра под размер формы
    img = cv2.resize(img, (WIDTH, HEIGHT))

    # транспонируем изображение, чтобы привести его в соотстветствие
    # с внутренним форматом изображения
    img = cv2.transpose(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # создаем поверхность Surface соответствующего размера, на которой будет отображаться видео:
    surface = pygame.surface.Surface((img.shape[0], img.shape[1]))
    # создаем объект clock для задержки в основном цикле:
    clock = pygame.time.Clock()
    # Устанавливаем частоту кадров в соответствии с частотой кадров в видео:
    FPS = 25
    # Загружаем фйл со звуковой дорожкой:
    pygame.mixer.music.load('intro.mp3')
    # Начинаем воспроизведение звука
    pygame.mixer.music.play(0)
    # Текущее состояние игры - PLAY
    scene = PLAY
    # Флаг, который указывает, что проигрывание стоит на паузе:
    on_pause = False
    running = True
    while running:
        # основной игровой цикл
        for event in pygame.event.get():
            # цикл обработки событий
            if event.type == pygame.QUIT:
                running = False
                scene = QUIT
            if event.type == pygame.KEYDOWN:
                # Нажатие ESC - завершить и вернуться в сотсояние START
                if event.key == pygame.K_ESCAPE:
                    running = False
                    scene = START
                if event.key == pygame.K_SPACE:
                    # Нажатие пробела - поставить на паузу /снять с паузы
                    on_pause = not on_pause

        if on_pause:
            # ставим звук на паузу:
            pygame.mixer.music.pause()

        else:
            # если не на паузе, играем звуковую дорожку:
            pygame.mixer.music.unpause()
            # захватываем и получаем следующий кадр:
            ret, img = cap.read()
            if not ret:
                # Ошибка: прочитать видео не удалось
                running = False
                scene = START
                break
            else:
                # изменяем изображение под размер формы
                img = cv2.resize(img, (WIDTH, HEIGHT))
                # Транспонируем полученное изображение:
                img = cv2.transpose(img)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # Непосредственно копируем значения из массива в Surface.
                # Так  быстрее, чем преобразование массива в Surface
                pygame.surfarray.blit_array(surface, img)
                # Отрисовываем поверхность на экране:
                screen.blit(surface, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)
    # Когда завершился основной цикл, останавливаем музыку:
    pygame.mixer.music.stop()
    return scene


pygame.init()
# Создаем экран:
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Задаем текущее состояние приложения:
scene = START
# Основной
def run_vid():
    global scene
    while scene!= QUIT:
        if scene == START:
            scene = start_screen()
        elif scene == PLAY:
            scene = play_movie()
            scene = QUIT
