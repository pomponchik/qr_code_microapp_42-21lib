# qr_code_microapp_42-21lib

Переменные окружения:

QR_URL - ip сервиса.
QR_PORT - порт сервиса.

При недоступности данных переменных, программа проверяет переменные URL и PORT (к значению порта прибавляет единицу).


Необязательные переменные окружения:

SITE_URL - URL собственно сайта, который будет вставляться в qr-коды

ЛИБО можно прописать 3 переменных:

SITE_IP - IP-адрес, строка только из цифр и строк (без префикса с протоколом)
SITE_PORT - порт
SITE_ROUTE - ссылка для перенаправления, начинается со слэша (можно просто слэш)

Если переменные окружения не заданы, будет подставляться ссылка на https://library.21-school.ru/

-------------

Запуск:

1. Установить переменные окружения из списка выше.
2. Войти в виртуальное окружение.
3. Установить пакеты из requirements.txt (если не установлены ранее)
4. Выполнить команду "python3 qr_app/qr_routes.py"

-------------

API:

<адрес сервиса>/api/get/all - возвращает PDF-файл со списком книг и QR-кодами.
