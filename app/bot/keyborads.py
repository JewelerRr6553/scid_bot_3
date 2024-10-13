from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.crud.questions import get_question_by_title
from app.crud.projects import get_all_prtfolio_projects, get_categories_by_name
from app.models.models import CheckCompanyPortfolio, ProductCategory
from sqlalchemy.ext.asyncio import AsyncSession

back_to_main_menu = InlineKeyboardButton(
    text='Вернуться к основным вариантам.',
    callback_data='back_to_main_menu'
)

back_to_previous_menu = InlineKeyboardButton(
    text='Назад к продуктам.',
    callback_data='back_to_previous_menu'
)

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Посмотреть портфолио.',
                callback_data='view_portfolio'
            )
        ],
        [
            InlineKeyboardButton(
                text='Получить информацию о компании.',
                callback_data='company_info'
            )
        ],
        [
            InlineKeyboardButton(
                text='Узнать о продуктах и услугах.',
                callback_data='products_services'
            )
        ],
        [
            InlineKeyboardButton(
                text='Получить техническую поддержку.',
                callback_data='tech_support'
            )
        ],
        [
            InlineKeyboardButton(
                text='Связаться с менеджером.',
                callback_data='contact_manager'
            )
        ],
    ]
)

company_information_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Презентация компании.',
                url='https://www.visme.co/ru/powerpoint-online/'
            )
        ],
        [
            InlineKeyboardButton(
                text='Карточка компании.',
                url='https://github.com/Rxyalxrd'
            )
        ],
        [back_to_main_menu]
    ]
)


async def inline_products_and_services(session: AsyncSession):
    """Инлайн клавиатура для продуктов и услуг."""

    keyboard = InlineKeyboardBuilder()

    objects_in_db = await get_all_prtfolio_projects(ProductCategory, session)

    for obj in objects_in_db:
        keyboard.add(InlineKeyboardButton(
            text=obj.title,
            callback_data=f'category_{obj.id}'
        ))

    keyboard.add(back_to_main_menu)

    return keyboard.adjust(1).as_markup()


company_portfolio_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Перейти к проектам.',
                callback_data='show_projects'
            )
        ],
        [back_to_main_menu]
    ]
)


async def list_of_projects_keyboard(session: AsyncSession):
    """Инлайн вывод проектов с данными из БД."""

    projects = await get_all_prtfolio_projects(CheckCompanyPortfolio, session)

    keyboard = InlineKeyboardBuilder()

    for project in projects:
        keyboard.add(
            InlineKeyboardButton(
                text=project.project_name,
                url=project.url
            )
        )

    keyboard.add(back_to_main_menu)

    return keyboard.adjust(1).as_markup()


support_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='F.A.Q',
                callback_data='get_faq'
            )
        ],
        [
            InlineKeyboardButton(
                text='Проблемы с продуктами',
                callback_data='get_problems_with_products'
            )
        ],
        [
            InlineKeyboardButton(
                text='Запрос на обратный звонок',
                callback_data='callback_request'
            )
        ],
        [back_to_main_menu]
    ]
)


async def faq_or_problems_with_products_inline_keyboard(
    question_type: str,
    session: AsyncSession
) -> InlineKeyboardMarkup:
    """Инлайн-клавиатуры для f.a.q вопросов или проблем с продуктами."""

    questions = await get_question_by_title(question_type, session)

    keyboard = InlineKeyboardBuilder()
    for question in questions:
        keyboard.add(
            InlineKeyboardButton(
                text=question.question,
                callback_data=f"answer:{question.id}"
            )
        )

    keyboard.add(back_to_main_menu)

    return keyboard.adjust(1).as_markup()


async def category_type_inline_keyboard(
    product_name: str,
    session: AsyncSession
) -> InlineKeyboardMarkup:
    """Инлайн клавиатура для типов в категориях."""

    category_types = await get_categories_by_name(product_name, session)

    keyboard = InlineKeyboardBuilder()

    for category_type in category_types:
        keyboard.add(
            InlineKeyboardButton(
                text=category_type.name,
                url=category_type.url
            )
        )

    keyboard.add(back_to_previous_menu)

    return keyboard.adjust(1).as_markup()
