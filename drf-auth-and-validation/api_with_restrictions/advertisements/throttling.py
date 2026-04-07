from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonAdvertisementThrottle(AnonRateThrottle):
    """
    Ограничение для анонимных пользователей.
    """
    # Допускаем 10 запросов в минуту с одного IP
    rate = '10/minute'


class UserAdvertisementThrottle(UserRateThrottle):
    """
    Ограничение для авторизованных пользователей.
    """
    # Допускаем 20 запросов в минуту для каждого пользователя
    rate = '20/minute'
