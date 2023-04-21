from aiogram.dispatcher.filters.state import State, StatesGroup


# класс для обработки состояний
class WaitPhoto(StatesGroup):
    wait_photo = State()
