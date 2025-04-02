from flask import Flask, render_template, redirect, url_for, request, flash, session
from markupsafe import Markup


app = Flask(__name__)
app.secret_key = 'blablabla123465789qweqweqwe'

# Дані для входу в адмінку (тимчасові, можна замінити на БД)
ADMIN_CREDENTIALS = {"username": "admin", "password": "admin123"}

publications = [
    {"id": 1, "title": "Як впоратися зі стресом", "content": "Стаття про стратегії подолання стресу..."},
    {"id": 2, "title": "5 порад для здорової психології", "content": "Ключові рекомендації для поліпшення ментального здоров'я..."}
]

@app.route('/')
def home():
    return render_template('index.html', title="Головна сторінка")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if len(message) < 10:
            flash("Повідомлення має містити мінімум 10 символів", "danger")
        else:
            # Тут можна зберігати дані в базу або надсилати email
            flash("Ваше повідомлення успішно надіслано!", "success")
            return redirect(url_for('contact'))

    return render_template('feedback.html')

"""
@app.route('/psychologists')
def psychologists_list():
    return render_template('psychologists.html', psychologists=psychologists)

@app.route('/psychologist/<int:id>')
def psychologist_detail(id):
    psychologist = next((p for p in psychologists if p['id'] == id), None)
    if psychologist is None:
        return "Психолога не знайдено", 404
    return render_template('psychologist_detail.html', psychologist=psychologist)
"""

@app.route('/psychologists')
def psychologists():
    psychologists_data = [
        {"id": 1, "name": "Наталія Салівон", "specialty": "Сертифікований гештальт-терапевт", "image": "1.jpg", "rating": 5.0, "reviews": 135},
        {"id": 2, "name": "Гулей Тетяна", "specialty": "Сертифікований гештальт терапевт", "image": "2.jpg", "rating": 5.0, "reviews": 135},
        {"id": 3, "name": "Оксана Моргоч", "specialty": "Практичний психолог в гештальт підході", "image": "3.jpg", "rating": 5.0, "reviews": 135},
        {"id": 4, "name": "Шевчук Оксана", "specialty": "Гештальт-коуч", "image": "4.jpg", "rating": 5.0, "reviews": 135},
        {"id": 5, "name": "Глушко Олена", "specialty": "Психолог консультант", "image": "5.jpg", "rating": 5.0, "reviews": 135},
    ]
    return render_template('psychologists.html', psychologists=psychologists_data)


@app.route('/psychologist/<int:id>')
def psychologist_detail(id):
    psychologists_data = {
        1: {
            "name": "Наталія Салівон",
            "specialty": "Сертифікований гештальт-терапевт",
            "bio": Markup("""
                Досвід роботи близько 13 років.<br>
                Спеціалізація "Кризи і травми".<br>
                Теми, з якими  працюю:<br>
                Кризи (вікові,в міжособистісних стосунках,екзистенційні);травми;<br>
                втрати;самотність;самогубство; невпевненість в собі;психосоматичні прояви;тривожність;панічні атаки;<br>
                працюю з онкохворими , військовими,Лгбт-friendly.<br>
                Формат сесій - змішаний,очно Одеса та онлайн.<br>
                Вартість сесії 60 хвилин/1400
            """),
            "image": "1.jpg",
            "rating": 5.0,
            "reviews": 135
        },
        2: {
            "name": "Гулей Тетяна",
            "specialty": "Сертифікований гештальт терапевт",
            "bio": Markup("""
                Досвід роботи: 2,5 роки<br>
                Спеціалізація : гештальт терапія з дітьми та сім’єю.<br>
                Напрями роботи:<br>
                розлучення, життя до, після і в моменті.<br>
                Конфлікти , батьківсько- дитячі стосунки.<br>
                Сепарація<br>
                Відновлення опори, ресурсів рухатись вперед.<br>
                Проживання горя, криз<br>
                Ідентичність, проявлення, самореалізація.<br>
                Формат сесій: змішаний, онлайн і очно м. Черніці<br>
                Вартість сесії 60хв/900гр
            """),
            "image": "2.jpg",
            "rating": 5.0,
            "reviews": 135
        },
        3: {
            "name": "Оксана Моргоч",
            "specialty": "Практичний психолог в гештальт підході",
            "bio": Markup("""
                Досвід з 2018 р.<br>
                Працюю з підлітками та дорослими.<br>
                Теми: <br>
                Кризові періоди в житті (розлучення, переїзд, втрата).<br>
                Відносини в парі, батьківсько дитячі, колегіальні.<br>
                Депресія. Тривога. Панічні атаки. У супроводі разом з психіатром.<br>
                Сепарація, пошук себе і свого шляху.<br>
                Підліткова криза. Селфхарм. Суциїдальна поведінка.<br> 
                Пошук життєвий опор. Саморегуляція. <br>
                Працюю онлайн та офлайн м.Чернівці.<br>
                Ціна 1000 грн. 60 хв.
            """),
            "image": "3.jpg",
            "rating": 5.0,
            "reviews": 135
        },
        4: {
            "name": "Шевчук Оксана",
            "specialty": "Гештальт-коуч",
            "bio": Markup("""
                Психотерапевт у навчанні (НАГТУ).<br> 
                Працюю 5 років, спеціалізуюся на парній терапії.<br> 
                Допомагаю знайти внутрішні опори, усвідомити себе, проявитися та будувати гармонійні стосунки — із собою та з оточенням.<br>
                Основні теми: особистісний ріст, вихід з кризи ,  сімейні та робочі стосунки, самоцінність.<br>
                Сесії онлайн або офлайн в Тернополі. 50 хв — 1200 грн.
            """),
            "image": "4.jpg",
            "rating": 5.0,
            "reviews": 135
        },
        5: {
            "name": "Глушко Олена",
            "specialty": "Психолог консультант",
            "bio": Markup("""
                Клінічна спеціалізація в гештальт підході.<br> 
                Працюю з такими темами:<br> 
                Вимушена міграція, кризи пов'язані з нею та адаптація в нових умовах.<br> 
                Депресивні та тривожні стани, панічні атаки, надмірна емоційність чи відсутність емоцій, нав'язливі думки та дії.<br> 
                Почуття сорому, провини, сепарація та дослідження своєї ідентичності.<br> 
                Не працюю з дітьми, підлітками, військовими.<br> 
                Консультація онлайн, 900грн/20євро за 60хв
            """),
            "image": "5.jpg",
            "rating": 5.0,
            "reviews": 135
        }
    }

    psychologist = psychologists_data.get(id)
    if psychologist:
        return render_template('psychologist_detail.html', psychologist=psychologist)
    else:
        return "Психолог не знайдений", 404

@app.route('/publications')
def publications():
    publications_data = [
        {"id": 1, "title": "Як подолати стрес?", "content": "Стрес є частиною нашого життя..."},
        {"id": 2, "title": "Психологічні техніки для зниження тривожності", "content": "Важливо знати, як контролювати свої емоції..."},
        {"id": 3, "title": "Як покращити відносини в сім'ї?", "content": "Сімейна гармонія починається з розуміння..."},
    ]
    return render_template('publications.html', publications=publications_data)

@app.route('/publish/<int:id>')
def publication_detail(id):
    publications_data = {
        1: {"title": "Як подолати стрес?", "content": "Стрес є частиною нашого життя. У цій статті ми розглянемо ефективні методи боротьби зі стресом...", "date": "1 березня 2025"},
        2: {"title": "Психологічні техніки для зниження тривожності", "content": "Тривожність може впливати на якість життя. Дізнайтеся, які техніки допоможуть вам почуватися спокійніше...", "date": "20 лютого 2025"},
        3: {"title": "Як покращити відносини в сім'ї?", "content": "Відносини в сім’ї важливі для щасливого життя. У цій статті ми розглянемо 5 порад для гармонії в родині...", "date": "10 лютого 2025"},
    }

    publication = publications_data.get(id)
    if publication:
        return render_template('publication_detail.html', publication=publication)
    else:
        return "Стаття не знайдена", 404

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    psychologists_data = [
        {"id": 1, "name": "Наталія Салівон"},
        {"id": 2, "name": "Гулей Тетяна"},
        {"id": 3, "name": "Оксана Моргоч"},
        {"id": 4, "name": "Шевчук Оксана"},
        {"id": 5, "name": "Глушко Олена"},
    ]

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        psychologist_id = request.form['psychologist']
        date = request.form['date']
        time = request.form['time']
        message = request.form.get('message', '')

        # Тут можна обробити дані (записати в базу)
        return f"Записано: {name}, email: {email}, до психолога {psychologist_id} на {date} о {time}. Коментар: {message}"

    return render_template('booking.html', psychologists=psychologists_data)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_CREDENTIALS['username'] and password == ADMIN_CREDENTIALS['password']:
            session['admin_logged_in'] = True
            flash("Вхід успішний!", "success")
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Неправильний логін або пароль", "danger")

    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash("Увійдіть в систему для доступу", "warning")
        return redirect(url_for('admin_login'))

    psychologists_data = [
        {"id": 1, "name": "Анна Коваленко", "specialty": "Сімейний психолог"},
        {"id": 2, "name": "Олег Василенко", "specialty": "Клінічний психолог"},
        {"id": 3, "name": "Марія Дорошенко", "specialty": "Дитячий психолог"},
    ]

    publications_data = [
        {"id": 1, "title": "Як подолати стрес?"},
        {"id": 2, "title": "Психологічні техніки для зниження тривожності"},
        {"id": 3, "title": "Як покращити відносини в сім'ї?"},
    ]

    return render_template('admin_dashboard.html', psychologists=psychologists_data, publications=publications_data)

# Додавання психолога
@app.route('/admin/add_psychologist')
def add_psychologist():
    return "Форма додавання психолога"

# Редагування психолога
@app.route('/admin/edit_psychologist/<int:id>')
def edit_psychologist(id):
    return f"Редагування психолога з ID {id}"

# Видалення психолога
@app.route('/admin/delete_psychologist/<int:id>')
def delete_psychologist(id):
    flash("Психолога успішно видалено", "success")
    return redirect(url_for('admin_dashboard'))

# Додавання публікації
@app.route('/admin/add_publication')
def add_publication():
    return "Форма додавання публікації"

# Редагування публікації
@app.route('/admin/edit_publication/<int:id>')
def edit_publication(id):
    return f"Редагування публікації з ID {id}"

# Видалення публікації
@app.route('/admin/delete_publication/<int:id>')
def delete_publication(id):
    flash("Публікацію успішно видалено", "success")
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash("Ви вийшли з системи", "info")
    return redirect(url_for('admin_login'))

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)