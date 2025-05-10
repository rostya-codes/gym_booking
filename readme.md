🎓 Сайт для бронирования спортивного зала / тренажерки
📌 Функционал:

    Регистрация/вход пользователей (спортсмены и админы)

    Просмотр расписания залов на неделю

    Онлайн-бронирование слота (время, дата, зал)

    Отмена брони

    Панель администратора:

        Управление расписанием (добавление слотов)

        Просмотр пользователей и их бронирований

    Email-уведомления или flash-сообщения при успешной броне/отмене

🧰 Технологии:

    Django (views, models, forms)

    PostgreSQL

    Bootstrap для UI

    Django messages framework

    (Дополнительно) Celery + Redis для email-уведомлений

💡 Почему это круто:

    Пригодно для реальной жизни

    Показывает навыки работы с расписаниями, формами, правами доступа

    Возможность потом расширить до приложения для зала или спортивного клуба я делаю сайт на джанго по такому тз, я пишу бек енд поэтому дай мне структуру и все html страницы для этого сайта используя bootstrap



🔧 Структура проекта

gym_booking/
├── templates/
│   ├── base.html
│   └── index.html
├── accounts/
│   └── templates/accounts/
│       ├── login.html
│       ├── register.html
│       └── profile.html
├── booking/
│   └── templates/booking/
│       ├── schedule.html
│       ├── booking_form.html
│       ├── booking_cancel.html
│       └── my_bookings.html
├── adminpanel/
│   └── templates/adminpanel/
│       ├── dashboard.html
│       ├── slot_add.html
│       └── users_list.html



| URL                | Template Path                               |
| ------------------ | ------------------------------------------- |
| `/login/`          | `accounts/templates/accounts/login.html`    |
| `/register/`       | `accounts/templates/accounts/register.html` |
| `/logout/`         | (нет шаблона, просто редирект)              |
| `/password-reset/` | (можно будет добавить шаблон позже)         |
| `/profile/`        | `accounts/templates/accounts/profile.html`  |

| URL                         | Template Path                                   |
| --------------------------- | ----------------------------------------------- |
| `/schedule/`                | `booking/templates/booking/schedule.html`       |
| `/my-bookings/`             | `booking/templates/booking/my_bookings.html`    |
| `/book/<int:slot_id>/`      | `booking/templates/booking/booking_form.html`   |
| `/cancel/<int:booking_id>/` | `booking/templates/booking/booking_cancel.html` |

| URL           | Template Path                                     |
| ------------- | ------------------------------------------------- |
| `/dashboard/` | `adminpanel/templates/adminpanel/dashboard.html`  |
| `/add-slot/`  | `adminpanel/templates/adminpanel/slot_add.html`   |
| `/users/`     | `adminpanel/templates/adminpanel/users_list.html` |



📌 Що робити — поетапно:
1. Головна сторінка

    Створи view-функцію, яка просто рендерить index.html.

    Пропиши шлях у main/urls.py.

2. Реєстрація та логін

    Зроби функцію для реєстрації (використай стандартну форму Django).

    Підключи login, logout, register у accounts/urls.py.

    Створи login.html і register.html.

3. Профіль користувача

    Зроби сторінку, яка показує інформацію про користувача (наприклад, ім’я, email).

    Ця сторінка має бути доступна лише авторизованим користувачам.

4. Розклад

    Створи модель слотів (наприклад, з датою, часом, статусом).

    Зроби view, який показує всі доступні слоти.

    Прив’яжи його до шаблону schedule.html.

5. Бронювання

    Створи модель бронювання (user + слот).

    Зроби view, який дозволяє користувачу забронювати вільний слот.

    Захисти доступ: лише авторизовані користувачі можуть бронювати.

6. Скасування броні

    Зроби view для видалення броні користувача (з підтвердженням).

    Сторінка booking_cancel.html.

7. Мої бронювання

    Зроби сторінку, яка показує всі бронювання поточного користувача.

    Шаблон: my_bookings.html.

8. Адмін-панель

    Зроби окрему сторінку dashboard.html, яка доступна лише для staff.

    Зроби форму для додавання нових слотів.

    Зроби сторінку зі списком всіх користувачів.
